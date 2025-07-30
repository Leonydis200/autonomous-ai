#!/data/data/com.termux/files/usr/bin/bash

# === SETUP ===
echo "[📦] Updating packages..."
pkg update -y && pkg upgrade -y

echo "[🐍] Installing Python & dependencies..."
pkg install -y python git libjpeg-turbo clang freetype harfbuzz libpng pkg-config libxslt libxml2 rust

echo "[🧪] Installing required Python tools..."
pip install --upgrade pip virtualenv wheel setuptools

# === PROJECT CLONE ===
echo "[📂] Cloning your Autonomous AI repo..."
git clone https://github.com/YOUR_USERNAME/AutonomousAI.git
cd AutonomousAI || exit 1

# === VIRTUAL ENV ===
echo "[📦] Setting up virtualenv..."
python -m virtualenv .venv
source .venv/bin/activate

# === DEPENDENCIES ===
echo "[📚] Installing project dependencies..."
pip install 'textual>=0.56.4' # change version as needed

# === CREATE TUI SCRIPT ===
echo "[📝] Writing TUI interface to tui.py..."
cat > tui.py <<EOF
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static, Log

class SelfImprovingAIApp(App):
    CSS_PATH = "styles.css"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Log(id="log_display")
        yield Static("Welcome to the Autonomous AI!", id="info")
        yield Button("Start Self-Improvement", id="start")
        yield Button("Run Diagnostics", id="diagnostics")
        yield Footer()

    def on_button_pressed(self, event):
        log = self.query_one("#log_display", Log)
        if event.button.id == "start":
            log.write("🚀 Beginning self-improvement process...")
            # TODO: Trigger AI upgrade logic
        elif event.button.id == "diagnostics":
            log.write("🔍 Running diagnostic checks...")
            # TODO: Trigger diagnostics

if __name__ == "__main__":
    SelfImprovingAIApp().run()
EOF

# === OPTIONAL: STYLES ===
echo "[🎨] Creating minimal styles.css..."
echo '
#log_display {
    height: 10;
}
' > styles.css

# === RUN ===
echo "[🚀] Launching your Autonomous AI Terminal UI..."
python tui.py
