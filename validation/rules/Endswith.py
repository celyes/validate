from typing import Any

from validation.rules.BaseRule import BaseRule


class Endswith(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, str) and value.endswith(self.payload)

    def message(self, attribute: str) -> str:
        return f"`{attribute}` does not end with the `{self.payload}`"
