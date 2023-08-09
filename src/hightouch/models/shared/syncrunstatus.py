"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class SyncRunStatus(str, Enum):
    r"""The status of sync runs"""
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    QUEUED = 'queued'
    SUCCESS = 'success'
    WARNING = 'warning'
    QUERYING = 'querying'
    PROCESSING = 'processing'
    REPORTING = 'reporting'
    INTERRUPTED = 'interrupted'