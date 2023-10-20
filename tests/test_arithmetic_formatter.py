from unittest import TestCase
from main import format_arithmetic

class TestArithmeticFormatter(TestCase):
    def test_valid_problems(self):
        result: str = format_arithmetic(['123 + 34', '56 - 1000', '180 + 180'], True)

        expected_result: str = (
            '  123        56      180\n' +
            '+  34    - 1000    + 180\n' +
            '-----    ------    -----'
        )

        self.assertEqual(result, expected_result)
    