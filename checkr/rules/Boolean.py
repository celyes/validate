from typing import Any

from checkr.rules.BaseRule import BaseRule


class Boolean(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, bool)

    def message(self, attribute: str) -> str:
        return f"{attribute} is not a boolean"
