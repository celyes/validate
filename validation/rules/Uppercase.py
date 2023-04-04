from typing import Any

from validation.rules.BaseRule import BaseRule


class Uppercase(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return str(value).upper() == str(value)

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not uppercased"
