import re
from typing import Any

from checkr.rules.BaseRule import BaseRule


class MacAdress(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        is_valid_mac = re.match(
            r"([0-9A-F]{2}[:]){5}[0-9A-F]{2}|([0-9A-F]{2}[-]){5}[0-9A-F]{2}",
            string=value or "",
            flags=re.IGNORECASE,
        )
        try:
            return bool(is_valid_mac.group())
        except AttributeError:
            return False

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not a valid MAC address"
