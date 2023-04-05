from typing import Any

from .rules.BaseRule import BaseRule


class Gte(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            return value >= float(self.payload[0])
        except TypeError:
            return False

    def message(self, attribute: str) -> str:
        try:
            return f"'{attribute}' is not greater than or equal to {self.payload[0]}"
        except TypeError:
            return "You haven't specified any value for comparison"
