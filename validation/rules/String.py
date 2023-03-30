from typing import Any

from validation.rules.BaseRule import BaseRule


class String(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, str)

    def message(self) -> str:
        return 'field value is not a string'
