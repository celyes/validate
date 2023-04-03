from typing import Any

from validation.rules.BaseRule import BaseRule


class Between(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        self.payload.sort()
        return (
            int(self.payload[0]) <= int(value) <= int(self.payload[-1])
            if value
            else False
        )

    def message(self, attribute: str) -> str:
        return f"`{attribute}` is not in the specified range"
