def result(str, counter):
    new_text = str * counter
    return new_text


str = input()
counter = int(input())

print(result(str, counter))
