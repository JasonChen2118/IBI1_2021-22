def chocolate_number(total, price):
    count = int(total / price)
    return count


total_money = float(input("total money:"))
price = float(input("price:"))

print(chocolate_number(total_money, price))


