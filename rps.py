import random as rand
botchoice = ["rock", "paper", "scissors"]
bot = rand.choice(botchoice)
user = input("What do you choose? Rock (R), Paper (P), or Scissors (S)").upper()

if bot == "rock" and user == "R":
    print("It's a tie!")
elif bot == "rock" and user == "P":
    print (f"The bot chose {bot} and the user chose paper. The user wins!")
elif bot == "rock" and user == "S":
    print (f"The bot chose {bot} and the user chose scissors. The bot wins!")

if bot == "paper" and user == "P":
    print("It's a tie!")
elif bot == "paper" and user == "S":
    print (f"The bot chose {bot} and the user chose scissors. The user wins!")
elif bot == "paper" and user == "R":
    print (f"The bot chose {bot} and the user chose rock. The bot wins!")

if bot == "scissors" and user == "S":
    print("It's a tie!")
elif bot == "scissors" and user == "R":
    print (f"The bot chose {bot} and the user chose rock. The user wins!")
elif bot == "scissors" and user == "P":
    print (f"The bot chose {bot} and the user chose paper. The bot wins!")