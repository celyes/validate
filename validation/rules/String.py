from validation.rules.BaseRule import BaseRule


class String(BaseRule):
    def validate(self, attribute, value) -> bool:
        return isinstance(value, str)

    def message(self) -> str:
        return 'Field value is not a string'
