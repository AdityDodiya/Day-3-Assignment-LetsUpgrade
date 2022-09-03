import random

def playAg():
    pg = input("\nDo you want to play again 'y/n': ")
    if pg == 'y' or pg == 'n':
        return pg
    else:
       return playAg()

def guessGame():
    playAgain = 'y'

    while playAgain == 'y':
        computerNum  = random.randint(1,50)
        userNum = int(input("\nEnter a number between 1 to 50: "))

        score = 0
        diff = computerNum - userNum

        if diff == 0:
            print("Its the same number, wow you get 50 points")
            score = score + 50
            print("Your updated score is ", score)

        elif diff<=5 and diff>=-5:
            print("This number is very close to real number")
            print("UserNum = ", userNum)
            print("ComputerNum = ", computerNum)
            score = score + 25
            print("Your updated score is ", score)

        elif diff>=-10 and diff<=10:
            print("This number is close to real number")
            print("UserNum = ", userNum)
            print("ComputerNum = ", computerNum)
            score = score + 10
            print("Your updated score is ", score)

        else:
            print("Sorry, your guess didnt make it ")
            print("UserNum = ", userNum)
            print("ComputerNum = ", computerNum)
            print("Your present score is ", score)


        playAgain = playAg()
    
    else:
        print("Final Score = ", score)


guessGame()