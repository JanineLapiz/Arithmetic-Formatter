def validate(operator: str) -> None:
    if operator == '+': return

    if operator == '-': return

    raise Exception("Error: Operator must be '+' or '-'.")