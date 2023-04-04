from typing import Any

from checkr.rules.BaseRule import BaseRule


class InArray(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return value in self.payload

    def message(self, attribute: str) -> str:
        return f"{attribute} is not in the given list"
