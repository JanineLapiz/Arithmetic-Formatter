from unittest import TestCase
from utils import problem_formatter

class TestProblemFormatter(TestCase):
    def test_operand_1_is_shorter(self):
        result = problem_formatter.format('12 + 4563')

        expected_result = (
            '    12\n' +
            '+ 4563\n' +
            '------'
        )

        self.assertEqual(result, expected_result)
    
    def test_operand_1_is_longer(self):
        result = problem_formatter.format('4563 + 12')

        expected_result = (
            '  4563\n' +
            '+   12\n' +
            '------'
        )

        self.assertEqual(result, expected_result)
    
    def test_operand_1_and_2_are_same_length(self):
        result = problem_formatter.format('1245 + 8462')

        expected_result = (
            '  1245\n' +
            '+ 8462\n' +
            '------'
        )

        self.assertEqual(result, expected_result)