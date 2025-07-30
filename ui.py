import tkinter as tk
import subprocess
import sys
import os
import importlib

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def git_pull():
    result = subprocess.run(["git", "pull"], cwd=REPO_DIR, capture_output=True, text=True)
    return result.stdout + "\n" + result.stderr

def run_tests():
    result = subprocess.run([sys.executable, "-m", "pytest"], cwd=REPO_DIR, capture_output=True, text=True)
    return result.stdout + "\n" + result.stderr

def reload_main():
    import main
    importlib.reload(main)

def update():
    output = git_pull()
    text.insert(tk.END, "[*] Git Pull:\n" + output + "\n")

def test():
    output = run_tests()
    text.insert(tk.END, "[*] Test Results:\n" + output + "\n")

def reload():
    try:
        reload_main()
        text.insert(tk.END, "[✓] Reloaded main.py\n")
    except Exception as e:
        text.insert(tk.END, "[!] Reload failed:\n" + str(e) + "\n")

# GUI
root = tk.Tk()
root.title("Autonomous AI")

tk.Label(root, text="Autonomous AI Interface", font=("Arial", 14)).pack()

tk.Button(root, text="Update Code", command=update).pack(pady=5)
tk.Button(root, text="Run Tests", command=test).pack(pady=5)
tk.Button(root, text="Reload Self", command=reload).pack(pady=5)

text = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text.pack()

root.mainloop()
