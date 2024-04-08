"""
PowerOfTen
"""
number = int(input("Enter a max three-digit number:"))
if number < 0:
    print("The number cannot be negativ.")
elif number > 999:
    print("The number cannot have more than three digits.")
else:
    decomposed = number % 10
    print(f"{number} = {decomposed}")






"""
Cash Box
"""
to_pay = int(input("To pay:"))
if to_pay < 0:
    print("Negativ payment is invalid.")
while to_pay < 0:
    int(input("To pay:"))
    break
recieved = int(input("Recieved:"))
if recieved > to_pay:
    change = recieved - to_pay
    print(f"Your change is: {change}.")
else:
    print("You did not pay enough.")

