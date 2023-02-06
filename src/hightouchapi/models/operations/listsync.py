import dataclasses
import dateutil.parser
from ..shared import security as shared_security
from ..shared import sync as shared_sync
from ..shared import validateerrorjson as shared_validateerrorjson
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from hightouchapi import utils
from marshmallow import fields
from typing import Optional

class ListSyncOrderByEnum(str, Enum):
    ID = "id"
    NAME = "name"
    SLUG = "slug"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"


@dataclasses.dataclass
class ListSyncQueryParams:
    after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    before: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before', 'style': 'form', 'explode': True }})
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    model_id: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'modelId', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order_by: Optional[ListSyncOrderByEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListSyncSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ListSyncRequest:
    query_params: ListSyncQueryParams = dataclasses.field()
    security: ListSyncSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class ListSync200ApplicationJSON:
    data: list[shared_sync.Sync] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class ListSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_sync_200_application_json_object: Optional[ListSync200ApplicationJSON] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    