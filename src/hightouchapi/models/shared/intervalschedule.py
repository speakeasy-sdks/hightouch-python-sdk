from __future__ import annotations
import dataclasses
from ..shared import interval as shared_interval
from dataclasses_json import Undefined, dataclass_json
from hightouchapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IntervalSchedule:
    interval: shared_interval.Interval = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('interval') }})
    