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
    r"""SyncRunFailedRows
    The number of rows that we attempted to sync, but were rejected by the
    destination.
    
    This does not include rows that weren't attempted due to the sync being
    cancelled.
    """
    
    added_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addedCount') }})
    changed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changedCount') }})
    removed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removedCount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncRunPlannedRows:
    r"""SyncRunPlannedRows
    The number of planned rows that this sync run was supposed to execute.
    
    Note that the counts for `successfulRows` and `failedRows` may not add up
    to `plannedRows` if the sync was cancelled.
    """
    
    added_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addedCount') }})
    changed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changedCount') }})
    removed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removedCount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncRunSuccessfulRows:
    r"""SyncRunSuccessfulRows
    The number of rows that were successfully processed by the destination.
    """
    
    added_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addedCount') }})
    changed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changedCount') }})
    removed_count: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removedCount') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncRun:
    completion_ratio: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completionRatio') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    failed_rows: SyncRunFailedRows = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failedRows') }})
    finished_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finishedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    planned_rows: SyncRunPlannedRows = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plannedRows') }})
    query_size: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('querySize') }})
    started_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('startedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: shared_syncrunstatus_enum.SyncRunStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    successful_rows: SyncRunSuccessfulRows = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('successfulRows') }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    