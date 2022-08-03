import random

minNum = 1
maxNum = 10 
maxTry = 4 
randomNum = random.randint(0,10)
count = 0
print(randomNum)
while (count < maxTry) :
    try:
        numGuess = int(input("Enter an integer to guess:"))
        if (numGuess > maxNum or numGuess < minNum) :
            print(f'Please enter an interger in the range [{minNum}, {maxNum}]')
        else:
            count+=1
            if (numGuess == randomNum) :
                print("Congrats that you guess the number the number correctly")
                break
            elif (numGuess < randomNum) :
                print("Try a higher number")
                print(f'You have {maxTry - count} guesses remaining')
            elif (numGuess > randomNum) :
                print("Try a lower number")
                print(f'You have {maxTry - count} guesses remaining')
    except ValueError:
        print("Please enter an integer to guess")