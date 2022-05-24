# Problem Statement :
# Find the factorial of a given number

def find_factorial(number):
    """

    :param number: a positive integer
    :return: the factorial for the input
    """

    # Check for positive integers
    if number < 0:
        print('Factorial not defined for negative integers')
        return None
    # Base case:
    if number < 1:
        return 1

    # Recursive case
    return number * find_factorial(number-1)

# Test
print(find_factorial(1))
print(find_factorial(5))
print(find_factorial(0))
print(find_factorial(-1))


