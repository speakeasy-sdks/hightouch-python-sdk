from __future__ import annotations
import dataclasses
from ..shared import destination as shared_destination
from ..shared import security as shared_security
from ..shared import validateerrorjson as shared_validateerrorjson
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from hightouchapi import utils
from typing import Optional

class ListDestinationOrderByEnum(str, Enum):
    ID = "id"
    NAME = "name"
    SLUG = "slug"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"


@dataclasses.dataclass
class ListDestinationQueryParams:
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order_by: Optional[ListDestinationOrderByEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slug', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListDestinationSecurity:
    bearer_auth: shared_security.SchemeBearerAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ListDestinationRequest:
    query_params: ListDestinationQueryParams = dataclasses.field()
    security: ListDestinationSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListDestination200ApplicationJSON:
    data: list[shared_destination.Destination] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class ListDestinationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_destination_200_application_json_object: Optional[ListDestination200ApplicationJSON] = dataclasses.field(default=None)
    validate_error_json: Optional[shared_validateerrorjson.ValidateErrorJSON] = dataclasses.field(default=None)
    