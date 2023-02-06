import dataclasses
from ..shared import security as shared_security
from ..shared import triggerruncustominput as shared_triggerruncustominput
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Any, Optional


@dataclasses.dataclass
class TriggerRunCustomSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class TriggerRunCustomRequest:
    request: shared_triggerruncustominput.TriggerRunCustomInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: TriggerRunCustomSecurity = dataclasses.field()
    

@dataclasses.dataclass
class TriggerRunCustomResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    trigger_run_custom_200_application_json_any_of: Optional[Any] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    