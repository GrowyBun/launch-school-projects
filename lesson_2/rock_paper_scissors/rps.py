import random as r

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

def get_user_choice():
    prompt(f"Choose one from: {', '.join(VALID_CHOICES)}")
    choice = input().lower()
    while choice not in VALID_CHOICES:
        prompt('That is not a valid choice')
        choice = input().lower()
    return choice

def get_computer_choice():
    return r.choice(VALID_CHOICES)

def display_choices(user, computer):
    prompt(f'You chose {user}')
    prompt(f'The computer chose {computer}.')

def calculate_winner(user, computer):
    if ((user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')):
        return 'You'
    elif ((user == 'rock' and computer == 'paper') or
        (user == 'paper' and computer == 'scissors') or
        (user == 'scissors' and computer == 'rock')):
        return 'Computer'
    return 'Tie'

score = {'You': 0, 'Computer': 0}

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    display_choices(user_choice, computer_choice)
    winner = calculate_winner(user_choice, computer_choice)
    if winner == 'Tie':
        prompt("It's a tie!")
    else:
        prompt(f'{winner} won!')
        score[winner] += 1
    prompt(f"Score - You: {score['You']}, Computer: {score['Computer']}")
    prompt('Do you want to play again? (y/n)')
    answer = input()
    if answer and answer[0].lower() != 'y':
        break