from validation.rules.BaseRule import BaseRule


class Required(BaseRule):
    def validate(self, attribute, value = None) -> bool:
        return value is not None

    def message(self) -> str:
        return 'field is required'
