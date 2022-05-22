def chocolate_number(total, price):
    count = int(total / price)
    change = int(total % price)
    return count, change
    # return the number of bars that can be bought and the change


total_money = int(input("total money:"))
price = int(input("price:"))
# suppose that money and price are simple numeric variables

result = chocolate_number(total_money, price)
print("bars:", result[0])
print("change:", result[1])

"""
Example:
input:
total money:20
price:7

output:
bars: 2
change: 6
"""
