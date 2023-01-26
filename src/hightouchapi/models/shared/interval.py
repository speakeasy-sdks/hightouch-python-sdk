import dataclasses
from enum import Enum
from dataclasses_json import dataclass_json
from hightouchapi import utils
from ..shared import intervalunit_enum as shared_intervalunit_enum


@dataclass_json
@dataclasses.dataclass
class Interval:
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity') }})
    unit: shared_intervalunit_enum.IntervalUnitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('unit') }})
    
