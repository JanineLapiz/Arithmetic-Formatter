from unittest import TestCase
from validators import problems_validator

class TestValidators(TestCase):
    def test_too_many_problems(self):
        with self.assertRaises(Exception) as context:
            problems_validator.validate(['123 + 3', '6 + 3', '10 - 5', '4 + 2', '345 - 1', '56 + 9'])

        self.assertEqual(str(context.exception), 'Too many problems.')
    
    def test_operand_is_not_digit(self):
        with self.assertRaises(Exception) as context:
            problems_validator.validate(['asdsf + 3', '6 + 3'])
        
        self.assertEqual(str(context.exception), 'Numbers must only contain digits.')
    
    def test_too_many_digits(self):
        with self.assertRaises(Exception) as context:
            problems_validator.validate(['1232532 + 3', '6 + 3'])
        
        self.assertEqual(str(context.exception), 'Numbers cannot be more than four digits.')

    def test_unsupported_number_of_notations(self):
        with self.assertRaises(Exception) as context:
            problems_validator.validate(['123 + 3', '6 + 3 - 4'])
        
        self.assertEqual(str(context.exception), 'Unsupported number of notations. There should only be 2 operands and 1 operator.')