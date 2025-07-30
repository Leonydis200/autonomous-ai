from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, TextLog
import subprocess
import sys
import os
import importlib

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

class AIApp(App):
    CSS_PATH = "tui.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("🤖 Autonomous AI Interface", id="title")
        yield Button("Update Code", id="update")
        yield Button("Run Tests", id="test")
        yield Button("Reload Self", id="reload")
        yield TextLog(highlight=True, markup=True, id="log", max_lines=200)
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        log = self.query_one(TextLog)
        btn = event.button.id
        if btn == "update":
            result = subprocess.run(["git", "pull"], cwd=REPO_DIR, capture_output=True, text=True)
            log.write("[bold cyan]Git Pull:[/]\n" + result.stdout + result.stderr)
        elif btn == "test":
            result = subprocess.run([sys.executable, "test_main_unittest.py"], cwd=REPO_DIR, capture_output=True, text=True)
            log.write("[bold yellow]Test Results:[/]\n" + result.stdout + result.stderr)
        elif btn == "reload":
            try:
                import main
                importlib.reload(main)
                log.write("[green]Reloaded main.py successfully.[/]")
            except Exception as e:
                log.write(f"[red]Reload failed:[/] {e}")

if __name__ == "__main__":
    AIApp().run()
