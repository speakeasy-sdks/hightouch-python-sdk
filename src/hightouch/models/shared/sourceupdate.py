from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceUpdate:
    r"""SourceUpdate
    The input for updating a Source
    """
    
    configuration: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    