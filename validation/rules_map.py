from validation.rules.DateAfter import DateAfter
from validation.rules.DateAfterOrEqual import DateAfterOrEqual
from validation.rules.ArrayOf import ArrayOf
from validation.rules.DateBefore import DateBefore
from validation.rules.DateBeforeOrEqual import DateBeforeOrEqual
from validation.rules.InArray import InArray
from validation.rules.Array import Array
from validation.rules.String import String
from validation.rules.Required import Required
from validation.rules.Numeric import Numeric
from validation.rules.Between import Between

rules_to_objects_map = {
    "between": Between,
    "string": String,
    "required": Required,
    "numeric": Numeric,
    "in_array": InArray,
    "array": Array,
    "array_of": ArrayOf,
    "date_after": DateAfter,
    "date_after_or_equal": DateAfterOrEqual,
    "date_before": DateBefore,
    "date_before_or_equal": DateBeforeOrEqual,
}
