from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateCustom:
    r"""ModelCreateCustom
    Custom query for sources that doesn't support sql. For example, Airtable.
    """
    
    query: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateDbt:
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateRaw:
    r"""ModelCreateRaw
    Standard raw SQL query
    """
    
    sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sql') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateTable:
    r"""ModelCreateTable
    Table-based query that fetches on a table instead of SQL
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateVisual:
    r"""ModelCreateVisual
    Visual query, used by audience
    """
    
    filter: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter') }})
    parent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentId') }})
    primary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryLabel') }})
    secondary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secondaryLabel') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreate:
    r"""ModelCreate
    The input for creating a Model
    """
    
    is_schema: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSchema') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    primary_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryKey') }})
    query_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queryType') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    custom: Optional[ModelCreateCustom] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom'), 'exclude': lambda f: f is None }})
    dbt: Optional[ModelCreateDbt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt'), 'exclude': lambda f: f is None }})
    raw: Optional[ModelCreateRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    table: Optional[ModelCreateTable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table'), 'exclude': lambda f: f is None }})
    visual: Optional[ModelCreateVisual] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visual'), 'exclude': lambda f: f is None }})
    