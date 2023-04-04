from typing import Any

from validation.rules.BaseRule import BaseRule


class Lowercase(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return str(value).lower() == str(value)

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not lowercased"
