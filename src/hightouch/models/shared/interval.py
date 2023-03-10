from __future__ import annotations
import dataclasses
from ..shared import intervalunit_enum as shared_intervalunit_enum
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Interval:
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    unit: shared_intervalunit_enum.IntervalUnitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit') }})
    