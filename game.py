def gameLoop():
    wannaPlay = True
    while wannaPlay:
        if(game() == 0):
            break
        if input("Do you want a new round? Y/N") == "N" or input("Do you want a new round? Y/N") == "n":
            break

import random
def game():
    computerScore = 0
    playerScore = 0
    rounds = 0
    while computerScore != 5 and playerScore != 5:
        chioces = ["scissor", "paper", "rock"]
        computerChoice = random.choice(chioces)
        playerChoice = input("enter your choice: (scissor/paper/rock or Q to quit)")
        if(playerChoice == "Q" or playerChoice == "q"):
            return 0

        computerScore += addScore(computerChoice, playerChoice)
        playerScore += addScore(playerChoice, computerChoice)
        if(addScore(playerChoice, computerChoice) == 1):
            print("you win this round")
            print("your score is", playerScore, "computer score is", computerScore)
        else:
            print("you lose this round or you're tied.")
            print("your score is", playerScore, "computer score is", computerScore)
        rounds += 1

    print("you played", rounds, "rounds")
    if(computerScore == 5):
        print("The final result is you lose")
    else:
        print("The final result is you win")

def addScore(computerChoice, playerChoice):
    if computerChoice == "rock" and playerChoice == "rock":
        return 0
    if computerChoice == "rock" and playerChoice == "paper":
        return 0
    if computerChoice == "rock" and playerChoice == "scissor":
        return 1
    if computerChoice == "paper" and playerChoice == "rock":
        return 1
    if computerChoice == "paper" and playerChoice == "paper":
        return 0
    if computerChoice == "paper" and playerChoice == "scissor":
        return 0
    if computerChoice == "scissor" and playerChoice == "rock":
        return 0
    if computerChoice == "scissor" and playerChoice == "paper":
        return 1
    if computerChoice == "scissor" and playerChoice == "scissor":
        return 0

if __name__ == "__main__":
    gameLoop()