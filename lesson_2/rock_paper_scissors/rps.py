import random
import os

VALID_CHOICES = ['rock', 'paper', 'scissors','lizard', 'spock']
CHOICE_ABBREVIATIONS = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock',
}
WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def clear_screen():
    # 'cls' for Windows, 'clear' for macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt(message):
    print(f'==> {message}')

def greeting():
    prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
    prompt('Best to 5 wins.')
    prompt('Rules:\n\n'
           'Scissors cuts Paper covers Rock crushes Lizard\n'
           'poisons Spock smashes Scissors decapitates Lizard\n'
           'eats Paper disproves Spock vaporizes Rock crushes Scissors.\n')

def get_user_choice():
    prompt(f"Choose one from: {', '.join(VALID_CHOICES)}")
    prompt("You can use: r, p, sc, l, sp")
    choice = input().lower().strip()

    if choice in CHOICE_ABBREVIATIONS:
        choice = CHOICE_ABBREVIATIONS[choice]

    while choice not in VALID_CHOICES:
        prompt('That is not a valid choice')
        choice = input().lower().strip()
        if choice in CHOICE_ABBREVIATIONS:
            choice = CHOICE_ABBREVIATIONS[choice]

    return choice

def get_computer_choice():
    return random.choice(VALID_CHOICES)

def display_choices(user, computer):
    prompt(f'You chose {user}')
    prompt(f'The computer chose {computer}.')

def calculate_winner(user, computer):
    if computer in WINNING_COMBOS[user]:
        return 'You'
    if user in WINNING_COMBOS[computer]:
        return 'Computer'
    return 'Tie'

def display_score(current_score):
    prompt(f"Score - You: {current_score['You']}, Computer: {current_score['Computer']}")

def match_is_over(winner_score):
    return winner_score == 5

def game():
    score = {'You': 0, 'Computer': 0}
    greeting()

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        clear_screen()
        display_choices(user_choice, computer_choice)
        winner = calculate_winner(user_choice, computer_choice)
        if winner == 'Tie':
            prompt("It's a tie!")
        else:
            prompt(f'{winner} won the round!')
            score[winner] += 1

        display_score(score)
        if winner != 'Tie' and match_is_over(score[winner]):
            prompt(f'The grand champion is: {winner}!')
            break
        
        if winner == 'Tie' or not match_is_over(score[winner]):
            prompt('Do you want to play again? (y/n)')
            answer = input().lower().strip()
            if answer and answer[0] != 'y':
                break

game()