# Rule Engine with AST

This is a simple rule engine that uses an Abstract Syntax Tree (AST) to evaluate user eligibility based on dynamic rules.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourhandle/rule-engine-ast.git
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app/rule_engine.py
```

Alternatively, you can build and run the Docker container:
```bash
docker build -t rule-engine-ast .
docker run -d rule-engine-ast
```

## Design Choices
- **AST Representation**: The engine builds an AST to represent and evaluate rules based on user attributes such as age, department, and salary.
- **Rule Evaluation**: Rules are dynamically created, combined, and evaluated against user data.
