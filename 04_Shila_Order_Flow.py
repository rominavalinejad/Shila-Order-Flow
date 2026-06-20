# --- Shila Restaurant Order Management ---
# Step 1: Menu List & Prices
shila_menu = [
                "combo", "pizza-30cm", "pizza-23cm",
                "fitex-pizza", "mini-pizza","stromboli", "fried-chicken",
                "burger", "hot-sandwich", "pasteroni", "hotdog", "appetizer", "soda", "water"
                ]
shila_price = {
                "combo": 910000, "pizza-30cm": 650000, "pizza-23cm": 450000, "fitex-pizza": 320000,
                "mini-pizza": 250000, "stromboli": 290000, "fried-chicken": 390000, "burger": 280000,
                "hot-sandwich": 260000, "pasteroni": 270000, "hotdog": 210000, "appetizer": 120000,
                "soda": 60000, "water": 20000
                }
# Step 2: User Cart List
user_cart = []
print("-" * 50)
print("*Welcome to Shila Restaurant*")
print("-" * 50)
print("Our Menu:")
print("Combo🍱 | Pizza-30cm🍕 | Pizza-23cm🍕 | Fitex-pizza🍕")
print("Mini-pizza🍕 | Stromboli🥖 | Fried-chicken🍗 | Burger🍔")
print("Hot-sandwich🥪 | Pasteroni🍝 | Hotdog🌭 | Appetizer🍟")
print("Drinks: Soda🥤 | Water💧")
print("-" * 50)
print("Guide: Type the food name to order.\nWhen you are done, simply type 'exit'")

# Step 3: Order Selection Loop
while True:
    order = input("💠Your Iteam:").lower().strip()
    if order == "exit":
        break

# Step 4: Check Menu Availability and Update Cart
    if order in shila_menu:
        user_cart.append(order)
        print(f"Successfully added '{order}' to your cart.✅")
    else:
        print(f"Sorry, '{order}' is not in our menu!❌")

# Step 5: Display Final Shopping Bill & Calculate Total Price
print("\n" + "=" * 50)
print("             🧾 YOUR FINAL BILL 🧾             ")
print("=" * 50)
total_bill = 0
for item in set(user_cart):
        count = user_cart.count(item)
        item_price = shila_price[item] * count
        total_bill += item_price
        print(f"💠{item.capitalize()} x{count}: {item_price:,} t")
print("-" * 50)
print("🛒Full shopping list: " + " , ".join(user_cart))
print(f"🛍Total items ordered: {len(user_cart)}")
print(f"💰Total Payable: {total_bill:,} Toman")
print("-" * 50)
print("\n✨ Thank you for choosing Shila! ✨")
        
        






