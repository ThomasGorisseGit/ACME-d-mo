from enum import IntEnum, Enum
from typing import Any, Dict, TypeAlias

JSON: TypeAlias = Dict[str, Any]
class Operation(IntEnum):
    CREATE = 1
    RETRIEVE = 2
    UPDATE = 3
    DELETE = 4
    NOTIFY = 5
    
class ResourceTypes(IntEnum):
    ACP = 1
    AE = 2
    CNT = 3
    CIN = 4
    SUB = 23
    
class HTTPMethods(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'