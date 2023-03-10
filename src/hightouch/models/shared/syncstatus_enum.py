from __future__ import annotations
from enum import Enum

class SyncStatusEnum(str, Enum):
    DISABLED = "disabled"
    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"
    QUEUED = "queued"
    SUCCESS = "success"
    WARNING = "warning"
    QUERYING = "querying"
    PROCESSING = "processing"
    REPORTING = "reporting"
    INTERRUPTED = "interrupted"
