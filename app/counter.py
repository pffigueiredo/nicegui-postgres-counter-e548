from nicegui import ui
from app.counter_service import get_counter_value, increment_counter, reset_counter


def create():
    """Create the counter module UI."""

    @ui.page("/")
    def counter_page():
        # Apply modern theme colors
        ui.colors(
            primary="#2563eb",
            secondary="#64748b",
            accent="#10b981",
            positive="#10b981",
            negative="#ef4444",
            warning="#f59e0b",
            info="#3b82f6",
        )

        # Main container with centered layout
        with ui.column().classes("items-center justify-center min-h-screen bg-gray-50 p-8"):
            # Header
            ui.label("Counter Application").classes("text-4xl font-bold text-gray-800 mb-8")

            # Counter display card
            with ui.card().classes("p-8 bg-white shadow-xl rounded-2xl text-center min-w-96"):
                ui.label("Current Count").classes("text-lg font-semibold text-gray-600 mb-4")

                # Counter value display
                current_value = get_counter_value()
                counter_display = ui.label(str(current_value)).classes("text-6xl font-bold text-primary mb-8")

                # Button row
                with ui.row().classes("gap-4 justify-center"):
                    # Increment button
                    def handle_increment():
                        new_value = increment_counter()
                        counter_display.set_text(str(new_value))
                        ui.notify(f"Counter incremented to {new_value}", type="positive")

                    ui.button("Increment", on_click=handle_increment).classes(
                        "bg-primary text-white px-6 py-3 rounded-lg shadow-md hover:shadow-lg transition-shadow font-semibold"
                    )

                    # Reset button
                    def handle_reset():
                        new_value = reset_counter()
                        counter_display.set_text(str(new_value))
                        ui.notify("Counter reset to 0", type="warning")

                    ui.button("Reset", on_click=handle_reset).classes(
                        "bg-gray-500 text-white px-6 py-3 rounded-lg shadow-md hover:shadow-lg transition-shadow font-semibold"
                    ).props("outline")

            # Footer info
            ui.label("Values are persistently stored in PostgreSQL").classes("text-sm text-gray-500 mt-8")
