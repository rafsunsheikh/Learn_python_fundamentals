numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

print("\nNow we will remove a value from the numbers list.")
numbers.remove(3)

for number in numbers: 
    print(number)


print("\nNow we will insert a value into the numbers list.")
numbers.insert(0, 10)

for number in numbers:
    print(number)