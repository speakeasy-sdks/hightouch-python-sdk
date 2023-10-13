"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import cronschedule as shared_cronschedule
from ..shared import dbtschedule as shared_dbtschedule
from ..shared import intervalschedule as shared_intervalschedule
from ..shared import syncstatus as shared_syncstatus
from ..shared import visualcronschedule as shared_visualcronschedule
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from hightouch import utils
from typing import Any, Optional, Union



@dataclasses.dataclass
class SyncScheduleSchedule:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SyncSchedule:
    r"""The scheduling configuration. It can be triggerd based on several ways:

    Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)

    Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.

    Visual: the sync will be trigged based a visual cron configuration on UI

    DBT-cloud: the sync will be trigged based on a dbt cloud job
    """
    schedule: Union[shared_intervalschedule.IntervalSchedule, shared_cronschedule.CronSchedule, shared_visualcronschedule.VisualCronSchedule, shared_dbtschedule.DBTSchedule] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
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
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The timestamp when the sync was created"""
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    r"""The id of the Destination that sync is connected to"""
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    r"""Whether the sync has been disabled by the user."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The sync's id"""
    last_run_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastRunAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The timestamp of the last sync run"""
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    r"""The id of the Model that sync is connected to"""
    primary_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryKey') }})
    r"""The primary key that sync uses to identify data from source"""
    referenced_columns: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('referencedColumns') }})
    r"""The reference column that sync depends on to sync data from source"""
    schedule: Optional[SyncSchedule] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    r"""The scheduling configuration. It can be triggerd based on several ways:

    Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)

    Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.

    Visual: the sync will be trigged based a visual cron configuration on UI

    DBT-cloud: the sync will be trigged based on a dbt cloud job
    """
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""The sync's slug"""
    status: shared_syncstatus.SyncStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""SyncStatus"""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The timestamp when the sync was last updated"""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    r"""The id of the workspace that the sync belongs to"""
    

