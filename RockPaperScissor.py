import random

def play():
    user = input("Your Choice: 'r' for rock, 'p' for paper, 's' for scissor ")
    computer = random.choice(['r', 'p', 's'])

    print("Computer chose: " + computer)  #GPT

    
    if user == computer:
        return 'It is a tie'
    
    if win(user, computer):
        return 'You Win'
    return 'You Lost'
    


def win(player, opponent):
    if (player=='r' and opponent=='p') or(player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    return False


print(play())

