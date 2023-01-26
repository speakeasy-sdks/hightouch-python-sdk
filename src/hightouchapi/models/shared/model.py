import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from hightouchapi import utils


@dataclass_json
@dataclasses.dataclass
class ModelCustom:
    r"""ModelCustom
    Custom query for sources that doesn't support sql. For example, Airtable.
    """
    
    query: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('query') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelDbt:
    r"""ModelDbt
    Query that is based on a dbt model
    """
    
    compiled_sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('compiledSql') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('database') }})
    dbt_unique_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dbtUniqueId') }})
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modelId') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    raw_sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('rawSql') }})
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('schema') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelRaw:
    r"""ModelRaw
    Standard raw SQL query
    """
    
    sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sql') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelTable:
    r"""ModelTable
    Table-based query that fetches on a table instead of SQL
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ModelVisual:
    r"""ModelVisual
    Visual query, used by audience
    """
    
    filter: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('filter') }})
    parent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('parentId') }})
    primary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('primaryLabel') }})
    secondary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('secondaryLabel') }})
    

@dataclass_json
@dataclasses.dataclass
class Model:
    r"""Model
    The SQL query that pulls data from your source to send to your destination.
    We send your SQL query directly to your source so any SQL that is valid for your source (including functions) is valid in Hightouch.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_schema: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('isSchema') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    primary_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('primaryKey') }})
    query_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('queryType') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    syncs: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncs') }})
    tags: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('updatedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspaceId') }})
    custom: Optional[ModelCustom] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('custom') }})
    dbt: Optional[ModelDbt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dbt') }})
    raw: Optional[ModelRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('raw') }})
    table: Optional[ModelTable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table') }})
    visual: Optional[ModelVisual] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('visual') }})
    
