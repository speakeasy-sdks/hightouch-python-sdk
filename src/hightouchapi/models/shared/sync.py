import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any
from enum import Enum
from dataclasses_json import dataclass_json
from hightouchapi import utils
from ..shared import intervalschedule as shared_intervalschedule
from ..shared import cronschedule as shared_cronschedule
from ..shared import visualcronschedule as shared_visualcronschedule
from ..shared import dbtschedule as shared_dbtschedule
from ..shared import syncstatus_enum as shared_syncstatus_enum


@dataclass_json
@dataclasses.dataclass
class SyncSchedule:
    r"""SyncSchedule
    The scheduling configuration. It can be triggerd based on several ways:
    
    Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)
    
    Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.
    
    Visual: the sync will be trigged based a visual cron configuration on UI
    
    DBT-cloud: the sync will be trigged based on a dbt cloud job
    """
    
    schedule: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('schedule') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class Sync:
    r"""Sync
    Syncs define how data from models are mapped to destinations. Each time a
    sync runs, Hightouch calculates the rows that have changed since the last
    run, and syncs them to Sync's destination.
    """
    
    configuration: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('destinationId') }})
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('disabled') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    last_run_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastRunAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modelId') }})
    primary_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('primaryKey') }})
    referenced_columns: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('referencedColumns') }})
    schedule: SyncSchedule = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('schedule') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    status: shared_syncstatus_enum.SyncStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('updatedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspaceId') }})
    
