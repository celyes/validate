from typing import Any

from checkr.rules.BaseRule import BaseRule


class String(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, str)

    def message(self, attribute: str) -> str:
        return f"{attribute} is not a string"
