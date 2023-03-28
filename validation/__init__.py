from typing import Callable, Dict

from .BaseRequest import BaseRequest


def validate(validation_class: BaseRequest, request_data: Dict):
    def decorator(route_func: Callable):
        def wrapper():
            validation_class.handle(data=request_data)
            if not validation_class.passes():
                return reject()
            route_func()
        wrapper()
    return decorator


def reject():
    print("Oops! invalid request")
