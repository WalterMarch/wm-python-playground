def factorial(n: int) -> int:
    output = 1
    if n > 1:
        output = n * (factorial(n - 1))
    return output


print(factorial(6))
