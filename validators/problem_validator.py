from . import operand_validator
from . import operator_validator

def validate(problem: str) -> None:
    notations = problem.split()

    [operand_1, operator, operand_2] = notations

    operand_validator.validate(operand_1)

    operator_validator.validate(operator)

    operand_validator.validate(operand_2)
   
    # If more than 3 entries, then it is not supported,
    # i.e., it should look something like: `"23 + 12"`.
    # No need to check if less than or equal to 3; validation above 
    # should be able to catch it, e.g., if there's no operand_2, then 
    # it should throw error.
    if len(notations) > 3: raise Exception("Unsupported number of notations. There should only be 2 operands and 1 operator.")