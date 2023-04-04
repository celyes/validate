from typing import Any

from checkr.rules.BaseRule import BaseRule


class MaxDigits(BaseRule):
    __message = None

    def validate(self, attribute: str, value: Any) -> bool:
        try:
            return float(self.payload) >= len(str(value).replace(".", ""))
        except ValueError:
            self.__message = f"{attribute[0]} value is not a valid float or int"
            return False

    def message(self, attribute: str) -> str:
        return (
            f"{attribute} number of digits is more than {self.payload}"
            if not self.__message
            else self.__message
        )
