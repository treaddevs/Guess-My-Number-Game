''' testGuessMyNumber
    Sam Treadwell
    CS 5001
    10/27/2022
'''
from guessMyNumber import firstGuess, additionalGuesses 

def testfirstGuess():
# The first test case is True
        first_guess = 8
        random_number = 8
        actual = firstGuess(first_guess, random_number)
        expected = "You guessed the right number, you win!"
        print("Test firstGuess")
        print("Expected ", expected)
        print("Actual ", actual)

# The second test case is False
        first_guess = 5
        random_number = 8
        actual = firstGuess(first_guess, random_number)
        expected = "Your number was too low"
        print("Test firstGuess")
        print("Expected ", expected)
        print("Actual ", actual)

def testadditionalGuesses():
# The first test case is True
        first_guess = 8
        random_number = 8
        actual = additionalGuesses(first_guess, next_guess, random_number)
        expected = "You guessed the right number, you win!"
        print("Test additionalGuesses")
        print("Expected ", expected)
        print("Actual ", actual)

# The second test case is False
        next_guess = 7
        random_number = 8
        next_guess = 9
        actual = additionalGuesses(first_guess, next_guess, random_number)
        expected = "Getting Colder"
        print("Test additionalGuesses")
        print("Expected ", expected)
        print("Actual ", actual)


