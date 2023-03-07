from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destination as shared_destination
from typing import Optional


@dataclasses.dataclass
class GetDestinationSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetDestinationPathParams:
    destination_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDestinationRequest:
    path_params: GetDestinationPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetDestinationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    destination: Optional[shared_destination.Destination] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    