from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destinationupdate as shared_destinationupdate
from ..shared import internalservererror_enum as shared_internalservererror_enum
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Any, Optional


@dataclasses.dataclass
class UpdateDestinationSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class UpdateDestinationRequest:
    destination_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})
    destination_update: shared_destinationupdate.DestinationUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateDestinationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    internal_server_error: Optional[shared_internalservererror_enum.InternalServerErrorEnum] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_destination_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    