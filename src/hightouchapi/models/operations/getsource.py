import dataclasses
from ..shared import security as shared_security
from ..shared import source as shared_source
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Optional


@dataclasses.dataclass
class GetSourcePathParams:
    source_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSourceSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetSourceRequest:
    path_params: GetSourcePathParams = dataclasses.field()
    security: GetSourceSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetSourceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source: Optional[shared_source.Source] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    