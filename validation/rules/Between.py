from typing import Any

from validation.rules.BaseRule import BaseRule
from validation.exceptions import InvalidRuleException


class Between(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        self.payload.sort()
        return int(self.payload[0]) <= int(value) <= int(self.payload[-1])

    def message(self) -> str:
        return 'field value is not in specified range'
