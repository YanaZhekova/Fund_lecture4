def palindromes(num):
    backward_num = ""
    current_num = num
    for i in range(len(num) - 1, -1, -1):
        backward_num += str(num[i])
    if int(current_num) == int(backward_num):
        return True
    else:
        return False


numbers = input().split(", ")
for number in numbers:
    print(palindromes(number))
