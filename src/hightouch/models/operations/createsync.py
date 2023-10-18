"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import internalservererror as shared_internalservererror
from ..shared import sync as shared_sync
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Optional, Union


@dataclasses.dataclass
class CreateSync200ApplicationJSON:
    r"""Ok"""
    



@dataclasses.dataclass
class CreateSyncResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_sync_200_application_json_one_of: Optional[Union[shared_sync.Sync, shared_validateerrorjson.ValidateErrorJSON, shared_internalservererror.InternalServerError]] = dataclasses.field(default=None)
    r"""Ok"""
    internal_server_error: Optional[shared_internalservererror.InternalServerError] = dataclasses.field(default=None)
    r"""Something went wrong"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    r"""Conflict"""
    

