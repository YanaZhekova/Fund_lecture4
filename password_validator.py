def chars_long(text):
    if 20 >= len(text) >= 6:
        return "Password is valid"
    else:
        return "Password must be between 6 and 10 characters"


def only_letters_digits(text):
    result = ""
    for c in text:
        if c.isalpha() or c.isdigit():
            result = "Password is valid"
        else:
            result = "Password must consist only of letters and digits"
            break
    return result


def two_digits(text):
    result = ""
    count = 0
    for c in text:
        if c.isdigit():
            count += 1
    if count >= 2:
        result = "Password is valid"
    else:
        result = "Password must have at least 2 digits"
    return result


password = input()
if chars_long(password) == only_letters_digits(password) == two_digits(password):
    print(chars_long(password))
else:
    if chars_long(password) != "Password is valid":
        print(chars_long(password))
    if only_letters_digits(password) != "Password is valid":
        print(only_letters_digits(password))
    if two_digits(password) != "Password is valid":
        print(two_digits(password))
