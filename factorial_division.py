def factorial(n):
    fact_number = 0
    for i in range(n - 1, 0, -1):
        if i == n - 1:
            fact_number += n * i
        else:
            fact_number = i * fact_number
    return fact_number


first_number = int(input())
second_number = int(input())
result = factorial(first_number)/factorial(second_number)
print(f"{result:.2f}")
