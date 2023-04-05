# Checkr

Checkr is a powerful validation library that enables developers to easily and accurately validate user input and other
data. With Checkr, you can quickly perform a wide range of checks, and ensuring that data conforms to specific
formatting requirements. With a simple and intuitive API, Checkr is easy to integrate into any project, and its flexible
configuration options make it a powerful
tool for building robust and reliable applications.
### Installation
```shell
pip install checkr
```

### Usage

1. First of all, You need to create a request class that has two methods:

```python
from checkr.BaseRequest import BaseRequest
from typing import Dict


class SampleRequest(BaseRequest):

    @staticmethod
    def authorize() -> bool:
        return True

    @staticmethod
    def rules() -> Dict:
        return {
            'name': 'required|string|min:3',  # You can use the pipe
            'age': ['required', 'numeric', 'gte:18'],  # Or you can just provide a list
        }
```

2. Use the request class to validate data:

```python
from checkr import validate
from checkr.exceptions import ValidationError


request_data = {
    'name': 'john doe'
}

try:
    validate(SampleRequest, request_data)
except ValidationError as e:
    # Do anything with the validation result here.
    print(e.errors)
```

### Authorizing the request

This method is useful when you want to ensure that validation is performed only by certain parties or by specific users.
In your request class, include a static method named `authorize` that returns a boolean.

### Customizing the validation messages

To customize the validation messages returned when the validation of a field fails,
you can use the `messages` method. Here's an example:

```python
from typing import Dict
from checkr.BaseRequest import BaseRequest


class SampleRequest(BaseRequest):
    ...

    @classmethod
    def messages(cls) -> Dict:
        return {
            'name.required': 'Please provide a name!',
            'age.number': 'Oops! not a number!'
        }

    ...
```

### Adding fields before starting the validation

Sometimes, you may find it useful to add a field before the process of validation starts.
You can accomplish this by using the `prepare_for_validation` hook as demonstrated in the following example:

```python
from typing import Dict
from checkr.BaseRequest import BaseRequest


class SampleRequest(BaseRequest):
    ...

    @classmethod
    def prepare_for_validation(cls) -> Dict:
        cls.merge(data_to_add={'foo': 'bar'})

    ...
```

### Adding fields after finishing the validation

It's almost identical to adding fields before starting the validation. You'll use
`passed_validation` hook as demonstrated in the following example:

Notice that this method will not run if the validation finds invalid data.

```python
from typing import Dict
from checkr.BaseRequest import BaseRequest


class SampleRequest(BaseRequest):
    ...

    @classmethod
    def passed_validation(cls) -> Dict:
        cls.merge(data_to_add={'foo': 'bar'})

    ...
```

### Available rules

| Rule Name            | Description                                                                                                                                                                          | Usage                                                                                                                                     |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| between              | Checks if a value is between a minimum and maximum value                                                                                                                             | `between:x,y` where `x` and `y` are required. If provided with more than 2 numbers, the first and last numbers will be taken into account |
| string               | Checks if a value is a string                                                                                                                                                        | `string`                                                                                                                                  |
| int                  | Checks if a value is an integer                                                                                                                                                      | `int`                                                                                                                                     |
| required             | Checks if a value is present                                                                                                                                                         | `required`                                                                                                                                |
| numeric              | Checks if a value is numeric                                                                                                                                                         | `numeric`                                                                                                                                 |
| array                | Checks if a value is a valid Python list                                                                                                                                             | `array`                                                                                                                                   |
| array_of             | Checks if an array contains only elements of a specific type                                                                                                                         | `array_of:string`                                                                                                                         |
| in_array             | Checks if a value is in an array of valid options                                                                                                                                    | `in_array:a,b,c`                                                                                                                          |
| not_in_array         | Checks if a value is not in a list of invalid options                                                                                                                                | `not_in_array:a,b,c`                                                                                                                      |
| date_after           | Checks if a date is after a specific date                                                                                                                                            | `date_after:YYYY-mm-dd`                                                                                                                   |
| date_after_or_equal  | Checks if a date is after or equal to a specific date                                                                                                                                | `date_after_or_equal:YYYY-mm-dd`                                                                                                          |
| date_before          | Checks if a date is before a specific date                                                                                                                                           | `date_before:YYYY-mm-dd`                                                                                                                  |
| date_before_or_equal | Checks if a date is before or equal to a specific date                                                                                                                               | `date_before_or_equal:YYYY-mm-dd`                                                                                                         |
| min                  | Checks if a value is greater than or equal to a minimum value if it's a number. If provided a string, it checks if the string length is greater than or equal to the provided value. | `min:x` where `x` is a number amd required                                                                                                |
| max                  | Checks if a value is greater than or equal to a maximum value if it's a number. If provided a string, it checks if the string length is less than or equal to the provided value.	   | `max:x` where `x` is a number and required                                                                                                |
| min_digits           | Checks if a numeric value has at least a specified number of digits                                                                                                                  | `min_digits:n`                                                                                                                            |
| max_digits           | Checks if a numeric value has at most a specified number of digits                                                                                                                   | `max_digits:n`                                                                                                                            |
| json                 | Checks if a value is a valid JSON object                                                                                                                                             | `json`                                                                                                                                    |
| nullable             | Allows a value to be null or undefined                                                                                                                                               | `nullable`                                                                                                                                |
| decimal              | Checks if a value is a decimal number                                                                                                                                                | `decimal:x` where `x` is the number of decimal places and is optional                                                                     |
| gt                   | Checks if a value is greater than a specified value                                                                                                                                  | `gt:x` where `x` is a number                                                                                                              |
| gte                  | Checks if a value is greater than or equal to a specified value                                                                                                                      | `gte:x` where `x` is a number                                                                                                             |
| lt                   | Checks if a value is less than a specified value                                                                                                                                     | `lt:x` where `x` is a number                                                                                                              |
| lte                  | Checks if a value is less than or equal to a specified value                                                                                                                         | `lte:x` where `x` is a number                                                                                                             |
| ip                   | Checks if a value is a valid IPv4 or IPv6 address                                                                                                                                    | `ip`                                                                                                                                      |
| ipv4                 | Checks if a value is a valid IPv4 address                                                                                                                                            | `ipv4`                                                                                                                                    |
| ipv6                 | Checks if a value is a valid IPv6 address                                                                                                                                            | `ipv6`                                                                                                                                    |
| lowercase            | Checks if a string is lowercase                                                                                                                                                      | `lowercase`                                                                                                                               |
| uppercase            | Checks if a string is uppercase                                                                                                                                                      | `uppercase`                                                                                                                               |
| mac_address          | Checks if a value is a valid MAC address                                                                                                                                             | `mac_address`                                                                                                                             |
| uuid                 | Checks if a value is a valid UUID                                                                                                                                                    | `uuid:v` where `v` is the version and defaults to v4 if no version provided                                                               |
| ulid                 | Checks if a value is a valid ULID                                                                                                                                                    | `ulid`                                                                                                                                    |
| url                  | Checks if a value is a valid URL                                                                                                                                                     | `url`                                                                                                                                     |
| startswith           | Checks if a string starts with a specific value                                                                                                                                      | `startswith`                                                                                                                              |
| endswith             | Checks if a string ends with a specific value                                                                                                                                        | `endswith`                                                                                                                                |
| email                | Checks if a value is a valid email address                                                                                                                                           | `email`                                                                                                                                   |
| bool                 | Checks if a value is a boolean (true or false)                                                                                                                                       | `bool`                                                                                                                                    |

### Adding custom validation rules:

In some cases, it is useful to create a rule that validates an input in custom way like checking if a phone number has a
specific format or checking that a city name exists in reality. The following example demonstrates how to accomplish
this:

```python
from typing import Any
from checkr.rules.BaseRule import BaseRule

class CustomRule(BaseRule):

    def __str__(self):
        return 'custom_rule'  # required. If not provided, incorrect errors dictionary will be returned

    def validate(self, attribute: str, value: Any) -> bool:
        return True

    def message(self, attribute: str):
        return f'This field failed because something was incorrect'

```

You can use the `validate` method to validate against a condition.
note that this method takes two arguments:

* `attribute` which is the name of the field
* `value` which is the actual value.

There's also another method called `message` which is used to return a message in case the validation fails. This method
receives one parameter, `attribute`, which is the name of the field under validation.
