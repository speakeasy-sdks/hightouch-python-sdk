from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DBTScheduleAccount:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DBTScheduleJob:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DBTSchedule:
    account: DBTScheduleAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account') }})
    dbt_credential_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbtCredentialId') }})
    job: DBTScheduleJob = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job') }})
    