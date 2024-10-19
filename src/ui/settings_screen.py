from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label, Switch


class SettingsScreen(Screen):
    """A screen for game settings."""

    CSS_PATH = "styles/settings_screen.tcss"

    def compose(self) -> ComposeResult:
        """Compose the settings UI."""
        yield Header()
        yield VerticalScroll(
            Label("Game Settings", id="settings_title"),
            Switch(value=False, id="sound_switch"),
            Label("Sound"),
            Switch(value=False, id="music_switch"),
            Label("Music"),
            Switch(value=False, id="fullscreen_switch"),
            Label("Fullscreen"),
            Button("Back to Main Menu", id="back_button"),
            id="settings_container",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events.

        Args:
            event (Button.Pressed): The button pressed event.
        """
        if event.button.id == "back_button":
            self.app.pop_screen()

    def on_switch_changed(self, event: Switch.Changed) -> None:
        """Handle switch toggle events."""
        if event.switch and event.switch.id:
            setting = event.switch.id.replace("_switch", "")
            state = "on" if event.value else "off"
            self.notify(f"{setting.capitalize()} turned {state}")
        else:
            self.notify("Unknown setting changed")
