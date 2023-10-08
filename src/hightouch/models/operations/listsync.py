"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from hightouch import utils
from typing import Any, Optional

class ListSyncOrderBy(str, Enum):
    r"""specify the order"""
    ID = 'id'
    NAME = 'name'
    SLUG = 'slug'
    CREATED_AT = 'createdAt'
    UPDATED_AT = 'updatedAt'



@dataclasses.dataclass
class ListSyncRequest:
    after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    r"""select syncs that were run after given ISO timestamp"""
    before: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before', 'style': 'form', 'explode': True }})
    r"""select syncs that were run before given ISO timestamp"""
    limit: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""limit the number of objects returned (default is 100)"""
    model_id: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'modelId', 'style': 'form', 'explode': True }})
    r"""filter based on modelId"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""set the offset on results (for pagination)"""
    order_by: Optional[ListSyncOrderBy] = dataclasses.field(default=ListSyncOrderBy.ID, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""specify the order"""
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    r"""filter based on slug"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListSync200ApplicationJSON:
    r"""Ok"""
    data: list[dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasMore') }})
    




@dataclasses.dataclass
class ListSyncResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    list_sync_200_application_json_object: Optional[ListSync200ApplicationJSON] = dataclasses.field(default=None)
    r"""Ok"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    validate_error_json: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""Validation Failed"""
    

