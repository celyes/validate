from typing import Any

from .BaseRule import BaseRule


class Decimal(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        if self.payload:
            return isinstance(value, float) and int(self.payload[0]) <= str(value)[
                ::-1
            ].find(".") <= int(self.payload[-1])
        else:
            return isinstance(value, float)

    def message(self, attribute: str) -> str:
        if self.payload:
            return f"{attribute} does not have the correct number of decimal places"
        return f"'{attribute}' is not a decimal number."
