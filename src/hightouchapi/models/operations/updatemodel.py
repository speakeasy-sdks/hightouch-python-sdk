from __future__ import annotations
import dataclasses
from ..shared import internalservererror_enum as shared_internalservererror_enum
from ..shared import modelupdate as shared_modelupdate
from ..shared import security as shared_security
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Any, Optional


@dataclasses.dataclass
class UpdateModelPathParams:
    model_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateModelSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class UpdateModelRequest:
    path_params: UpdateModelPathParams = dataclasses.field()
    request: shared_modelupdate.ModelUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: UpdateModelSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UpdateModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    internal_server_error: Optional[shared_internalservererror_enum.InternalServerErrorEnum] = dataclasses.field(default=None)
    update_model_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    