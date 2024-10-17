from ast_builder import create_rule, combine_rules
from evaluate_rule import evaluate_rule

def main():
    # Example usage
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    
    # Create individual rules
    ast1 = create_rule(rule1)
    ast2 = create_rule(rule2)
    
    # Combine rules
    combined_ast = combine_rules([rule1, rule2])
    
    # Example user data
    user_data = {
        "age": 32,
        "department": "Sales",
        "salary": 60000,
        "experience": 6
    }
    
    # Evaluate the combined rule
    is_eligible = evaluate_rule(combined_ast, user_data)
    print(f"User eligibility: {is_eligible}")

if __name__ == "__main__":
    main()
