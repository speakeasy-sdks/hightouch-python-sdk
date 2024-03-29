"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerRunInput:
    r"""The input of a trigger action to run syncs"""
    full_resync: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fullResync'), 'exclude': lambda f: f is None }})
    r"""Whether to resync all the rows in the query (i.e. ignoring previously
    synced rows).
    """
    reset_cdc: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resetCDC'), 'exclude': lambda f: f is None }})
    r"""Whether to sync all the rows in the query without executing changes on the destination."""
    

