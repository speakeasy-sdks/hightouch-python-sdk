"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateCustom:
    r"""Custom query for sources that doesn't support sql. For example, Airtable."""
    
    query: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateDbt:
    
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})

    r"""Number as a string"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateRaw:
    r"""Standard raw SQL query"""
    
    sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sql') }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateTable:
    r"""Table-based query that fetches on a table instead of SQL"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreateVisual:
    r"""Visual query, used by audience"""
    
    filter: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter') }})

    parent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentId') }})

    r"""Number as a string"""
    primary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryLabel') }})

    secondary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secondaryLabel') }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelCreate:
    r"""The input for creating a Model"""
    
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
    custom: Optional[ModelCreateCustom] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom'), 'exclude': lambda f: f is None }})

    r"""Custom query for sources that doesn't support sql. For example, Airtable."""
    dbt: Optional[ModelCreateDbt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt'), 'exclude': lambda f: f is None }})

    raw: Optional[ModelCreateRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})

    r"""Standard raw SQL query"""
    table: Optional[ModelCreateTable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table'), 'exclude': lambda f: f is None }})

    r"""Table-based query that fetches on a table instead of SQL"""
    visual: Optional[ModelCreateVisual] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visual'), 'exclude': lambda f: f is None }})

    r"""Visual query, used by audience"""
    