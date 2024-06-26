def price_snack(snack, count):
    if snack == "coffee":
        return count * 1.50
    elif snack == "coke":
        return count * 1.40
    elif snack == "water":
        return count * 1.0
    elif snack == "snacks":
        return count * 2.00


snack = input()
count = int(input())
print(f"{price_snack(snack, count):.2f}")
