import ast
import inspect
import sys
import os
import subprocess
import importlib

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def load_self_ast():
    with open(__file__, 'r') as f:
        source = f.read()
    return ast.parse(source)

def print_function_names(tree):
    print("Functions in this file:")
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            print(" -", node.name)

def git_pull():
    print("\n[🛠] Checking for updates from GitHub...")
    proc = subprocess.run(["git", "pull"], cwd=REPO_DIR, capture_output=True, text=True)
    print(proc.stdout)
    if proc.returncode != 0:
        print("[!] Git pull failed:", proc.stderr)
    else:
        print("[✓] Git updated successfully.")

def git_rollback():
    print("[!] Rolling back to previous version...")
    subprocess.run(["git", "reset", "--hard", "HEAD@{1}"], cwd=REPO_DIR)

def run_tests():
    print("[🧪] Running test suite...")
    proc = subprocess.run([sys.executable, "-m", "pytest"], cwd=REPO_DIR, capture_output=True, text=True)
    print(proc.stdout)
    if "FAILED" in proc.stdout or proc.returncode != 0:
        print("[✗] Tests failed.")
        return False
    print("[✓] All tests passed.")
    return True

def reload_module():
    print("[↻] Reloading self...")
    import main
    importlib.reload(main)

if __name__ == "__main__":
    print("=== SELF-UPDATING AI CORE ===")

    tree = load_self_ast()
    print_function_names(tree)

    git_pull()

    if not run_tests():
        git_rollback()
    else:
        reload_module()
