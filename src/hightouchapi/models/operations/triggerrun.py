from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import triggerruninput as shared_triggerruninput
from ..shared import triggerrunoutput as shared_triggerrunoutput
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Optional


@dataclasses.dataclass
class TriggerRunPathParams:
    sync_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TriggerRunSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class TriggerRunRequest:
    path_params: TriggerRunPathParams = dataclasses.field()
    security: TriggerRunSecurity = dataclasses.field()
    request: Optional[shared_triggerruninput.TriggerRunInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TriggerRunResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    trigger_run_output: Optional[shared_triggerrunoutput.TriggerRunOutput] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    