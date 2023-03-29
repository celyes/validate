import json

from requests.models import Response

from typing import Callable, Dict

from .BaseRequest import BaseRequest


def validate(validation_class, request_data: Dict):
    def decorator(route_func: Callable):
        def wrapper():
            validation_class.set_data(data=request_data)
            validation_class.prepare_for_validation()
            validation_class.handle()
            if not validation_class.passes():
                return respond_with_errors(errors=validation_class.get_errors())
            validation_class.passed_validation()
            return route_func()

        wrapper()

    return decorator


def respond_with_errors(errors: Dict):
    response = Response()
    response.headers = {'Content-Length': len(json.dumps(errors)), 'Content-Type': 'application/json'}
    response.status_code = 422
    response._content = json.dumps({
        'errors': errors,
        'success': False,
        'status': response.status_code
    })
    return response


def encapsulate_errors(errors: Dict, status_code: int) -> Dict:
    return {
        'errors': errors,
        'success': False,
        'status': status_code
    }
