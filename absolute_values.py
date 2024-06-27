def absolute_values(numbers):
    absolute_values = []
    for number in numbers:
        current_number = float(number)
        absolute_values.append(abs(current_number))
    return absolute_values


numbers = input().split(" ")

print(absolute_values(numbers))