from __future__ import annotations
from enum import Enum

class IntervalUnitEnum(str, Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
