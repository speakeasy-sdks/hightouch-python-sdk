import dataclasses
from dataclasses_json import dataclass_json
from hightouchapi import utils


@dataclass_json
@dataclasses.dataclass
class DbtScheduleAccount:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class DbtScheduleJob:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class DbtSchedule:
    account: DbtScheduleAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('account') }})
    dbt_credential_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dbtCredentialId') }})
    job: DbtScheduleJob = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('job') }})
    
