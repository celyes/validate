from typing import Any

from validation.rules.BaseRule import BaseRule


class Gt(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            return value > float(self.payload[0])
        except:
            raise

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not bigger than {self.payload[0]}"
