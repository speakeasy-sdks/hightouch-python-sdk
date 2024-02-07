"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import validateerrorjson as errors_validateerrorjson
from ...models.shared import internalservererror as shared_internalservererror
from ...models.shared import source as shared_source
from ...models.shared import sourceupdate as shared_sourceupdate
from typing import Optional, Union


@dataclasses.dataclass
class UpdateSourceRequest:
    source_update: shared_sourceupdate.SourceUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    source_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceId', 'style': 'simple', 'explode': False }})
    r"""The source's ID"""
    



@dataclasses.dataclass
class UpdateSourceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    one_of: Optional[Union[shared_source.Source, errors_validateerrorjson.ValidateErrorJSON, shared_internalservererror.InternalServerError]] = dataclasses.field(default=None)
    r"""Ok"""
    

