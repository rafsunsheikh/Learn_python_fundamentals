weight = float(input("Enter your weight: "))
choice = input("(L)bs or (K)g: ")
if choice.upper() == "L":
    weight_in_kg = weight * 0.45
    print(f"Your weight in kg is: {weight_in_kg} kg")

elif choice.upper() == "K":
    weight_in_lbs = weight / 0.45
    print(f"Your weight in lbs is: {weight_in_lbs} lbs")
else:
    print("Bad input! Please enter either 'L' or 'K'")