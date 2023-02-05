import dataclasses
from dataclasses_json import dataclass_json
from hightouchapi import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class ModelUpdateCustom:
    r"""ModelUpdateCustom
    Custom query for sources that doesn't support sql. For example, Airtable.
    """
    
    query: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('query') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelUpdateDbt:
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modelId') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelUpdateRaw:
    r"""ModelUpdateRaw
    Standard raw SQL query
    """
    
    sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sql') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelUpdateTable:
    r"""ModelUpdateTable
    Table-based query that fetches on a table instead of SQL
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelUpdateVisual:
    r"""ModelUpdateVisual
    Visual query, used by audience
    """
    
    filter: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('filter') }})
    parent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('parentId') }})
    primary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('primaryLabel') }})
    secondary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('secondaryLabel') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelUpdate:
    r"""ModelUpdate
    The input for updating a Model
    """
    
    custom: Optional[ModelUpdateCustom] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('custom') }})
    dbt: Optional[ModelUpdateDbt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dbt') }})
    is_schema: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isSchema') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('primaryKey') }})
    raw: Optional[ModelUpdateRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('raw') }})
    table: Optional[ModelUpdateTable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table') }})
    visual: Optional[ModelUpdateVisual] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('visual') }})
    