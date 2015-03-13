__author__ = 'bahrom'


import unittest
from main import parser


expression = "((1-2+(2+5))+(3-(2+1)))-((2-1)-(3-1))"


class ParserUnitTest(unittest.TestCase):
    def setUp(self):
        self.expression = expression

    def test_get_last_given_char_index(self):
        char = "("
        last_char_index = parser.get_last_given_char_index(self.expression, char)
        self.assertEquals(
            last_char_index, self.expression.rfind(char)
        )

    def test_get_first_given_char_index(self):
        char = ")"
        first_char_index = parser.get_first_given_char_index(self.expression, char)
        self.assertEquals(
            first_char_index, self.expression.find(char)
        )


def main():
    unittest.main()

if __name__ == "main":
    main()