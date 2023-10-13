"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import internalservererror as shared_internalservererror
from ..shared import sync as shared_sync
from ..shared import syncupdate as shared_syncupdate
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Optional, Union



@dataclasses.dataclass
class UpdateSyncRequest:
    sync_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    r"""The sync's ID"""
    sync_update: shared_syncupdate.SyncUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateSync200ApplicationJSON:
    r"""Ok"""
    




@dataclasses.dataclass
class UpdateSyncResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    internal_server_error: Optional[shared_internalservererror.InternalServerError] = dataclasses.field(default=None)
    r"""Something went wrong"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_sync_200_application_json_one_of: Optional[Union[shared_sync.Sync, shared_validateerrorjson.ValidateErrorJSON, shared_internalservererror.InternalServerError]] = dataclasses.field(default=None)
    r"""Ok"""
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    r"""Validation Failed"""
    

