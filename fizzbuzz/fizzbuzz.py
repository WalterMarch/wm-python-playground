MAX: int = 100

print("using standard for loop with range")
for i in range(1, MAX + 1):
    output: str = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"

    print(output or i)

print("using a list comprehension")
fizz_buzz = [
    (
        "FizzBuzz"
        if i % 15 == 0
        else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
    )
    for i in range(1, MAX + 1)
]

print(fizz_buzz)
