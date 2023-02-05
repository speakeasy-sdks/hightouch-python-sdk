import dataclasses
from ..shared import security as shared_security
from ..shared import sync as shared_sync
from typing import Optional


@dataclasses.dataclass
class GetSyncPathParams:
    sync_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSyncSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetSyncRequest:
    path_params: GetSyncPathParams = dataclasses.field()
    security: GetSyncSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    sync: Optional[shared_sync.Sync] = dataclasses.field(default=None)
    