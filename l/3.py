def guess_number():
    print("Project One (01) : Guess a Number\n")
    print("Enter a whole number between 1 and 100 (inclusive): ")
    target_number = int(input())
    low = 1
    high = 100
    tries = 0
    while high >=low :
        guess = (high + low ) // 2
        print("\nThe Computer Guessed:", guess )
        tries +=1
        if guess < target_number:
            print("The number I am thinking of is higher than", guess)
            low = guess + 1
        elif guess == target_number:
            print("Number", target_number, "is the number I was thinking of.")
            print("You found this after", tries, "tries.")
            break
        else:
            print("The number I am thinking of is less than", guess)
            high = guess - 1
    
    print("\nEND: Project One (01)")
guess_number()
