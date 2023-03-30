from validation.rules.String import String
from validation.rules.Required import Required
from validation.rules.Numeric import Numeric
from validation.rules.Between import Between
from validation.rules.InArray import InArray

rules_to_objects_map = {
    'string': String,
    'required': Required,
    'numeric': Numeric,
    'between': Between,
    'in_array': InArray,
}
