player1 = input("Please enter the player1 name:")
player2 = input("Please enter the player2 name: ")

player1Answer = input(player1 +" Do you want to select rock or paper or scissors: " ).lower()
player2Answer = input(player2 +" Do you want to select  rock or paper or scissors: ").lower()

if player1Answer==player2Answer:
    print("It's a tie")

elif player1Answer == 'rock':
    if player2Answer == 'scissors':
     print(player1 + " - Rock wins")
    else:
        print(player2 + " - paper wins")

elif player1Answer == 'scissors':
    if player2Answer == 'paper':
         print(player1 + "scissors wins")
    else:
        print(player2 + " - Rock wins")
elif player1Answer== "paper":
    if player2Answer == "rock":
        print(player1+ " - paper wins")
    else:
        print(player2 + " - scissors wins")

else:
    print("one of the player have given invalid input")



    


