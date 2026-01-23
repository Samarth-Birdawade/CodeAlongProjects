prices = {
   'milk' : 28,
   'bread' : 25,
   'eggs' : 60,
}

list_of_items = [ x for x in input("Enter the quantities of itemss you bought (milk, bread, eggs) separated by commas: ").split(",")]

total_price = 0

for price in prices.values():
   quantity = int(list_of_items.pop(0))
   total_price += price * quantity

print(f'The total price of your grocery bill is: {total_price}')