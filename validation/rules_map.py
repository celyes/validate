from validation.rules.String import String
from validation.rules.Required import Required
from validation.rules.Numeric import Numeric

rules_map = {
    'string': String,
    'required': Required,
    'numeric': Numeric
}
