from datetime import datetime
from sqlmodel import select
from app.database import get_session
from app.models import Counter


def get_counter_value() -> int:
    """Get the current counter value from the database."""
    with get_session() as session:
        counter = session.exec(select(Counter)).first()
        if counter is None:
            # Initialize counter if it doesn't exist
            counter = Counter(value=0)
            session.add(counter)
            session.commit()
            session.refresh(counter)
        return counter.value


def increment_counter() -> int:
    """Increment the counter value and return the new value."""
    with get_session() as session:
        counter = session.exec(select(Counter)).first()
        if counter is None:
            # Initialize counter if it doesn't exist
            counter = Counter(value=1, updated_at=datetime.utcnow())
            session.add(counter)
        else:
            counter.value += 1
            counter.updated_at = datetime.utcnow()
        session.commit()
        session.refresh(counter)
        return counter.value


def reset_counter() -> int:
    """Reset the counter to 0 and return the new value."""
    with get_session() as session:
        counter = session.exec(select(Counter)).first()
        if counter is None:
            # Initialize counter if it doesn't exist
            counter = Counter(value=0, updated_at=datetime.utcnow())
            session.add(counter)
        else:
            counter.value = 0
            counter.updated_at = datetime.utcnow()
        session.commit()
        session.refresh(counter)
        return counter.value
