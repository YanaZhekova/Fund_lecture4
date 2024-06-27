def even_numbers(nums):
    if nums % 2 == 0:
        return True
    else:
        return False


def result(nums):
    result = filter(even_numbers, nums)
    return list(result)


numbers = list(map(int, input().split(" ")))

print(result(numbers))
