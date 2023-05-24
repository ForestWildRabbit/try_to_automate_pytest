
def factorial(n: int):
    if n < 0:
        return "The number can not be negative."
    elif not isinstance(n, int):
        return "Only integer numbers are accepted."
    elif n == 1 or n == 0:
        return 1

    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


