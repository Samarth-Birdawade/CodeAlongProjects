import random

def number_guessing_game():
    num_to_guess = random.randint(1, 10)
    attempts = 3
    print("Welcome to the Number Guessing Game!")
    while attempts > 0:
        guess = input("Guess a number between 1 and 10: ")
        
        # Input validation
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please enter a valid number.")
            continue

        # Actual game logic
        if guess == num_to_guess:
            print("Yay! Your guess is correct")
            return
        elif guess < num_to_guess:
            attempts -= 1
            print(f"Too low! You have {attempts} attempts left.")
        elif guess > num_to_guess:
            attempts -= 1
            print(f"Too high! You have {attempts} attempts left.")
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

if __name__ == "__main__":
    number_guessing_game()