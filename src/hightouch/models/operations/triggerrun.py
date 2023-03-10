from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import triggerruninput as shared_triggerruninput
from ..shared import triggerrunoutput as shared_triggerrunoutput
from ..shared import validateerrorjson as shared_validateerrorjson
from typing import Optional


@dataclasses.dataclass
class TriggerRunSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class TriggerRunPathParams:
    sync_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TriggerRunRequest:
    path_params: TriggerRunPathParams = dataclasses.field()
    request: Optional[shared_triggerruninput.TriggerRunInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TriggerRunResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    trigger_run_output: Optional[shared_triggerrunoutput.TriggerRunOutput] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    