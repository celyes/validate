from typing import Union, Any

from .BaseRule import BaseRule


class Numeric(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            float(value)
        except (ValueError, TypeError):
            return False
        return True

    def message(self, attribute: str) -> str:
        return f"{attribute} is non-numeric"
