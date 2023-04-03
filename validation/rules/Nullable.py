from typing import Any

from validation.rules.BaseRule import BaseRule


class Nullable(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return value is None

    def message(self, attribute: str) -> str:
        return f"{attribute} is not nullable"
