from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import model as shared_model
from typing import Optional


@dataclasses.dataclass
class GetModelSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetModelPathParams:
    model_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetModelRequest:
    path_params: GetModelPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model: Optional[shared_model.Model] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    