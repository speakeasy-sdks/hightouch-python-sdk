from __future__ import annotations
import dataclasses
from ..shared import record_day_boolean_or_undefined_ as shared_record_day_boolean_or_undefined_
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class VisualCronScheduleExpressions:
    days: shared_record_day_boolean_or_undefined_.RecordDayBooleanOrUndefined = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days') }})
    time: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class VisualCronSchedule:
    expressions: list[VisualCronScheduleExpressions] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expressions') }})
    