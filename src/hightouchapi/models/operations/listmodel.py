import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from hightouchapi import utils
from ..shared import security as shared_security
from ..shared import model as shared_model
from ..shared import validateerrorjson as shared_validateerrorjson

class ListModelOrderByEnum(str, Enum):
    ID = "id"
    NAME = "name"
    SLUG = "slug"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"


@dataclasses.dataclass
class ListModelQueryParams:
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order_by: Optional[ListModelOrderByEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListModelSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclass_json
@dataclasses.dataclass
class ListModel200ApplicationJSON:
    data: list[shared_model.Model] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class ListModelRequest:
    query_params: ListModelQueryParams = dataclasses.field()
    security: ListModelSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ListModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_model_200_application_json_object: Optional[ListModel200ApplicationJSON] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    
