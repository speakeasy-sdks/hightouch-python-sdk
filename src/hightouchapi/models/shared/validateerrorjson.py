import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from hightouchapi import utils
from typing import Any

class ValidateErrorJSONMessageEnum(str, Enum):
    VALIDATION_FAILED = "Validation failed"


@dataclass_json
@dataclasses.dataclass
class ValidateErrorJSON:
    details: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('details') }})
    message: ValidateErrorJSONMessageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    