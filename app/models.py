from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


# Persistent model for storing counter value
class Counter(SQLModel, table=True):
    __tablename__ = "counters"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    value: int = Field(default=0)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Non-persistent schema for counter updates
class CounterUpdate(SQLModel, table=False):
    value: int
