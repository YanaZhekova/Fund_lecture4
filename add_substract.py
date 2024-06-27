def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(sum, third_number):
    return sum - third_number


def add_and_subtract(first_number, second_number, third_number):
    sum_numbers(first_number, second_number)
    return subtract(sum_numbers(first_number, second_number), third_number)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
