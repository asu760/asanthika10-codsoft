import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors Game!")

    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Try again.")
            continue

        computer = get_computer_choice()
        print(f"🧍 You chose: {user}")
        print(f"💻 Computer chose: {computer}")

        result = determine_winner(user, computer)
        print(f"🏁 Result: {result}")

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"📊 Scores → You: {user_score} | Computer: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("👋 Thanks for playing!")
            break

# Start the game
play_game()
