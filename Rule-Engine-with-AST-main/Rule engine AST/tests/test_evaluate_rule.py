import pytest
from app.evaluate_rule import evaluate_rule

def test_evaluate_rule():
    ast = {"type": "mock_ast"}  # Mock AST
    user_data = {"age": 35}
    result = evaluate_rule(ast, user_data)
    assert result is True  # Check evaluation result
