"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import sync as shared_sync
from typing import Optional



@dataclasses.dataclass
class GetSyncSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class GetSyncRequest:
    sync_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    r"""The id of the sync"""
    




@dataclasses.dataclass
class GetSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    sync: Optional[shared_sync.Sync] = dataclasses.field(default=None)
    r"""Ok"""
    

