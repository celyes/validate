import json
from typing import Union, List, Dict


class ErrorBag:
    def __init__(self):
        self.__errors: Dict = {}

    def __str__(self):
        return json.dumps(self.__errors)

    def add_error(self, key, error: Union[List, Dict, str]):
        previous_field_error = self.__errors.get(key)
        if len(error) > 0:
            if previous_field_error:
                self.__errors[key] = previous_field_error + (
                    error if isinstance(error, List) else [error]
                )
            else:
                self.__errors[key] = error if isinstance(error, List) else [error]

    def is_not_empty(self):
        return len(self.__errors.values()) > 0
