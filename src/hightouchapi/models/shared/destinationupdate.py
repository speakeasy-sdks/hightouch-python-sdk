import dataclasses
from dataclasses_json import dataclass_json
from hightouchapi import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class DestinationUpdate:
    r"""DestinationUpdate
    The input for updating a Destination
    """
    
    configuration: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    