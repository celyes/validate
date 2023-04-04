from checkr.rules.Boolean import Boolean
from checkr.rules.Endswith import Endswith
from checkr.rules.Email import Email
from checkr.rules.NotInArray import NotInArray
from checkr.rules.Startswith import Startswith
from checkr.rules.Url import Url
from checkr.rules.Uuid import Uuid
from checkr.rules.Ulid import Ulid
from checkr.rules.Gte import Gte
from checkr.rules.Gt import Gt
from checkr.rules.DateAfter import DateAfter
from checkr.rules.DateAfterOrEqual import DateAfterOrEqual
from checkr.rules.ArrayOf import ArrayOf
from checkr.rules.DateBefore import DateBefore
from checkr.rules.DateBeforeOrEqual import DateBeforeOrEqual
from checkr.rules.Decimal import Decimal
from checkr.rules.InArray import InArray
from checkr.rules.Array import Array
from checkr.rules.Integer import Integer
from checkr.rules.Ip import Ip
from checkr.rules.Ipv4 import Ipv4
from checkr.rules.Ipv6 import Ipv6
from checkr.rules.Json import Json
from checkr.rules.Lowercase import Lowercase
from checkr.rules.Lt import Lt
from checkr.rules.Lte import Lte
from checkr.rules.MacAddress import MacAdress
from checkr.rules.Max import Max
from checkr.rules.MaxDigits import MaxDigits
from checkr.rules.Min import Min
from checkr.rules.MinDigits import MinDigits
from checkr.rules.Nullable import Nullable
from checkr.rules.String import String
from checkr.rules.Required import Required
from checkr.rules.Numeric import Numeric
from checkr.rules.Between import Between
from checkr.rules.Uppercase import Uppercase

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
