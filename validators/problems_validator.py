from . import problem_validator
from typing import List

def validate(problems: List[str]) -> None:
    number_of_problems = len(problems)

    if number_of_problems > 5:
        raise Exception('Too many problems.')

    for problem in problems:
        problem_validator.validate(problem)