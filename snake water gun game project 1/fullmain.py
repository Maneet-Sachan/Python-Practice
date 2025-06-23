import random

def play_round():
    # Valid options
    options = ['snake', 'water', 'gun']
    # Computer makes a choice
    comp_choice = random.choice(options)

    # Get user's choice
    user_choice = input("Enter your choice (snake/water/gun or 'quit' to stop): ").strip().lower()
    if user_choice == 'quit':
        return None, comp_choice
    if user_choice not in options:
        print("Invalid choice! Please choose snake, water, or gun.")
        return 'invalid', comp_choice

    # Determine result
    if user_choice == comp_choice:
        result = 'tie'
    elif (user_choice == 'snake' and comp_choice == 'water') or \
         (user_choice == 'water' and comp_choice == 'gun') or \
         (user_choice == 'gun' and comp_choice == 'snake'):
        result = 'user'
    else:
        result = 'computer'

    return result, comp_choice


def main():
    print("Welcome to the Snake, Water, Gun game!")
    user_score = 0
    comp_score = 0
    rounds_played = 0

    while True:
        result, comp_choice = play_round()
        if result is None:
            # User chose to quit
            break
        if result == 'invalid':
            continue

        rounds_played += 1
        if result == 'tie':
            print(f"Both chose {comp_choice}. It's a tie!")
        elif result == 'user':
            user_score += 1
            print(f"Computer chose {comp_choice}. You win this round!")
        else:
            comp_score += 1
            print(f"Computer chose {comp_choice}. Computer wins this round.")

        print(f"Score -> You: {user_score} | Computer: {comp_score}\n")

    # Final results
    print("Game over!")
    print(f"Total rounds played: {rounds_played}")
    print(f"Final Score -> You: {user_score} | Computer: {comp_score}")
    if user_score > comp_score:
        print("Congratulations, you won the game!")
    elif user_score < comp_score:
        print("Oops, the computer won the game. Better luck next time!")
    else:
        print("It's an overall tie!")


if __name__ == '__main__':
    main()
