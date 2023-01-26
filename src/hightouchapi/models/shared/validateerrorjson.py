import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any
from enum import Enum
from dataclasses_json import dataclass_json
from hightouchapi import utils

class ValidateErrorJSONMessageEnum(str, Enum):
    VALIDATION_FAILED = "Validation failed"


@dataclass_json
@dataclasses.dataclass
class ValidateErrorJSON:
    details: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    message: ValidateErrorJSONMessageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    
