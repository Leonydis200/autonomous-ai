#!/data/data/com.termux/files/usr/bin/bash

pkg update -y && pkg upgrade -y
pkg install -y python git

mkdir -p ~/AutonomousAI
cd ~/AutonomousAI || exit

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

echo "[✓] Environment ready!"
