from typing import Any, List, Dict, Tuple, Union

from checkr.exceptions import InvalidRuleException
from checkr.rules.BaseRule import BaseRule


class ArrayOf(BaseRule):
    def __get_type_from_string(self, type_string):
        types = {
            "int": int,
            "float": float,
            "complex": complex,
            "string": str,
            "bool": bool,
            "dict": Dict,
            "set": set,
            "frozenset": frozenset,
            "list": List,
            "tuple": Tuple,
            "range": range,
        }
        return types[type_string]

    def validate(self, attribute: str, value: Any) -> bool:
        try:
            requested_types = [
                self.__get_type_from_string(type_string=type_string)
                for type_string in self.payload
            ]
            return all(isinstance(v, Union[tuple(requested_types)]) for v in value)
        except KeyError as e:
            raise InvalidRuleException(
                f"Payload {e} is not allowed on current rule. check the payload name."
            )

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not fully composed of one of these type: `{self.payload}`"
