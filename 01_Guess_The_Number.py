# Made by Jashan(Tanjiro)
# -------------Challenge-------------
# Make A Mini Game, Guess The Number. User inputs the range in which a random number will be picked, user have to guess it within 5 chances, the program will tell the user whether his/her guess is more than the number or less.
# Source: My Mind LOL

# -------------Code-------------
#importing Modules Required
import random

# main function:
def main():

    # asking for input
    num1=int(input('Enter 1st number: '))
    num2=int(input('Enter 2nd number: '))

    # run the function only when there's in enough gap between 2 numbers.

    if num2-num1>=10:

        # function to run the main game
        def game():

            # declaring some game variables
            gameOver = False
            chances = 0

            # variable containing a random number
            random_num=random.randint(num1, num2)

            # guess number

            # loop to go until either user wins or all chances are gone
            while chances<5:
                guess = int(input('Guess the number:\n'))
                if guess>random_num:
                    print("You're going far away!!")
                elif guess==random_num:
                    print('Bingo! You Won!!')
                    gameOver=True
                    chances=6
                elif guess<random_num:
                    print('It is very less than my number!!')
                chances+=1
            
            # losing condition
            if gameOver==False and chances>=5:
                print('You lose!! My Number Was ' + str(random_num))


        game()
    else:
        print('There must be a gap of 10 or more in the 2 numbers you added!')

main()