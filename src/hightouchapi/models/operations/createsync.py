import dataclasses
from ..shared import internalservererror_enum as shared_internalservererror_enum
from ..shared import security as shared_security
from ..shared import synccreate as shared_synccreate
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Any, Optional


@dataclasses.dataclass
class CreateSyncSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class CreateSyncRequest:
    request: shared_synccreate.SyncCreate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: CreateSyncSecurity = dataclasses.field()
    

@dataclasses.dataclass
class CreateSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_sync_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    internal_server_error: Optional[shared_internalservererror_enum.InternalServerErrorEnum] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    