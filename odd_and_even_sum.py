def odd_and_even_sum(str):
    result = ""
    even = 0
    odd = 0
    for i in str:
        current_number = int(i)
        if current_number % 2 == 0:
            even += current_number
        else:
            odd += current_number
    result = f"Odd sum = {odd}, Even sum = {even}"
    return result


text =input()
print(odd_and_even_sum(text))