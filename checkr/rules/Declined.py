from typing import Any

from .BaseRule import BaseRule


class Declined(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return value in ["no", "off", 0, False]

    def message(self, attribute: str) -> str:
        return f"{attribute} is not declined"
