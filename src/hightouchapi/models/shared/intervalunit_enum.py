from __future__ import annotations
import dataclasses
from enum import Enum

class IntervalUnitEnum(str, Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
