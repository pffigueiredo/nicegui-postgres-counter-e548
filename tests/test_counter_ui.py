import pytest
from nicegui.testing import User
from app.database import reset_db


@pytest.fixture()
def new_db():
    reset_db()
    yield
    reset_db()


async def test_counter_page_loads(user: User, new_db) -> None:
    """Test that the counter page loads correctly."""
    await user.open("/")

    # Check that main elements are present
    await user.should_see("Counter Application")
    await user.should_see("Current Count")
    await user.should_see("0")  # Initial counter value
    await user.should_see("Increment")
    await user.should_see("Reset")
    await user.should_see("Values are persistently stored in PostgreSQL")


async def test_counter_increment_button(user: User, new_db) -> None:
    """Test that clicking increment button increases counter."""
    await user.open("/")

    # Initial state should show 0
    await user.should_see("0")

    # Click increment button
    user.find("Increment").click()

    # Should now show 1
    await user.should_see("1")

    # Click increment again
    user.find("Increment").click()

    # Should now show 2
    await user.should_see("2")


async def test_counter_reset_button(user: User, new_db) -> None:
    """Test that clicking reset button resets counter to 0."""
    await user.open("/")

    # Increment counter first
    user.find("Increment").click()
    user.find("Increment").click()
    user.find("Increment").click()

    # Should show 3
    await user.should_see("3")

    # Click reset button
    user.find("Reset").click()

    # Should now show 0
    await user.should_see("0")


async def test_counter_workflow(user: User, new_db) -> None:
    """Test complete counter workflow through UI."""
    await user.open("/")

    # Initial state
    await user.should_see("0")

    # Increment several times
    user.find("Increment").click()
    await user.should_see("1")

    user.find("Increment").click()
    await user.should_see("2")

    user.find("Increment").click()
    await user.should_see("3")

    # Reset counter
    user.find("Reset").click()
    await user.should_see("0")

    # Increment again after reset
    user.find("Increment").click()
    await user.should_see("1")


async def test_counter_persistence_across_page_reloads(user: User, new_db) -> None:
    """Test that counter value persists across page reloads."""
    await user.open("/")

    # Increment counter
    user.find("Increment").click()
    user.find("Increment").click()
    await user.should_see("2")

    # Reload page
    await user.open("/")

    # Counter should still show 2
    await user.should_see("2")

    # Should be able to increment from previous value
    user.find("Increment").click()
    await user.should_see("3")
