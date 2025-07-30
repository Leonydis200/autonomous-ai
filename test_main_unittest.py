import unittest
import ast
import main

class TestMainAI(unittest.TestCase):
    def test_parse_ast(self):
        tree = main.load_self_ast()
        self.assertIsInstance(tree, ast.Module)

    def test_function_names(self):
        tree = main.load_self_ast()
        names = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
        expected = {
            "load_self_ast", "list_defined_functions",
            "git_pull", "git_rollback",
            "run_tests", "reload_self"
        }
        self.assertTrue(expected.issubset(names))

if __name__ == '__main__':
    unittest.main()
