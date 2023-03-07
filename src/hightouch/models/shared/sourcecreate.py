from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCreate:
    r"""SourceCreate
    The input for creating a Source
    """
    
    configuration: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    