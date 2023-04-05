from typing import Any

from .BaseRule import BaseRule


class Gte(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            return float(value) >= float(self.payload)
        except (TypeError, ValueError):
            return False

    def message(self, attribute: str) -> str:
        try:
            return f"'{attribute}' is not greater than or equal to {self.payload}"
        except TypeError:
            return "You haven't specified any value for comparison"
