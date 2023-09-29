"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destination as shared_destination
from ..shared import validateerrorjson as shared_validateerrorjson
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from hightouch import utils
from typing import Optional

class ListDestinationOrderBy(str, Enum):
    r"""Order the returned destinations"""
    ID = 'id'
    NAME = 'name'
    SLUG = 'slug'
    CREATED_AT = 'createdAt'
    UPDATED_AT = 'updatedAt'



@dataclasses.dataclass
class ListDestinationRequest:
    limit: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""limit the number of objects returned (default is 100)"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Filter based on the destination's name"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""set the offset on results (for pagination)"""
    order_by: Optional[ListDestinationOrderBy] = dataclasses.field(default=ListDestinationOrderBy.ID, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""Order the returned destinations"""
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    r"""Filter based on destination's slug"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListDestination200ApplicationJSON:
    r"""Ok"""
    data: list[shared_destination.Destination] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    




@dataclasses.dataclass
class ListDestinationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    list_destination_200_application_json_object: Optional[ListDestination200ApplicationJSON] = dataclasses.field(default=None)
    r"""Ok"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    r"""Validation Failed"""
    

