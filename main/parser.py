__author__ = 'bahrom'

EXPRESSION = '((1-2+(2+5))+(3-(2+1)))-((2-1)-(3-1))'


def get_last_given_char_index(expression, char):
    index, location = 0, 0
    for c in expression:
        if c == char:
            location = index
        index += 1
    return location


def get_first_given_char_index(expression, char, start=0):
    index = start
    for c in expression[start:]:
        if c == char:
            return index
        index += 1
    return -1


def get_innermost_rightmost_group(expression, open_char, close_char):
    """
    Given an expression and group start/end identifier characters,
    returns the innermost rightmost group. For example:
    '(2-1)+((3-4)-(2*5))', '(', ')' results in '2*5'
    """
    # Find last opening paren index
    start = get_last_given_char_index(expression, open_char)
    # Find first closing paren index after that opening paren
    end = get_first_given_char_index(expression, close_char, start)
    return expression[start+1:end]