# Given a string, return its reverse

def reverse_string_recursive(input_string):

    """
    :param input_string: the string to be reversed
    :return: the reversed string
    """
    n = len(input_string)
    # Basecase
    if n < 2:
        return input_string

    # Recursion
    return (input_string[n-1] + reverse_string_recursive(input_string[:n-1]))



print(reverse_string_recursive("Yellowstone"))
print



