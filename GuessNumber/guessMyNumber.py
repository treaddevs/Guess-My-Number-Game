''' guessMyNumber
    Sam Treadwell
    CS 5001
    10/27/2022
'''
import random
# "import random" is necessary to generate a random number

# The first funciton, firstGuess, takes the first_guess the player guesses
# and compares it to the randomly generated number, random_number
def firstGuess(first_guess, random_number):
    if first_guess == random_number:
        return("You guessed the right number, you win!")
    elif first_guess < random_number: 
        return("Your number was too low")
    else:
        if first_guess > random_number:
            return("Your number was too high")
#firstGuess()

# The second funciton, additionalGuesses, takes the absolute value of both the 
# difference between the first_guess and the random_number and the difference 
# between the next_guess and the random_number before comparing them to each other
# to indicate if the guesses are "Getting Hotter" or "Getting Colder", in that they 
# are either moving closer to or further from the actual value of the random_number
def additionalGuesses(first_guess, next_guess, random_number):
    difference_first = abs(first_guess - random_number)
    difference_next = abs(next_guess - random_number)
    if difference_next == 0:
        return("You guessed the right number, you win!")
    elif difference_next < difference_first: 
        return("Getting Hotter")
    else:
        if difference_next > difference_first:
            return("Getting Colder")
#secondGuess()

# The main funciton executes the full program where the program randomly generates 
# a number and the player inputs their first_guess before it prints from the firstGuess
# function (telling them if their guess was right, too low, or too high)
def main(min_value, max_value):
    random_number = random.randint(min_value, max_value)

    first_guess = int(input("Guess a number between " + str(min_value) + " and " + str(max_value) + ": "))

    print(firstGuess(first_guess, random_number))

# The while loop in this function indicates when the first_guess is not the same as 
# the random_number the player then needs to input a new guess called the next_guess 
# which will tell them if they are moving closer to or further from the actual value
    while first_guess != random_number:
        next_guess = int(input("Guess a number between " + str(min_value) + " and " + str(max_value) + ": "))
        print(additionalGuesses(first_guess, next_guess, random_number))
# The first_guess is then replaced with the next_guess so that every new guess is compared
# to the most recent guess
        first_guess = next_guess
# "Congrats!" is printed when the loop is False ending the loop and printing the statement
# in full: "You guessed the right number, you win!", "Congrats!"
    print("Congrats!")
main(1, 10) 



