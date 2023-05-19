"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import syncstatus as shared_syncstatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from hightouch import utils
from marshmallow import fields
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncSchedule:
    r"""The scheduling configuration. It can be triggerd based on several ways:
    
    Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)
    
    Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.
    
    Visual: the sync will be trigged based a visual cron configuration on UI
    
    DBT-cloud: the sync will be trigged based on a dbt cloud job
    """
    
    schedule: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Sync:
    r"""Syncs define how data from models are mapped to destinations. Each time a
    sync runs, Hightouch calculates the rows that have changed since the last
    run, and syncs them to Sync's destination.
    """
    
    configuration: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    r"""The sync's configuration. This specifies how data is mapped, among other
    configuration.
    
    The schema depends on the destination type.
    
    Consumers should NOT make assumptions on the contents of the
    configuration. It may change as Hightouch updates its internal code.
    """
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when the sync was created"""
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    r"""Number as a string"""
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    r"""Whether the sync has been disabled by the user."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Number as a string"""
    last_run_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastRunAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp of the last sync run"""
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    r"""Number as a string"""
    primary_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryKey') }})
    r"""The primary key that sync uses to identify data from source"""
    referenced_columns: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('referencedColumns') }})
    r"""The reference column that sync depends on to sync data from source"""
    schedule: SyncSchedule = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    r"""The scheduling configuration. It can be triggerd based on several ways:
    
    Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)
    
    Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.
    
    Visual: the sync will be trigged based a visual cron configuration on UI
    
    DBT-cloud: the sync will be trigged based on a dbt cloud job
    """
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""The sync's slug"""
    status: shared_syncstatus.SyncStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when the sync was last updated"""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    r"""Number as a string"""
    