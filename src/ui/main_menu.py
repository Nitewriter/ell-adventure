from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, Header

from ui.settings_screen import SettingsScreen  # Add this import


class MainMenu(App):
    """Main menu application for the game."""

    CSS_PATH = "styles/main_menu.tcss"
    SCREENS = {"settings": SettingsScreen}  # Provide the class, not an instance

    def compose(self) -> ComposeResult:
        """Compose the UI elements."""
        yield Header()
        yield Container(
            Button("Start Game", id="start_game"),
            Button("Settings", id="settings"),
            Button("Exit", id="exit"),
            id="menu_container",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id
        if button_id == "start_game":
            self.start_game()
        elif button_id == "settings":
            self.push_screen("settings")  # Change this line
        elif button_id == "exit":
            self.exit_app()

    def start_game(self) -> None:
        """Start the game."""
        self.log("Starting the game...")

    def exit_app(self) -> None:
        """Exit the application."""
        self.exit()


if __name__ == "__main__":
    MainMenu().run()
