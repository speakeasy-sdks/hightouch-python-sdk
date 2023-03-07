from __future__ import annotations
from enum import Enum

class SyncRunStatusEnum(str, Enum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    QUEUED = "queued"
    SUCCESS = "success"
    WARNING = "warning"
    QUERYING = "querying"
    PROCESSING = "processing"
    REPORTING = "reporting"
    INTERRUPTED = "interrupted"
