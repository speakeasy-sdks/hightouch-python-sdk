import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from hightouchapi import utils


@dataclass_json
@dataclasses.dataclass
class TriggerRunCustomInput:
    r"""TriggerRunCustomInput
    The input of a trigger action to run syncs based on sync ID, slug or other filters
    """
    
    full_resync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fullResync') }})
    sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncId') }})
    sync_slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncSlug') }})
    
