from typing import Any

from validation.rules.BaseRule import BaseRule


class After(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        # TODO: work on it more...
        # specified_date = datetime.strptime(self.payload, "%Y-%m-%d")
        return True

    def message(self, attribute: str) -> str:
        return f"{attribute} is not accepted"
