"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import model as shared_model
from typing import Optional


@dataclasses.dataclass
class GetModelRequest:
    model_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    r"""The id of the model"""
    



@dataclasses.dataclass
class GetModelResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    model: Optional[shared_model.Model] = dataclasses.field(default=None)
    r"""Ok"""
    

