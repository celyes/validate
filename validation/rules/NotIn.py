from typing import Any

from validation.rules.BaseRule import BaseRule


class NotIn(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        if value:
            return value not in self.payload
        return True

    def message(self, attribute: str) -> str:
        return f"`{attribute}` is in `{self.payload}`"
