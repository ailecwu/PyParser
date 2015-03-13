__author__ = 'bahrom'

expression = "((1-2+(2+5))+(3-(2+1)))-((2-1)-(3-1))"


def get_inner_most_group(expression, open_char, close_char):
    pass


def get_last_given_char_index(expression, char):
    index, location = 0, 0
    for c in expression:
        if c == char:
            location = index
        index += 1
    return location


def get_first_given_char_index(expression, char):
    index = 0
    for c in expression:
        if c == char:
            return index
        index += 1
    return -1