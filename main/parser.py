__author__ = 'bahrom'

EXPRESSION = '((1-2+(2+5))+(3-(2+1)))-((2-1)-(3-1*2-3/-4))'


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


def split_into_numbers_and_operations(expression):
    """
    :param expression: an expression string without parens
    :return fields: a list of strings where each string is either a number, an operation,
                    or a set of operations (in the case of a*-b or a**b)
    """
    fields = []
    field = []
    previous_is_digit = expression[0].isdigit()     # Check what the starting data type is
    i = 0                                           # Used to see if have reached the end yet
    for char in expression:
        next_is_digit = char.isdigit()              # Check the next data type
        if previous_is_digit == next_is_digit:      # If it's the same as the previous one
            field.append(char)                      # we're still going through the same field.
        else:                                       # Otherwise we're done,
            fields.append(''.join(field))           # add the field to fields, and
            field = [char]                          # reset the field to only contain the current char
        previous_is_digit = next_is_digit
        i += 1
    if i == len(expression):
        fields.append(''.join(field))
    return fields