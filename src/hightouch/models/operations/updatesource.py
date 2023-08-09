"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import internalservererror as shared_internalservererror
from ..shared import sourceupdate as shared_sourceupdate
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Any, Optional



@dataclasses.dataclass
class UpdateSourceSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class UpdateSourceRequest:
    source_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceId', 'style': 'simple', 'explode': False }})
    r"""The source's ID"""
    source_update: shared_sourceupdate.SourceUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateSourceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    internal_server_error: Optional[shared_internalservererror.InternalServerError] = dataclasses.field(default=None)
    r"""Something went wrong"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_source_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    r"""Ok"""
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    r"""Validation Failed"""
    

