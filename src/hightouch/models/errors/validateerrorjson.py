"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from hightouch import utils
from typing import Any, Dict

class Message(str, Enum):
    VALIDATION_FAILED = 'Validation failed'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ValidateErrorJSON(Exception):
    details: Dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    message: Message = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
