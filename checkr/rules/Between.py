from typing import Any

from .rules.BaseRule import BaseRule


class Between(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        self.payload.sort()
        try:
            return (
                float(self.payload[0]) <= float(value) <= float(self.payload[-1])
                if value
                else False
            )
        except ValueError:
            return False

    def message(self, attribute: str) -> str:
        return f"`{attribute}` is not in the specified range"
