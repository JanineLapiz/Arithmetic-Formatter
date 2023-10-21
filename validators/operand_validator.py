def validate(operand: str) -> None:
    if not operand.isnumeric():
        raise Exception("Numbers must only contain digits.")
    
    if len(operand) > 4:
        raise Exception("Numbers cannot be more than four digits.")
