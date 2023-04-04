from validation.rules.Endswith import Endswith
from validation.rules.Email import Email
from validation.rules.In import In
from validation.rules.NotIn import NotIn
from validation.rules.Startswith import Startswith
from validation.rules.Url import Url
from validation.rules.Uuid import Uuid
from validation.rules.Ulid import Ulid
from validation.rules.Gte import Gte
from validation.rules.Gt import Gt
from validation.rules.DateAfter import DateAfter
from validation.rules.DateAfterOrEqual import DateAfterOrEqual
from validation.rules.ArrayOf import ArrayOf
from validation.rules.DateBefore import DateBefore
from validation.rules.DateBeforeOrEqual import DateBeforeOrEqual
from validation.rules.Decimal import Decimal
from validation.rules.InArray import InArray
from validation.rules.Array import Array
from validation.rules.Integer import Integer
from validation.rules.Ip import Ip
from validation.rules.Ipv4 import Ipv4
from validation.rules.Ipv6 import Ipv6
from validation.rules.Json import Json
from validation.rules.Lowercase import Lowercase
from validation.rules.Lt import Lt
from validation.rules.Lte import Lte
from validation.rules.MacAddress import MacAdress
from validation.rules.Max import Max
from validation.rules.MaxDigits import MaxDigits
from validation.rules.Min import Min
from validation.rules.MinDigits import MinDigits
from validation.rules.Nullable import Nullable
from validation.rules.String import String
from validation.rules.Required import Required
from validation.rules.Numeric import Numeric
from validation.rules.Between import Between
from validation.rules.Uppercase import Uppercase

rules_to_objects_map = {
    "between": Between,
    "string": String,
    "int": Integer,
    "required": Required,
    "numeric": Numeric,
    "in_array": InArray,
    "array": Array,
    "array_of": ArrayOf,
    "date_after": DateAfter,
    "date_after_or_equal": DateAfterOrEqual,
    "date_before": DateBefore,
    "date_before_or_equal": DateBeforeOrEqual,
    "min": Min,
    "max": Max,
    "max_digits": MaxDigits,
    "min_digits": MinDigits,
    "json": Json,
    "nullable": Nullable,
    "decimal": Decimal,
    "gt": Gt,
    "gte": Gte,
    "lt": Lt,
    "lte": Lte,
    "ip": Ip,
    "ipv4": Ipv4,
    "ipv6": Ipv6,
    "lowercase": Lowercase,
    "uppercase": Uppercase,
    "mac_address": MacAdress,
    "uuid": Uuid,
    "ulid": Ulid,
    "url": Url,
    "startswith": Startswith,
    "endswith": Endswith,
    "email": Email,
    "in": In,
    "not_in": NotIn,
}
