# cafe.py

# The cafe has a list called "menu"
# a dictionary called "stock"
# and a dictionary called "price"
# The program calculates the total cost of all stock in the cafe
# and assigns it to the variable "total_stock"

menu = ['Coca Cola', 'Coffee', 'Tea', 'Egg mayo sandwich', 
        'Tomato soup', 'Flapjack']

menu_prices = [('Coca Cola', 1.80), ('Coffee', 2.50), ('Tea', 1.50),
               ('Egg mayo sandwich', 3.50), ('Tomato soup', 4.95),
               ('Flapjack', 2.25)]

print(f'''The items available on the menu are:
      {menu}
      ''')

price = dict(menu_prices)

print(f'''Price menu for cafe items:
      {price}
      ''')

stock = {'Coca Cola': 30,
         'Coffee': 58,
         'Tea': 100,
         'Egg mayo sandwich': 8,
         'Tomato soup': 15,
         'Flapjack': 18
         }

print(f'''Current stock of menu items:
      {stock}
      ''')

# Total_stock assigned value of 0
# and 'keys' variable assigned to contain all keys in the
# stock dictionary and the price dictionary

total_stock = 0
keys = stock.keys()

for x in keys:
    item_value = (stock[x] * price[x])
    total_stock += item_value
    if stock[x] <= 10:
        print(f'''
There are {stock[x]} units of {x}
with a total stock value of £{round(item_value, 2)}

*** YOU ARE RUNNING LOW ON {x}, please order more stock. ***
''')
    else:
        print(f'''
There are {stock[x]} units of {x}
with a total stock value of £{round(item_value, 2)}
                ''')

print(f"The total stock value in the cafe is: £{round(total_stock, 2)}")