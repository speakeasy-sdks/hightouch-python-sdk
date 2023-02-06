import dataclasses
from ..shared import model as shared_model
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetModelPathParams:
    model_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetModelSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetModelRequest:
    path_params: GetModelPathParams = dataclasses.field()
    security: GetModelSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model: Optional[shared_model.Model] = dataclasses.field(default=None)
    