from abc import ABCMeta
from typing import Dict, Union, List, Any

from validation.exceptions import InvalidRuleException, UnauthorizedRequestException
from validation.rules.BaseRule import BaseRule
from validation.rules_map import rules_to_objects_map


class BaseRequest(metaclass=ABCMeta):
    __is_valid = False
    __data = {}
    __errors = {}
    __rules_map = rules_to_objects_map
    __user_provided_validation_messages = {}

    @staticmethod
    def rules() -> Dict:
        """Returns a dictionary of validation rules for the request.

        :raises NotImplementedError: The method is not implemented.
        :return: A dictionary of validation rules.
        :rtype: dict
        """
        raise NotImplementedError("Method `rules` not implemented")

    @staticmethod
    def authorize() -> bool:
        raise NotImplementedError("Method `authorize` not implemented")

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
        """Handles validation for the given rules and returns validation result.

        :return: A boolean value indicating whether the data passes the validation or a dictionary containing error
        messages.
        :rtype: bool or dict
        """
        cls.__user_provided_validation_messages = cls.messages() or {}
        if cls.authorize():
            rules = cls.rules()
            for field_rules in rules:
                cls.__validate_single_field(
                    rules_map=cls.__rules_map,
                    attribute=field_rules,
                    rules=rules[field_rules],
                    value=cls.__data.get(field_rules),
                )
            after_validation_errors = cls.get_errors()
            if len(after_validation_errors.values()) == 0:
                cls.__is_valid = True
                return True
            return cls.get_errors()
        raise UnauthorizedRequestException("Request is not authorized.")

    @classmethod
    def passes(cls) -> bool:
        return cls.__is_valid

    @classmethod
    def prepare_for_validation(cls) -> None:
        """A hook that executes before starting the validation process.

        :return: Nothing
        :rtype: None
        """
        pass

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
    def passed_validation(cls) -> None:
        """A hook that executes after the validation succeeds and the data is valid.

        :return: None
        :rtype: None
        """
        pass

    @classmethod
    def __validate_single_field(
        cls, rules_map: Dict, attribute: str, rules: Union[str, List], value: Any
    ) -> None:
        """Validates a single field against the given rules.

        :param attribute: The attribute being validated.
        :type attribute: str
        :param rules: The rules to validate against, as a list or a pipe-separated string.
        :type rules: Union[list, str]
        :param value: The value of the attribute being validated.
        :type value: Any
        :return: None
        :rtype: None
        """
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
                        f"Rule `{extracted_rule_with_data['rule_name']} does not exist. check the rule name."
                    )
            else:
                rule_object = rule
            try:
                if not rule_object.validate(attribute=attribute, value=value):
                    field_errors.append(
                        cls.__get_user_provided_message(
                            attribute=attribute,
                            extracted_rule=extracted_rule_with_data,
                            rule=rule,
                        )
                        or rule_object.message(attribute=attribute)
                    )
            except (ValueError, AttributeError):
                raise InvalidRuleException(
                    f"Invalid validation rule: {extracted_rule_with_data['rule_name']}. Check your request "
                    f"class."
                )
        if len(field_errors) > 0:
            cls.set_field_errors(attribute, field_errors)

    @classmethod
    def __get_user_provided_message(
        cls,
        attribute: str,
        extracted_rule: Union[Dict, None],
        rule: Union[BaseRule, str],
    ) -> str:
        return (
            cls.__user_provided_validation_messages.get(
                f"{attribute}.{extracted_rule['rule_name']}"
            )
            if isinstance(rule, str)
            else None
        )

    @classmethod
    def get_errors(cls) -> Dict:
        """Returns the validation errors stored in the class.

        :return: A dictionary containing errors resulting from the validation process.
        :rtype: dict
        """
        return cls.__errors

    @classmethod
    def set_field_errors(cls, attribute: str, errors_list: List) -> None:
        """Sets the errors for the specified field.

        :param attribute: The attribute to set the errors for.
        :type attribute: str
        :param errors_list: The list of errors to set.
        :type errors_list: list
        :return: None
        :rtype: None
        """
        cls.__errors[attribute] = errors_list

    @classmethod
    def extract_rule_data(cls, rule: str) -> Dict:
        rule_parts = rule.split(":")
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

    @classmethod
    def messages(cls) -> Dict:
        pass

    def get_data(self) -> Dict:
        return self.__data
