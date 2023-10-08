"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import internalservererror as shared_internalservererror
from typing import Any, Optional



@dataclasses.dataclass
class CreateSourceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_source_200_application_json_one_of: Optional[Any] = dataclasses.field(default=None)
    r"""Ok"""
    internal_server_error: Optional[shared_internalservererror.InternalServerError] = dataclasses.field(default=None)
    r"""Something went wrong"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    validate_error_json: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""Conflict"""
    

