import random

print("Welcome to the number guessing game!")


def game():
    number_of_guess = 0
    level = input('Please select the level ["Easy"/"Medium"/"Hard"]: ').lower()

    if level == "easy":
        number_of_guess = 10
    elif level == "medium":
        number_of_guess = 5
    else:
        number_of_guess = 3

    random_number = random.randint(1, 100)
    print(f"\nI'm thinking of a number between 1 and 100. You have {number_of_guess} guesses.")

    while number_of_guess > 0:
        guess = int(input("Guess the number: \n"))

        if guess == random_number:
            print(f"🎉 You guessed it right! The number was {random_number}")
            break  # Stop the loop since the user guessed right

        elif abs(guess - random_number) > 10:
            if guess > random_number:
                print("Too high and far.")
            else:
                print("Too low and far.")
            number_of_guess -= 1

        else:  # Close guess but not correct
            if guess > random_number:
                print("Close, but still high.")
            else:
                print("Close, but still low.")
            number_of_guess -= 1

        if number_of_guess == 0:
            print(f"😢 You lost. The correct number was {random_number}")


def main():
    game_is_on = True
    while game_is_on:
        game()  # Start the game round

        # After the game, ask the user if they want to play again
        play_again = input("\nDo you want to play again? Type 'y' for yes or 'n' to exit: ").lower()

        if play_again == 'n':
            print("Thanks for playing! Goodbye.")
            game_is_on = False  # Exit the loop and end the program


main()
