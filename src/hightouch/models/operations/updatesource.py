"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import internalservererror as shared_internalservererror
from ...models.shared import source as shared_source
from ...models.shared import sourceupdate as shared_sourceupdate
from ...models.shared import validateerrorjson as shared_validateerrorjson
from typing import Optional, Union


@dataclasses.dataclass
class UpdateSourceRequest:
    source_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceId', 'style': 'simple', 'explode': False }})
    r"""The source's ID"""
    source_update: shared_sourceupdate.SourceUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateSourceResponseBody:
    r"""Ok"""
    



@dataclasses.dataclass
class UpdateSourceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    one_of: Optional[Union[shared_source.Source, shared_validateerrorjson.ValidateErrorJSON, shared_internalservererror.InternalServerError]] = dataclasses.field(default=None)
    r"""Ok"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

