__author__ = 'bahrom'


from random import choice

import unittest
from main import parser


class ParserUnitTest(unittest.TestCase):
    def setUp(self):
        self.expression = parser.EXPRESSION

    def test_get_last_given_char_index(self):
        char = '('
        last_char_index = parser.get_last_given_char_index(self.expression, char)
        self.assertEquals(
            self.expression.rfind(char), last_char_index
        )

    def test_get_first_given_char_index(self):
        char = ')'
        first_char_index = parser.get_first_given_char_index(self.expression, char)
        self.assertEquals(
            self.expression.find(char), first_char_index
        )

    def test_get_innermost_rightmost_group(self):
        self.assertEquals(
            '3-1*2-3/-4-2**3',
            parser.get_innermost_rightmost_group(self.expression, '(', ')'),
        )

    def test_split_into_numbers_and_operations(self):
        self.assertEquals(
            ['3', '-', '11', '*-', '2', '-', '3', '/-', '44', '*', '5', '+', '11'],
            parser.split_into_numbers_and_operations('3-11*-2-3/-44*5+11')
        )

    def test_format_fields_parses_numbers_and_operations(self):
        expression = '3-11*-2-3/-44*5+11--2*-3**2'
        fields = parser.split_into_numbers_and_operations(expression)
        self.assertEquals(
            [3, '-', 11, '*', -2, '-', 3, '/', -44, '*', 5, '+', 11, '-', -2, '*', -3, '**', 2],
            parser.format_fields(fields)
        )

    def test_format_fields_raises_exception_for_invalid_format(self):
        fields = ['1', '*+', '2', '/*', '3']
        self.assertRaises(Exception, parser.format_fields, fields)

    def test_format_fields_raises_exception_for_unsupported_ops(self):
        field = choice(['+--', '***', '**-', '++++'])
        self.assertRaises(Exception, parser.format_fields, [field])

def main():
    unittest.main()

if __name__ == 'main':
    main()