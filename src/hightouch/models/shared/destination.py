"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from hightouch import utils
from marshmallow import fields
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Destination:
    r"""The service receiving your data (e.g. Salesforce, Hubspot, Customer.io, or a
    SFTP server)
    """
    configuration: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    r"""The destination's configuration. This specifies general metadata about destination, like hostname and username.
    Hightouch will be using this configuration to connect to destination.

    The schema depends on the destination type.

    Consumers should NOT make assumptions on the contents of the
    configuration. It may change as Hightouch updates its internal code.
    """
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when the destination was created"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The destination's id"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The destination's name"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""The destination's slug"""
    syncs: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncs') }})
    r"""A list of syncs that sync to this destination."""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The destination's type (e.g. salesforce or hubspot)."""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when the destination was last updated"""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    r"""The id of the workspace that the destination belongs to"""
    

