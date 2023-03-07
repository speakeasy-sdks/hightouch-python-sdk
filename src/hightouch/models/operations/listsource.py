from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import source as shared_source
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from hightouch import utils
from typing import Optional


@dataclasses.dataclass
class ListSourceSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    
class ListSourceOrderByEnum(str, Enum):
    ID = "id"
    NAME = "name"
    SLUG = "slug"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"


@dataclasses.dataclass
class ListSourceQueryParams:
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order_by: Optional[ListSourceOrderByEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListSourceRequest:
    query_params: ListSourceQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListSource200ApplicationJSON:
    data: list[shared_source.Source] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

@dataclasses.dataclass
class ListSourceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_source_200_application_json_object: Optional[ListSource200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    