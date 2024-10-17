class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

def create_rule(rule_string):
    """Parse a rule string and return the corresponding AST."""
    # Here we should implement parsing logic to convert rule_string to AST
    # For simplicity, we will return a mock node. This function needs to be implemented properly.
    return Node("operator", Node("operand", value="age"), Node("operand", value="30"))

def combine_rules(rules):
    """Combine multiple rules into a single AST."""
    # Implement logic to combine ASTs
    # Return the combined root node
    return Node("operator", Node("operand", value="combined"), Node("operand", value="1"))
