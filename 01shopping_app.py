#shopping app
print("welcome to my shoppong app:")
total_items = int(input("enter how many items:"))
total_price=0

for i in range(1,total_items+1):
    price = float(input(f"enter  price for {i}:"))
    total_price = total_price + price

print(f"total price is {total_price}")
