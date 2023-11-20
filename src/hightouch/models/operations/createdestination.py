"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import validateerrorjson as errors_validateerrorjson
from ...models.shared import destination as shared_destination
from ...models.shared import internalservererror as shared_internalservererror
from hightouch import utils
from typing import Optional, Union


@dataclasses.dataclass
class CreateDestinationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    one_of: Optional[Union[shared_destination.Destination, errors_validateerrorjson.ValidateErrorJSON, shared_internalservererror.InternalServerError]] = dataclasses.field(default=None)
    r"""Ok"""
    

