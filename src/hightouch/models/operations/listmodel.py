"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import model as shared_model
from ..shared import validateerrorjson as shared_validateerrorjson
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from hightouch import utils
from typing import Optional


@dataclasses.dataclass
class ListModelSecurity:
    
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})  
    
class ListModelOrderByEnum(str, Enum):
    r"""specify the order"""
    ID = "id"
    NAME = "name"
    SLUG = "slug"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"


@dataclasses.dataclass
class ListModelRequest:
    
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""limit the number of objects returned (default is 100)"""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""filter based on name"""  
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""set the offset on results (for pagination)"""  
    order_by: Optional[ListModelOrderByEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""specify the order"""  
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    r"""filter based on slug"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListModel200ApplicationJSON:
    r"""Ok"""
    
    data: list[shared_model.Model] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})  
    

@dataclasses.dataclass
class ListModelResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    list_model_200_application_json_object: Optional[ListModel200ApplicationJSON] = dataclasses.field(default=None)
    r"""Ok"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    r"""Validation Failed"""  
    