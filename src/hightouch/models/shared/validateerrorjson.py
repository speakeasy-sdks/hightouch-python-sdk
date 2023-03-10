from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from hightouch import utils
from typing import Any

class ValidateErrorJSONMessageEnum(str, Enum):
    VALIDATION_FAILED = "Validation failed"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ValidateErrorJSON:
    details: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    message: ValidateErrorJSONMessageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    