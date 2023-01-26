import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from enum import Enum
from ..shared import security as shared_security
from ..shared import sourceupdate as shared_sourceupdate
from ..shared import internalservererror_enum as shared_internalservererror_enum
from ..shared import source as shared_source
from ..shared import validateerrorjson as shared_validateerrorjson


@dataclasses.dataclass
class UpdateSourcePathParams:
    source_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateSourceSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class UpdateSourceRequest:
    path_params: UpdateSourcePathParams = dataclasses.field()
    request: shared_sourceupdate.SourceUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: UpdateSourceSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UpdateSourceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    internal_server_error: Optional[shared_internalservererror_enum.InternalServerErrorEnum] = dataclasses.field(default=None)
    update_source_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    
