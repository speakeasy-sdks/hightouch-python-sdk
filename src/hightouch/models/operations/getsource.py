from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import source as shared_source
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Optional


@dataclasses.dataclass
class GetSourceSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetSourcePathParams:
    source_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSourceRequest:
    path_params: GetSourcePathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSourceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    source: Optional[shared_source.Source] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    