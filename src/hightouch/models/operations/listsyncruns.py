from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import syncrun as shared_syncrun
from ..shared import validateerrorjson as shared_validateerrorjson
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from hightouch import utils
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class ListSyncRunsSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class ListSyncRunsPathParams:
    sync_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    
class ListSyncRunsOrderByEnum(str, Enum):
    ID = "id"
    CREATED_AT = "createdAt"
    STARTED_AT = "startedAt"
    FINISHED_AT = "finishedAt"


@dataclasses.dataclass
class ListSyncRunsQueryParams:
    after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    before: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before', 'style': 'form', 'explode': True }})
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order_by: Optional[ListSyncRunsOrderByEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    run_id: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'runId', 'style': 'form', 'explode': True }})
    within: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'within', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListSyncRunsRequest:
    path_params: ListSyncRunsPathParams = dataclasses.field()
    query_params: ListSyncRunsQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListSyncRuns200ApplicationJSON:
    data: list[shared_syncrun.SyncRun] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

@dataclasses.dataclass
class ListSyncRunsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_sync_runs_200_application_json_object: Optional[ListSyncRuns200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    