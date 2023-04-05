from typing import Any

from .BaseRule import BaseRule


class Required(BaseRule):
    def validate(self, attribute: str, value: Any = None) -> bool:
        return value is not None

    def message(self, attribute: str) -> str:
        return f"{attribute} field is required"
