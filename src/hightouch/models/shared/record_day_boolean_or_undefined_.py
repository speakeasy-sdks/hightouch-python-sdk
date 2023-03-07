from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RecordDayBooleanOrUndefined:
    r"""RecordDayBooleanOrUndefined
    Construct a type with a set of properties K of type T
    """
    
    friday: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('friday'), 'exclude': lambda f: f is None }})
    monday: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monday'), 'exclude': lambda f: f is None }})
    saturday: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('saturday'), 'exclude': lambda f: f is None }})
    sunday: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sunday'), 'exclude': lambda f: f is None }})
    thursday: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('thursday'), 'exclude': lambda f: f is None }})
    tuesday: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tuesday'), 'exclude': lambda f: f is None }})
    wednesday: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wednesday'), 'exclude': lambda f: f is None }})
    