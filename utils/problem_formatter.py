from . import indentation
from . import line_break

def format(problem: str) -> str:
    [operand_1, operator, operand_2] = problem.split()

    operand_1_length = len(operand_1)
    operand_2_length = len(operand_2)
        
    # first operand is longer in length
    if operand_1_length > operand_2_length:
        return (
            f'{indentation.indent_arithmetic(operand_1, 2)}\n' +
            f'{operator} {indentation.indent_arithmetic(operand_2, operand_1_length - operand_2_length)}\n' +
            f'{line_break.get(operand_1_length + 2)}'
        )

    # second operand is longer in length
    if operand_1_length < operand_2_length:
        return (
            f'{indentation.indent_arithmetic(operand_1, operand_2_length - operand_1_length + 2)}\n' +
            f'{operator} {operand_2}\n' +
            f'{line_break.get(operand_2_length + 2)}'
        )
    
    # both operands are of the same length
    return (
        f'{indentation.indent_arithmetic(operand_1, 2)}\n' +
        f'{operator} {operand_2}\n' +
        f'{line_break.get(operand_1_length + 2)}'
    )