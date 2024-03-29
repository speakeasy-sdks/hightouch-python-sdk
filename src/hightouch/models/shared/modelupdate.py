"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from hightouch import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateCustom:
    r"""Custom query for sources that doesn't support sql. For example, Airtable."""
    query: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateDbt:
    model_id: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    r"""Model id that refers to a dbt model"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateRaw:
    r"""Standard raw SQL query"""
    sql: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sql') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateTable:
    r"""Table-based query that fetches on a table instead of SQL"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdateVisual:
    r"""Visual query, used by audience"""
    filter_: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter') }})
    parent_id: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentId') }})
    r"""Parent id of the schema that visual query is based on"""
    primary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryLabel') }})
    secondary_label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secondaryLabel') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelUpdate:
    r"""The input for updating a Model"""
    custom: Optional[ModelUpdateCustom] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom'), 'exclude': lambda f: f is None }})
    r"""Custom query for sources that doesn't support sql. For example, Airtable."""
    dbt: Optional[ModelUpdateDbt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt'), 'exclude': lambda f: f is None }})
    folder_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folderId'), 'exclude': lambda f: f is None }})
    is_schema: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSchema'), 'exclude': lambda f: f is None }})
    r"""If is_schema is true, the model is just used to build other models.
    Either as part of visual querying, or as the root of a visual query.
    """
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the model"""
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryKey'), 'exclude': lambda f: f is None }})
    r"""The primary key will be null if the query doesn't get directly synced (e.g. a relationship table for visual querying)"""
    raw: Optional[ModelUpdateRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    r"""Standard raw SQL query"""
    table: Optional[ModelUpdateTable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table'), 'exclude': lambda f: f is None }})
    r"""Table-based query that fetches on a table instead of SQL"""
    visual: Optional[ModelUpdateVisual] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visual'), 'exclude': lambda f: f is None }})
    r"""Visual query, used by audience"""
    

