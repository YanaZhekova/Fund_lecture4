def numbers_divides_10(num):
    return int(num / 10)


def loading_bar(count):
    result = ""
    if count < 10:
        result += count * "%"
        result += (10 - count) * "."
    else:
        result += count * "%"
    return result


number = int(input())

if number < 100:
    output = f"{number}% [{loading_bar(numbers_divides_10(number))}]"
    print(output)
    print("Still loading...")
else:
    print(f"{number}% Complete!")
    output = f"[{loading_bar(numbers_divides_10(number))}]"
    print(output)

