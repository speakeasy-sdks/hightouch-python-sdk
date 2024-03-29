"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import source as shared_source
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from hightouch import utils
from typing import List, Optional

class ListSourceQueryParamOrderBy(str, Enum):
    r"""specify the order"""
    ID = 'id'
    NAME = 'name'
    SLUG = 'slug'
    CREATED_AT = 'createdAt'
    UPDATED_AT = 'updatedAt'


@dataclasses.dataclass
class ListSourceRequest:
    limit: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""limit the number of objects returned (default is 100)"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""filter based on name"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""set the offset on results (for pagination)"""
    order_by: Optional[ListSourceQueryParamOrderBy] = dataclasses.field(default=ListSourceQueryParamOrderBy.ID, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""specify the order"""
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    r"""filter based on slug"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListSourceResponseBody:
    r"""Ok"""
    data: List[shared_source.Source] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    



@dataclasses.dataclass
class ListSourceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[ListSourceResponseBody] = dataclasses.field(default=None)
    r"""Ok"""
    

