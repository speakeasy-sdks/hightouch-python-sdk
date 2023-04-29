"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import syncrunstatus_enum as shared_syncrunstatus_enum
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from hightouch import utils
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncRunFailedRows:
    r"""The number of rows that we attempted to sync, but were rejected by the
    destination.
    
    This does not include rows that weren't attempted due to the sync being
    cancelled.
    """
    
    added_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addedCount') }})
    r"""The number of failed adds."""
    changed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changedCount') }})
    r"""The number of failed changes."""
    removed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removedCount') }})
    r"""The number of failed removes."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncRunPlannedRows:
    r"""The number of planned rows that this sync run was supposed to execute.
    
    Note that the counts for `successfulRows` and `failedRows` may not add up
    to `plannedRows` if the sync was cancelled.
    """
    
    added_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addedCount') }})
    r"""The number of added rows."""
    changed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changedCount') }})
    r"""The number of changed rows."""
    removed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removedCount') }})
    r"""The number of removed rows."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncRunSuccessfulRows:
    r"""The number of rows that were successfully processed by the destination."""
    
    added_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addedCount') }})
    r"""The number of successful adds."""
    changed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changedCount') }})
    r"""The number of successful changes."""
    removed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removedCount') }})
    r"""The number of successful removes."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncRun:
    
    completion_ratio: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completionRatio') }})
    r"""The completion ratio of sync run, showing the progress of a sync run"""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when sync run was created. In most cases this will be
    equivalent to `startedAt`, but it may be earlier if the sync was triggered
    while a run was already in progress, and the new run didn't start for
    a while.
    """
    failed_rows: SyncRunFailedRows = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failedRows') }})
    r"""The number of rows that we attempted to sync, but were rejected by the
    destination.
    
    This does not include rows that weren't attempted due to the sync being
    cancelled.
    """
    finished_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finishedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when the sync run finished"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Number as a string"""
    planned_rows: SyncRunPlannedRows = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plannedRows') }})
    r"""The number of planned rows that this sync run was supposed to execute.
    
    Note that the counts for `successfulRows` and `failedRows` may not add up
    to `plannedRows` if the sync was cancelled.
    """
    query_size: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('querySize') }})
    r"""The number of rows in the query."""
    started_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('startedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when the sync run started"""
    status: shared_syncrunstatus_enum.SyncRunStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of sync runs"""
    successful_rows: SyncRunSuccessfulRows = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('successfulRows') }})
    r"""The number of rows that were successfully processed by the destination."""
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    r"""Error message if the sync run didn't finish successfully"""
    