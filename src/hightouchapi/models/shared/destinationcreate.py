import dataclasses
from typing import Any
from dataclasses_json import dataclass_json
from hightouchapi import utils


@dataclass_json
@dataclasses.dataclass
class DestinationCreate:
    r"""DestinationCreate
    The input for creating a Destination
    """
    
    configuration: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
