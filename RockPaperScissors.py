# Write your code here
import random

player_name = input("Enter your name: ")
print(f"Hello, {player_name}")

options = input().split(',')
if len(options) == 1:
    options = ['rock', 'paper', 'scissors']


print("Okay, let's start")

def player_won(player_choice, computer_choice, options):
    player_choice_index = options.index(player_choice)
    computer_choice_index = options.index(computer_choice)
    length = len(options) - 1
    
    if computer_choice_index < player_choice_index:
        new_index = computer_choice_index + (length - player_choice_index)
    elif computer_choice_index > player_choice_index:
        if player_choice_index > 0:
            new_index = computer_choice_index % player_choice_index - 1
        else:
            new_index = computer_choice_index - 1
    
    new_half = (length - 1) // 2
    return new_index > new_half

scores = open("rating.txt")

player_score = None
player_index = None
line_index = 0

for line in scores:
    if player_name in line:
        player_index = line_index
        player_score = int(line.replace("\n", "").split()[1])
    line_index += 1
    
if player_score == None:
    player_index = line_index + 1
    player_score = 0


while True:
    player_choice = input()
    if player_choice == "!exit":
        print("Bye!")
        break
    elif player_choice == "!rating":
        print(f"Your rating: {player_score}")
        continue
    elif player_choice not in options:
        print("Invalid input")
        continue
    
    computer_choice = random.choice(options)
    
    if player_choice == computer_choice:
        print(f"There is a draw ({computer_choice})")
        player_score += 50
    else:
        if player_won(player_choice, computer_choice, options):
            print(f"Well done. Computer chose {computer_choice} and failed")
            player_score += 100
        else:
            print(f"Sorry, but computer chose {computer_choice}")


scores.close()
