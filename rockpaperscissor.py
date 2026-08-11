import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "tie"

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "scissors" and computer_choice == "paper")
        or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"

    else:
        return "computer"


def display_result(user_choice, computer_choice, result):

    print("\n-----------------------------")
    print("Your choice     :", user_choice)
    print("Computer choice :", computer_choice)

    if result == "user":
        print("Result          : You Win! 🎉")

    elif result == "computer":
        print("Result          : Computer Wins! 🤖")

    else:
        print("Result          : It's a Tie! 🤝")

    print("-----------------------------")


def main():

    user_score = 0
    computer_score = 0
    ties = 0

    print("=" * 45)
    print("       ROCK-PAPER-SCISSORS GAME")
    print("=" * 45)

    print("\nGame Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")

    while True:

        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("\nEnter your choice (1-3): ")

        # Convert user's number into choice
        if choice == "1":
            user_choice = "rock"

        elif choice == "2":
            user_choice = "paper"

        elif choice == "3":
            user_choice = "scissors"

        else:
            print("\n❌ Invalid choice!")
            print("Please enter 1, 2, or 3.")
            continue

        # Computer selects randomly
        computer_choice = get_computer_choice()

        # Determine winner
        result = determine_winner(user_choice, computer_choice)

        # Update score
        if result == "user":
            user_score += 1

        elif result == "computer":
            computer_score += 1

        else:
            ties += 1

        # Display result
        display_result(
            user_choice,
            computer_choice,
            result
        )

        # Display current score
        print("\nCurrent Score:")
        print("You      :", user_score)
        print("Computer :", computer_score)
        print("Ties     :", ties)

        # Play again
        play_again = input(
            "\nDo you want to play again? (yes/no): "
        )

        if play_again.lower() != "yes":
            break

    # Final score
    print("\n" + "=" * 45)
    print("              FINAL SCORE")
    print("=" * 45)

    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)
    print("Ties           :", ties)

    if user_score > computer_score:
        print("\n🏆 Congratulations! You are the overall winner!")

    elif computer_score > user_score:
        print("\n🤖 Computer wins the game!")

    else:
        print("\n🤝 The game ended in a tie!")

    print("\nThank you for playing! 😊")


if __name__ == "__main__":
    main()