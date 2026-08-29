products = ["Milk", "Bread", "Chocolate", "Chips", "Juice"]
prices = [5, 3, 6, 4, 5]

cart_items = []
cart_prices = []


print("=== Welcome to Mini Supermarket ===")
print("Available Products:")
print(f"1. {products[0]} - ${prices[0]}")
print(f"2. {products[1]} - ${prices[1]}")
print(f"3. {products[2]} - ${prices[2]}")
print(f"4. {products[3]} - ${prices[3]}")
print(f"5. {products[4]} - ${prices[4]}")
print("-" * 35)


cart_items.append(products[0])  

cart_prices.append(prices[0])

cart_items.append(products[2])  

cart_prices.append(prices[2])

cart_items.append(products[4]) 

cart_prices.append(prices[4])


cart_items.insert(0, products[3])  
cart_prices.insert(0, prices[3])



cart_items.remove("Juice")
cart_prices.remove(5)


total_price = sum(cart_prices)
item_count = len(cart_items)


discount = 0

if total_price >= 20:
    discount = 5
elif total_price >= 10:
    discount = 2
else:
    discount = 0

final_price = total_price - discount

items_str = ", ".join(cart_items)

print("\nRECEIPT")
print(f"Items ({item_count}): {items_str}")
print(f"Total: ${total_price}")
print(f"Discount: ${discount}")
print(f"Final Price: ${final_price}")
print("Thank you for shopping! ")