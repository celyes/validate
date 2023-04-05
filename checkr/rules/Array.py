from typing import Any, List

from .rules.BaseRule import BaseRule


class Array(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, List)

    def message(self, attribute: str) -> str:
        return f"{attribute} is not an array"
