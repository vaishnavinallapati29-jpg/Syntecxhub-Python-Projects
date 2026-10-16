
import random


def play_game():
    print("\n===== NUMBER GUESSING GAME =====")
    print("Choose a difficulty level:")
    print("1. Easy   (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard   (1 to 100)")

    difficulty = input("Enter your choice: ").strip()

    if difficulty == "1":
        maximum = 10
    elif difficulty == "2":
        maximum = 50
    elif difficulty == "3":
        maximum = 100
    else:
        print("Invalid choice. Starting Easy level.")
        maximum = 10

    secret_number = random.randint(1, maximum)
    attempts = 0

    print(f"\nGuess a number between 1 and {maximum}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > maximum:
                print(f"Enter a number from 1 to {maximum}.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print("Congratulations! You guessed correctly!")
                print("Number:", secret_number)
                print("Attempts:", attempts)
                return attempts

        except ValueError:
            print("Invalid input! Enter a whole number.")


def main():
    best_score = None

    while True:
        attempts = play_game()

        if best_score is None or attempts < best_score:
            best_score = attempts
            print("New best score!")

        print("Your best score:", best_score, "attempts")

        replay = input("\nPlay again? (yes/no): ").strip().lower()

        if replay not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
