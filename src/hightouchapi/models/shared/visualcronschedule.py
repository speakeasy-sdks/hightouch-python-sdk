import dataclasses
from dataclasses_json import dataclass_json
from hightouchapi import utils
from ..shared import record_day_boolean_or_undefined_ as shared_record_day_boolean_or_undefined_


@dataclass_json
@dataclasses.dataclass
class VisualCronScheduleExpressions:
    days: shared_record_day_boolean_or_undefined_.RecordDayBooleanOrUndefined = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('days') }})
    time: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('time') }})
    

@dataclass_json
@dataclasses.dataclass
class VisualCronSchedule:
    expressions: list[VisualCronScheduleExpressions] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('expressions') }})
    
