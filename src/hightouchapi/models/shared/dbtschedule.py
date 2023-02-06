import dataclasses
from dataclasses_json import dataclass_json
from hightouchapi import utils


@dataclass_json
@dataclasses.dataclass
class DBTScheduleAccount:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class DBTScheduleJob:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class DBTSchedule:
    account: DBTScheduleAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('account') }})
    dbt_credential_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dbtCredentialId') }})
    job: DBTScheduleJob = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('job') }})
    