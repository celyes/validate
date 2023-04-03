import json
from typing import Union, List, Dict


class ErrorBag:
    def __init__(self):
        self.__cursor = 0
        self.__errors: Dict = {}
        self.__field: str = ""
        self.__level: int = 0

    def __str__(self):
        return json.dumps(self.__errors)

    def add_error(self, rule_name: str, error: Union[List, Dict, str]) -> None:
        if len(error) > 0:
            current_field = self.get_current_field()[0]
            current_field_errors = self.__errors.get(current_field)
            if current_field_errors:
                self.__errors[current_field] = {
                    **current_field_errors,
                    **{rule_name: error},
                }
            else:
                self.__errors[current_field] = {rule_name: error}

    def has_errors(self) -> bool:
        return len(self.__errors.values()) > 0

    def get_current_field(self) -> str:
        return self.__field

    def set_current_field(self, field: Union[List, str]) -> None:
        self.__field = field

    def reset_current_field(self) -> None:
        self.set_current_field(field="")
