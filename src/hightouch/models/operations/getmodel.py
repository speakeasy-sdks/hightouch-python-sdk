"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import model as shared_model
from typing import Optional



@dataclasses.dataclass
class GetModelSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class GetModelRequest:
    model_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    r"""The id of the model"""
    




@dataclasses.dataclass
class GetModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model: Optional[shared_model.Model] = dataclasses.field(default=None)
    r"""Ok"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

