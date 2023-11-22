import random

OPTIONS = ['rock', 'paper', 'scissors'] 

SCORES = {  #The scores of the player and computer
    "PLAYER":0,
    "COMPUTER":0
}

def computer_choice(): #Selecting random option for the computer
    return random.choice(OPTIONS)


def player_choice(): #Geting input for the player
    return input("Enter your choice: ").lower()

def check_winner(pl_choice, cm_choice,score_list): #Checking the winner
    if (pl_choice == "rock" and cm_choice == "scissors") or (pl_choice == "paper" and cm_choice =="rock") or (pl_choice == "scissors" and cm_choice == "paper"):
        score_list["PLAYER"] += 1
        print("PLAYER")
    elif (pl_choice == "rock" and cm_choice == "paper") or (pl_choice == "paper" and cm_choice =="scissors") or (pl_choice == "scissors" and cm_choice == "rock"):
        score_list["COMPUTER"] += 1
        print("COMPUTER")
    else:
        print("Draw")



def main():  
  p_choice = player_choice() #Geting input from user for the start while loop
  
  while p_choice in OPTIONS: #Starting the game 
      c_choice = computer_choice()
      print(c_choice)
      check_winner(p_choice, c_choice, SCORES)
      print(SCORES)
      p_choice = player_choice()


main()
