from abc import ABCMeta
from typing import Dict, Union
from validation.rules_map import RULES


class BaseRequest(metaclass=ABCMeta):
    __is_valid = False
    __data = {}
    __errors = {}

    @staticmethod
    def rules() -> Dict:
        raise NotImplementedError("Method not implemented")

    @classmethod
    def set_data(cls, data: Dict) -> None:
        cls.__data = data

    @classmethod
    def handle(cls) -> Union[bool, Dict]:
        rules = cls.rules()
        for field_rules in rules:
            cls.__validate_single_field(field_rules, rules[field_rules], cls.__data.get(field_rules))
        after_validation_errors = cls.get_errors()
        if len(after_validation_errors.values()) == 0:
            cls.__is_valid = True
            return True
        return cls.get_errors()

    @classmethod
    def passes(cls) -> bool:
        return cls.__is_valid

    @classmethod
    def prepare_for_validation(cls) -> None:
        pass

    @classmethod
    def merge(cls, data_to_add: Dict) -> None:
        cls.__data = {**cls.__data, **data_to_add}

    @classmethod
    def passed_validation(cls) -> None:
        pass

    @classmethod
    def __validate_single_field(cls, attribute, rules, value) -> None:
        if isinstance(rules, str):
            rules = rules.split('|')
        field_errors = []
        for rule in rules:
            rule_object = RULES[rule]()
            if not rule_object.validate(attribute=attribute, value=value):
                field_errors.append(rule_object.message())
        if len(field_errors) > 0:
            cls.set_field_errors(attribute, field_errors)

    @classmethod
    def get_request_data(cls) -> Dict:
        return cls.__data

    @classmethod
    def get_errors(cls) -> Dict:
        return cls.__errors

    @classmethod
    def set_field_errors(cls, attribute, errors_list):
        cls.__errors[attribute] = errors_list

    @classmethod
    def add_metadata(cls, metadata: Dict):
        cls.__data['_meta'] = metadata
