# fibonacci series with memoization

def fib_memoization(n):
    """

    :param n: a positive integer
    :return: the nth fibonacci number
    """
    # define an empty dict or cache
    cache = {}

    # define fibonacci as a separate function
    def fibonacci(n):

        # if the n key is already in the dictionary,
        # returns its value
        if n in cache:
            return cache[n]
        # else calculate the fibonacci value for n and store it in cache
        else:
            if n < 2: # base case for recursion
                cache[n] = n # update cache for n not already in cache
                return n
            else:
                cache[n] = fibonacci(n-1) + fibonacci(n-2) # update cache
                return cache[n]

    # return the value of fibonacci(n) in the main function
    return fibonacci(n)


print(fib_memoization(1))
print(fib_memoization(2))
print(fib_memoization(3))
print(fib_memoization(10))
print(fib_memoization(50))
print(fib_memoization(100))


