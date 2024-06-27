def min_number(numbers):
    return min(numbers)


def max_number(numbers):
    return max(numbers)


def sum_number(numbers):
    return sum(numbers)


numbers = list(map(int, input().split(" ")))
print(f"The minimum number is {min_number(numbers)}")
print(f"The maximum number is {max_number(numbers)}")
print(f"The sum number is: {sum_number(numbers)}")
