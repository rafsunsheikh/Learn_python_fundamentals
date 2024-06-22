secret_number = 9
 
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Correct guess. You won!")
        break 
    else:
        print("wrong guess. Try again!")
else:
    print("You failed!")