from typing import List
from validators import problems_validator
from utils import problem_formatter


def format_arithmetic(problems: List[str], print_result: bool = False) -> str:
    problems_validator.validate(problems)

    formatted_problems = map(problem_formatter.format, problems)

    _line_1: List[str] = []
    _line_2: List[str] = []
    _line_3: List[str] = []

    for formatted_problem in formatted_problems:
        [problem_line_1, problem_line_2, problem_line_3]= formatted_problem.splitlines()

        _line_1.append(problem_line_1)
        _line_2.append(problem_line_2)
        _line_3.append(problem_line_3)

    gap = ' ' * 4

    line_1: str = gap.join(_line_1)
    line_2: str = gap.join(_line_2)
    line_3: str = gap.join(_line_3)

    formatted_arithmetic = '\n'.join([line_1, line_2, line_3])

    if (print_result): print(formatted_arithmetic)

    return formatted_arithmetic