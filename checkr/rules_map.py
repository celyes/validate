from .rules.Boolean import Boolean
from .rules.Endswith import Endswith
from .rules.Email import Email
from .rules.NotInArray import NotInArray
from .rules.Startswith import Startswith
from .rules.Url import Url
from .rules.Uuid import Uuid
from .rules.Ulid import Ulid
from .rules.Gte import Gte
from .rules.Gt import Gt
from .rules.DateAfter import DateAfter
from .rules.DateAfterOrEqual import DateAfterOrEqual
from .rules.ArrayOf import ArrayOf
from .rules.DateBefore import DateBefore
from .rules.DateBeforeOrEqual import DateBeforeOrEqual
from .rules.Decimal import Decimal
from .rules.InArray import InArray
from .rules.Array import Array
from .rules.Integer import Integer
from .rules.Ip import Ip
from .rules.Ipv4 import Ipv4
from .rules.Ipv6 import Ipv6
from .rules.Json import Json
from .rules.Lowercase import Lowercase
from .rules.Lt import Lt
from .rules.Lte import Lte
from .rules.MacAddress import MacAdress
from .rules.Max import Max
from .rules.MaxDigits import MaxDigits
from .rules.Min import Min
from .rules.MinDigits import MinDigits
from .rules.Nullable import Nullable
from .rules.String import String
from .rules.Required import Required
from .rules.Numeric import Numeric
from .rules.Between import Between
from .rules.Uppercase import Uppercase

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
    "not_in_array": NotInArray,
    "bool": Boolean,
}
