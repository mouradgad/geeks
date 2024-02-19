def guess_number():
    print("Project One (01) : Guess a Number\n")
    target = int(input("Enter a whole number between 1 and 100 (inclusive): "))
    print()
    guess = 50
    tries = 1
    halfway = 50
    
    while True:
        print("The Computer Guessed:", guess)
        if guess == target:
            print("Number", target, "is the number I was thinking of.")
            print("You found this after", tries, "tries.\n")
            print("END: Project One (01)")
            break
        elif guess < target:
            print("The number I am thinking of is higher than", guess, "\n")
            halfway = (halfway) // 2
            if halfway == 0:
                halfway = 1
            guess = guess + halfway
            tries += 1
        else:
            print("The number I am thinking of is less than", guess, "\n")
            halfway = (halfway) // 2
            if halfway == 0:
                halfway = 1
            guess = guess - halfway
            tries += 1
guess_number()
