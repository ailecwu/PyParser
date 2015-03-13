__author__ = 'bahrom'


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

    def test_get_inner_rightmost_group(self):
        self.assertEquals(
            '3-1',
            parser.get_innermost_rightmost_group(self.expression, '(', ')'),
        )


def main():
    unittest.main()

if __name__ == 'main':
    main()