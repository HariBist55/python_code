def number_check(number):
    if number % 2 == 0:
        print(f"the number is even")
    else:
        print(f"the number is odd")
number = int(input("number:"))
print("\n")
number_check(number)