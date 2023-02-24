from __future__ import annotations
import dataclasses
from ..shared import destination as shared_destination
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetDestinationPathParams:
    destination_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDestinationSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetDestinationRequest:
    path_params: GetDestinationPathParams = dataclasses.field()
    security: GetDestinationSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetDestinationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    destination: Optional[shared_destination.Destination] = dataclasses.field(default=None)
    