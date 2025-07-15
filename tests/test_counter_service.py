import pytest
from app.counter_service import get_counter_value, increment_counter, reset_counter
from app.database import reset_db


@pytest.fixture()
def new_db():
    reset_db()
    yield
    reset_db()


def test_get_counter_value_initializes_to_zero(new_db):
    """Test that getting counter value for the first time initializes to 0."""
    value = get_counter_value()
    assert value == 0


def test_increment_counter_from_zero(new_db):
    """Test incrementing counter from initial state."""
    value = increment_counter()
    assert value == 1


def test_increment_counter_multiple_times(new_db):
    """Test incrementing counter multiple times."""
    # First increment
    value1 = increment_counter()
    assert value1 == 1

    # Second increment
    value2 = increment_counter()
    assert value2 == 2

    # Third increment
    value3 = increment_counter()
    assert value3 == 3


def test_reset_counter_to_zero(new_db):
    """Test resetting counter to zero."""
    # First increment counter
    increment_counter()
    increment_counter()
    value = get_counter_value()
    assert value == 2

    # Reset counter
    reset_value = reset_counter()
    assert reset_value == 0

    # Verify counter is actually reset
    current_value = get_counter_value()
    assert current_value == 0


def test_reset_counter_when_not_initialized(new_db):
    """Test resetting counter when it hasn't been initialized."""
    value = reset_counter()
    assert value == 0


def test_counter_persistence_across_calls(new_db):
    """Test that counter value persists across multiple function calls."""
    # Increment counter
    increment_counter()
    increment_counter()

    # Get value in separate call
    value = get_counter_value()
    assert value == 2

    # Increment again
    new_value = increment_counter()
    assert new_value == 3

    # Verify persistence
    final_value = get_counter_value()
    assert final_value == 3


def test_counter_workflow(new_db):
    """Test complete counter workflow."""
    # Initial state
    assert get_counter_value() == 0

    # Increment several times
    assert increment_counter() == 1
    assert increment_counter() == 2
    assert increment_counter() == 3

    # Check current value
    assert get_counter_value() == 3

    # Reset
    assert reset_counter() == 0

    # Verify reset worked
    assert get_counter_value() == 0

    # Increment again after reset
    assert increment_counter() == 1
