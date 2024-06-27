def char_in_range(first_char, second_char):
    result = []
    first_number = ord(first_char)
    second_number = ord(second_char)
    for i in range(first_number+1, second_number ):
        result.append(chr(i))

    return result


first_char = input()
second_char = input()
print(" ".join(char_in_range(first_char, second_char)))
