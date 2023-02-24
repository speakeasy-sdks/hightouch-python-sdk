from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouchapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerRunOutput:
    r"""TriggerRunOutput
    The output of a trigger action to run syncs
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    