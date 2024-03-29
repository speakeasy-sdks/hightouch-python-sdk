"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerSequenceRunOutput:
    r"""The output of a trigger action to run sync sequences"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The id of the triggered sync sequence run."""
    

