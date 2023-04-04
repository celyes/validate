from abc import ABCMeta
from typing import Dict, Union, List, Any

from checkr.ErrorBag import ErrorBag
from checkr.exceptions import (
    InvalidRuleException,
    UnauthorizedRequestException,
)

from checkr.rules_map import rules_to_objects_map


class BaseRequest(metaclass=ABCMeta):
    __is_valid = False
    __data = {}
    __errors = {}
    __rules_map = rules_to_objects_map
    __user_provided_validation_messages = {}
    __error_bag = ErrorBag()

    @staticmethod
    def authorize() -> bool:
        raise NotImplementedError("Method `authorize` not implemented")

    @staticmethod
    def rules() -> Dict:
        """Returns a dictionary of checkr rules for the request.

        :raises NotImplementedError: The method is not implemented.
        :return: A dictionary of checkr rules.
        :rtype: dict
        """
        raise NotImplementedError("Method `rules` not implemented")

    @classmethod
    def prepare_for_validation(cls) -> None:
        """A hook that executes before starting the checkr process.

        :return: Nothing
        :rtype: None
        """
        pass

    @classmethod
    def passed_validation(cls) -> None:
        """A hook that executes after the checkr succeeds and the data is valid.

        :return: None
        :rtype: None
        """
        pass

    @classmethod
    def messages(cls) -> Dict:
        pass

    @classmethod
    def set_data(cls, data: Dict) -> None:
        """Sets the request data for the class.

        :param data: The data to set for the request.
        :type data: dict
        :return: None
        :rtype: None
        """
        cls.__data = data

    @classmethod
    def handle(cls) -> Union[bool, Dict]:
        """Handles checkr for the given rules and returns checkr result.

        :return: A boolean value indicating whether the data passes the checkr or a dictionary containing error
        messages.
        :rtype: bool or dict
        """
        cls.__user_provided_validation_messages = cls.messages() or {}
        if cls.authorize():
            fields = cls.rules()
            for field in fields:
                cls.__error_bag.set_current_field(field=field)
                cls.__validate_field(
                    rules_map=cls.__rules_map,
                    attribute=field,
                    rules=fields[field],
                    value=cls.__data.get(field.split(".")[0]),
                )
            if cls.__error_bag.has_errors():
                cls.__is_valid = False
                return False
            cls.__is_valid = True
            return True
        raise UnauthorizedRequestException("Request is not authorized.")

    @classmethod
    def passes(cls) -> bool:
        return cls.__is_valid

    @classmethod
    def merge(cls, data_to_add: Dict) -> None:
        """Merges the given dictionary of data into the existing request data.

        :param data_to_add: The dictionary of data to merge.
        :type data_to_add: dict
        :return: None
        :rtype: None
        """
        cls.__data = {**cls.__data, **data_to_add}

    @classmethod
    def __validate_field(
        cls, rules_map: Dict, attribute: str, rules: Union[str, List], value: Any
    ) -> ErrorBag:
        """Validates a single field against the given rules.

        :param attribute: The attribute being validated.
        :type attribute: str
        :param rules: The rules to validate against, as a list or a pipe-separated string.
        :type rules: Union[list, str]
        :param value: The value of the attribute being validated.
        :type value: Any
        :return: List
        :rtype: List
        """
        attribute = attribute.split(".")
        cls.__error_bag.set_current_field(field=attribute)
        validation_errors = cls.__validate_nested_field(
            rules_map=rules_map,
            attribute=attribute,
            rules=rules,
            value=value,
        )
        cls.__error_bag.reset_current_field()
        return validation_errors

    @classmethod
    def __validate_single_field(
        cls, rules_map: Dict, attribute: str, rules: Union[str, List], value: Any
    ):
        is_custom_rule = False
        if isinstance(rules, str):
            rules = rules.split("|")
        field_errors = []
        extracted_rule_with_data = None
        for rule in rules:
            if isinstance(rule, str):
                try:
                    extracted_rule_with_data = cls.extract_rule_data(rule=rule)
                    rule_object = rules_map[extracted_rule_with_data["rule_name"]]()
                    rule_object.set_validation_payload(
                        payload=extracted_rule_with_data["rule_payload"]
                    )
                except KeyError:
                    raise InvalidRuleException(
                        f"Invalid validation rule: {extracted_rule_with_data['rule_name']}. "
                        f"Check the provided rules dictionary."
                    )
            else:
                rule_object = rule
                is_custom_rule = True
            try:
                if not rule_object.validate(attribute=attribute, value=value):
                    custom_validation_message = cls.__user_provided_validation_messages.get(
                        f'{cls.__error_bag.get_current_field()[0]}.{extracted_rule_with_data["rule_name"]}'
                    )
                    cls.__error_bag.add_error(
                        rule_name=extracted_rule_with_data["rule_name"]
                        if not is_custom_rule
                        else str(rule),
                        error=custom_validation_message
                        or rule_object.message(attribute=attribute[0]),
                    )
            except (ValueError, AttributeError):
                raise InvalidRuleException(
                    f"Invalid validation rule: {extracted_rule_with_data['rule_name']}. "
                    f"Check the provided rules dictionary."
                )
        return field_errors

    @classmethod
    def __validate_nested_field(
        cls,
        rules_map: Dict,
        attribute: Union[str, List],
        rules: Union[str, List],
        value: Any,
    ):
        if len(attribute) == 1:
            if attribute[0] == "*":
                for key, single_value in enumerate(value):
                    cls.__validate_single_field(
                        rules_map=rules_map,
                        attribute=attribute,
                        rules=rules,
                        value=single_value,
                    )
            else:
                cls.__validate_single_field(
                    rules_map=rules_map,
                    attribute=attribute,
                    rules=rules,
                    value=value[attribute[0]] if isinstance(value, Dict) else value,
                )
        else:
            if attribute[0] == "*":
                try:
                    for key, single_value in enumerate(value):
                        cls.__validate_nested_field(
                            rules_map=rules_map,
                            attribute=attribute[1:],
                            rules=rules,
                            value=single_value.get(attribute[1]),
                        )
                except TypeError:
                    custom_rule = cls.__user_provided_validation_messages.get(
                        f"{cls.__error_bag.get_current_field()[0]}.required"
                    )
                    cls.__error_bag.add_error(
                        rule_name="required", error=custom_rule or "Field is required"
                    )
            else:
                cls.__validate_nested_field(
                    rules_map=rules_map,
                    attribute=attribute[1:],
                    rules=rules,
                    value=value,
                )
        return cls.__error_bag

    @classmethod
    def get_errors(cls) -> ErrorBag:
        """Returns the checkr errors stored in the class.

        :return: A dictionary containing errors resulting from the checkr process.
        :rtype: dict
        """
        return cls.__error_bag

    @classmethod
    def extract_rule_data(cls, rule: str) -> Dict:
        rule_parts = rule.split(":", 1)
        rule_name = rule_parts[0]
        rule_payload = rule_parts[-1] if rule_parts[0] != rule_parts[-1] else None
        return {
            "rule_name": rule_name,
            "rule_payload": (
                cls.extract_rule_payload(rule_payload) if rule_payload else rule_payload
            ),
        }

    @classmethod
    def extract_rule_payload(cls, payload: str) -> Union[List, str]:
        payload = payload.split(",")
        return payload[0] if len(payload) == 1 else payload

    def get_data(self) -> Dict:
        return self.__data
