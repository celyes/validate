from typing import Any

from checkr.rules.BaseRule import BaseRule


class Startswith(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, str) and value.startswith(self.payload)

    def message(self, attribute: str) -> str:
        return f"`{attribute}` does not start with the `{self.payload}`"
