# Find the fibonacci sum using recursion

def fibonacci(n):
    """
     :param n: A positive integer
    :return: returns the number in the fibonacci sequence, with the index corresponding to the input number
    Ex: Fibonacci sequence : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, .....
    fibonacci(3) = 2
    fibonacci(8) = 21
    """
    # Check for correct parameters
    if n < 0:
        print("Fibonnaci sum can be calculated only for positive numbers")
        return None

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)

# Test cases
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(7))
print(fibonacci(10))
print(fibonacci(-10))


