import ipaddress
from typing import Any

from checkr.rules.BaseRule import BaseRule


class Ipv6(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            ip = ipaddress.ip_address(value)
            return True if ip.version == 6 else False
        except ValueError:
            return False

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not a valid IPv6 address"
