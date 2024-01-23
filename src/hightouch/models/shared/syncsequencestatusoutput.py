"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .syncrunstatus import SyncRunStatus
from .syncsequencerequeststatus import SyncSequenceRequestStatus
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncRuns:
    finished_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finishedAt') }})
    status: SyncRunStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of sync runs"""
    sync_id: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncId') }})
    sync_run_id: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncRunId') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncSequenceStatusOutput:
    r"""The status of a given sync sequence run at both a high level and the individual
    sync-run level.
    """
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    status: SyncSequenceRequestStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    sync_runs: List[SyncRuns] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncRuns') }})
    

