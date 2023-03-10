from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncUpdateSchedule:
    r"""SyncUpdateSchedule
    The scheduling configuration. It can be triggerd based on several ways:
    
    Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)
    
    Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.
    
    Visual: the sync will be trigged based a visual cron configuration on UI
    
    DBT-cloud: the sync will be trigged based on a dbt cloud job
    """
    
    schedule: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncUpdate:
    r"""SyncUpdate
    The input for updating a Sync
    """
    
    configuration: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration'), 'exclude': lambda f: f is None }})
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    schedule: Optional[SyncUpdateSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    