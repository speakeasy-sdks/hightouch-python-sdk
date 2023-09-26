"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Any, Optional



@dataclasses.dataclass
class TriggerRunCustomResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    trigger_run_custom_200_application_json_one_of: Optional[Any] = dataclasses.field(default=None)
    r"""Ok"""
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    r"""Validation Failed"""
    

