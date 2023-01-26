import dataclasses
from dataclasses_json import dataclass_json
from hightouchapi import utils


@dataclass_json
@dataclasses.dataclass
class CronSchedule:
    expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('expression') }})
    
