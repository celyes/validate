from typing import Any

from .BaseRule import BaseRule


class Integer(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, int)

    def message(self, attribute: str) -> str:
        return f"{attribute} is not an integer"
