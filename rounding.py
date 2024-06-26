def rounding(numbers):
    result = []
    for num in numbers:
        result.append(round(float(num)))
    return result


numbers = input().split(" ")

print(rounding(numbers))
