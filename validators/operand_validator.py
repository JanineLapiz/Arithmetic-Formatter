def validate(operand: str) -> None:
    if not operand.isnumeric():
        raise Exception("Error: Numbers must only contain digits.")
    
    if len(operand) > 4:
        raise Exception("Error: Numbers cannot be more than four digits.")
