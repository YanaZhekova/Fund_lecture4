def smallest_of_three_numbers(numbers):
    return min(numbers)

numbers = []
first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers.append(first_number)
numbers.append(second_number)
numbers.append(third_number)

print(smallest_of_three_numbers(numbers))