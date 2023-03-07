from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerRunInput:
    r"""TriggerRunInput
    The input of a trigger action to run syncs
    """
    
    full_resync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fullResync'), 'exclude': lambda f: f is None }})
    