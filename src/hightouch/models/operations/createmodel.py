from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import internalservererror_enum as shared_internalservererror_enum
from ..shared import modelcreate as shared_modelcreate
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Any, Optional


@dataclasses.dataclass
class CreateModelSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class CreateModelRequest:
    request: shared_modelcreate.ModelCreate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_model_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    internal_server_error: Optional[shared_internalservererror_enum.InternalServerErrorEnum] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    