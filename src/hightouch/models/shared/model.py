"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from hightouch import utils
from marshmallow import fields
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCustom:
    r"""Custom query for sources that doesn't support sql. For example, Airtable."""
    
    query: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelDbt:
    r"""Query that is based on a dbt model"""
    
    compiled_sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compiledSql') }})
    r"""Compiled SQL in the dbt model"""  
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database containing the generated table"""  
    dbt_unique_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbtUniqueId') }})
    r"""Unique ID of the model assigned by dbt (usually some combination of the schema and table name)"""  
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    r"""Number as a string"""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the table generated by the dbt model"""  
    raw_sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rawSql') }})
    r"""Raw SQL in the dbt model"""  
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    r"""Name of the schema containing the generated table"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelRaw:
    r"""Standard raw SQL query"""
    
    sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sql') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelTable:
    r"""Table-based query that fetches on a table instead of SQL"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelVisual:
    r"""Visual query, used by audience"""
    
    filter: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter') }})  
    parent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentId') }})
    r"""Number as a string"""  
    primary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryLabel') }})  
    secondary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secondaryLabel') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Model:
    r"""The SQL query that pulls data from your source to send to your destination.
    We send your SQL query directly to your source so any SQL that is valid for your source (including functions) is valid in Hightouch.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when model was created"""  
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Number as a string"""  
    is_schema: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSchema') }})
    r"""If is_schema is true, the model is just used to build other models.
    Either as part of visual querying, or as the root of a visual query.
    """  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the model"""  
    primary_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryKey') }})
    r"""The primary key will be null if the query doesn't get directly synced (e.g. a relationship table for visual querying)"""  
    query_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queryType') }})
    r"""The type of the query. Available options: custom, raw_sql, tabel, dbt and visual."""  
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""The slug of the model"""  
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    r"""Number as a string"""  
    syncs: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncs') }})
    r"""The list of id of syncs that uses this model"""  
    tags: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags') }})
    r"""The tags of the model"""  
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The timestamp when model was lastly updated"""  
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    r"""Number as a string"""  
    custom: Optional[ModelCustom] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom'), 'exclude': lambda f: f is None }})
    r"""Custom query for sources that doesn't support sql. For example, Airtable."""  
    dbt: Optional[ModelDbt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt'), 'exclude': lambda f: f is None }})
    r"""Query that is based on a dbt model"""  
    raw: Optional[ModelRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    r"""Standard raw SQL query"""  
    table: Optional[ModelTable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table'), 'exclude': lambda f: f is None }})
    r"""Table-based query that fetches on a table instead of SQL"""  
    visual: Optional[ModelVisual] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visual'), 'exclude': lambda f: f is None }})
    r"""Visual query, used by audience"""  
    