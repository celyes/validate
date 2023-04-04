import ipaddress
from typing import Any

from validation.rules.BaseRule import BaseRule


class Ip(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            ipaddress.ip_address(value)
            return True
        except ValueError:
            return False

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not a valid IP address"
