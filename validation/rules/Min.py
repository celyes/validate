from typing import Any

from validation.rules.BaseRule import BaseRule


class Min(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return len(value) >= int(self.payload)

    def message(self, attribute: str) -> str:
        return f"{attribute} length is smaller than {self.payload}"
