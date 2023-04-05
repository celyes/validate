import ipaddress
from typing import Any

from .BaseRule import BaseRule


class Ipv4(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            ip = ipaddress.ip_address(value)
            return True if ip.version == 4 else False
        except ValueError:
            return False

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not a valid IPv4 address"
