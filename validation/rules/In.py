from typing import Any

from validation.rules.BaseRule import BaseRule


class In(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        if value:
            return value in self.payload
        return True

    def message(self, attribute: str) -> str:
        return f"`{attribute}` is not in `{self.payload}`"
