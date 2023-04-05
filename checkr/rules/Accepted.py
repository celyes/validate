from typing import Any

from .BaseRule import BaseRule


class Accepted(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return value in ["yes", "on", 1, True]

    def message(self, attribute: str) -> str:
        return f"{attribute} is not accepted"
