from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateCustom:
    r"""ModelUpdateCustom
    Custom query for sources that doesn't support sql. For example, Airtable.
    """
    
    query: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateDbt:
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateRaw:
    r"""ModelUpdateRaw
    Standard raw SQL query
    """
    
    sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sql') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateTable:
    r"""ModelUpdateTable
    Table-based query that fetches on a table instead of SQL
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateVisual:
    r"""ModelUpdateVisual
    Visual query, used by audience
    """
    
    filter: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter') }})
    parent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentId') }})
    primary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryLabel') }})
    secondary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secondaryLabel') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdate:
    r"""ModelUpdate
    The input for updating a Model
    """
    
    custom: Optional[ModelUpdateCustom] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom'), 'exclude': lambda f: f is None }})
    dbt: Optional[ModelUpdateDbt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt'), 'exclude': lambda f: f is None }})
    is_schema: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSchema'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryKey'), 'exclude': lambda f: f is None }})
    raw: Optional[ModelUpdateRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    table: Optional[ModelUpdateTable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table'), 'exclude': lambda f: f is None }})
    visual: Optional[ModelUpdateVisual] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visual'), 'exclude': lambda f: f is None }})
    