import ast
import main

def test_parse_ast():
    tree = main.load_self_ast()
    assert isinstance(tree, ast.Module)

def test_detect_functions():
    tree = main.load_self_ast()
    found = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
    expected = {
        "load_self_ast", "list_defined_functions", 
        "git_pull", "git_rollback", 
        "run_tests", "reload_self"
    }
    assert expected.issubset(found)
