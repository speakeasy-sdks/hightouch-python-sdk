import dataclasses
from dataclasses_json import dataclass_json
from hightouchapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class TriggerRunInput:
    r"""TriggerRunInput
    The input of a trigger action to run syncs
    """
    
    full_resync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fullResync') }})
    