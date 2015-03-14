__author__ = 'bahrom'

EXPRESSION = '((1-2+(2+5))+(3-(2+1)))-((2-1)-(3-1*2-3/-4-2**3))'


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
    fields.append(''.join(field))                   # add the final remaining field
    return fields


def format_fields(fields):
    """
    :param fields: list of numbers and operations as strings
    :return a list of formatted fields, with numbers cast into integers
    """
    leading_sign = ''
    formatted_fields = []
    for field in fields:
        try:
            result = int(leading_sign+field)
        except ValueError:
            leading_sign = ''                               # Reset the sign
            if len(field) == 1:
                result = field
            elif len(field) == 2:                           # This should happen in the case of *+/*- or **.
                if field == '**':                           # Just raising to a power.
                    result = field
                elif field[1] in '+-':                      # Second value would be a sign in case of *+/*-, so
                    result, leading_sign = field            # field is split into an operation and the sign.
                else:
                    raise Exception('Invalid operation')    # Operation is invalid, ie +/, */, +* etc
            else:
                raise Exception('Unsupported operation')    # Operation is longer than 2 chars (2**-1 not supported yet)
        formatted_fields.append(result)
    return formatted_fields
