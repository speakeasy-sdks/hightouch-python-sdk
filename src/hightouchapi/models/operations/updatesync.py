import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from enum import Enum
from ..shared import security as shared_security
from ..shared import syncupdate as shared_syncupdate
from ..shared import internalservererror_enum as shared_internalservererror_enum
from ..shared import sync as shared_sync
from ..shared import validateerrorjson as shared_validateerrorjson


@dataclasses.dataclass
class UpdateSyncPathParams:
    sync_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateSyncSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class UpdateSyncRequest:
    path_params: UpdateSyncPathParams = dataclasses.field()
    request: shared_syncupdate.SyncUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: UpdateSyncSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UpdateSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    internal_server_error: Optional[shared_internalservererror_enum.InternalServerErrorEnum] = dataclasses.field(default=None)
    update_sync_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    
