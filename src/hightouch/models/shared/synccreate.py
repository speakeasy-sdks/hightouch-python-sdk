"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SyncCreateSchedule:
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
class SyncCreate:
    r"""The input for creating a Sync"""
    configuration: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    r"""The sync's configuration. This specifies how data is mapped, among other
    configuration.

    The schema depends on the destination type.

    Consumers should NOT make assumptions on the contents of the
    configuration. It may change as Hightouch updates its internal code.
    """
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    r"""The id of the Destination that sync is connected to"""
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    r"""Whether the sync has been disabled by the user."""
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    r"""The id of the Model that sync is connected to"""
    schedule: SyncCreateSchedule = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    r"""The scheduling configuration. It can be triggerd based on several ways:

    Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)

    Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.

    Visual: the sync will be trigged based a visual cron configuration on UI

    DBT-cloud: the sync will be trigged based on a dbt cloud job
    """
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""The sync's slug"""
    

