from . import operand_validator
from . import operator_validator

def validate(problem: str) -> None:
    notations = problem.split()

    if len(notations) > 3: raise Exception("Unsupported number of notations. There should only be 2 operands and 1 operator.")

    [operand_1, operator, operand_2] = notations

    operand_validator.validate(operand_1)

    operator_validator.validate(operator)

    operand_validator.validate(operand_2)