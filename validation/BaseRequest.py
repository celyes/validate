from abc import ABCMeta
from typing import Dict
from validation.rules_map import rules_map


class BaseRequest(metaclass=ABCMeta):
    is_valid = False
    errors = {}

    @staticmethod
    def rules():
        raise NotImplementedError("Method not implemented")

    @classmethod
    def handle(cls, data: Dict):
        rules = cls.rules()
        for field in rules:
            cls.validate_single_field(field, rules[field], data.get(field))
        cls.is_valid = (len(cls.errors.values()) == 0)

    @classmethod
    def passes(cls):
        return cls.is_valid

    @classmethod
    def validate_single_field(cls, attribute, rules, value):
        if isinstance(rules, str):
            rules = rules.split('|')
        field_errors = []
        for rule in rules:
            rule_object = rules_map[rule]()
            if not rule_object.validate(attribute=attribute, value=value):
                field_errors.append(rule_object.message())
        if len(field_errors) > 0:
            cls.errors[attribute] = field_errors
