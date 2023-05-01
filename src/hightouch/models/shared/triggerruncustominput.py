"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerRunCustomInput:
    r"""The input of a trigger action to run syncs based on sync ID, slug or other filters"""
    
    full_resync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fullResync'), 'exclude': lambda f: f is None }})
    r"""Whether to resync all the rows in the query (i.e. ignoring previously
    synced rows).
    """
    sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncId'), 'exclude': lambda f: f is None }})
    r"""Number as a string"""
    sync_slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncSlug'), 'exclude': lambda f: f is None }})
    r"""Trigger run based on sync slug"""
    