import pytest
from app.ast_builder import create_rule

def test_create_rule():
    rule_string = "age > 30"
    ast = create_rule(rule_string)
    assert ast is not None  # Check if AST is created successfully
