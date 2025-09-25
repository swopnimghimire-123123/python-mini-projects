import random
while True:
    #ask player for input
    i=input("rock/paper/sissor ie (r/p/s)")
    #ask computer for input
    l=["r","p","s"]
    computer=random.choice(l)
    # accepting both upper and lower case
    choice=i.lower()
    # printing user response 
    if choice=="r":
        print("Your input was Rock")
    elif choice=="p":
        print("Your input was Paper")
    elif choice=="s":
        print("Your input was Sissor")
    else:
        print("invalid input form the user chose from rock/paper/sissor ie (r/p/s)")
        #restart the loop if the user enters invalid input
        continue 
    #show what the computer chose 
    if computer == "r":
        print("Computer input was Rock")
    elif computer == "p":
        print("Computer input was paper")
    elif computer == "s":
        print("Computer input was Sissor")
    #the internal logic of the game
    if choice==computer:
        print("It's a tie")
    elif( choice=="r" and computer=="s") or \
        ( choice=="p" and computer=="r") or \
        ( choice=="s" and computer=="p"):
        print("You won")
    else:
        print("Computer won")
    play_again=input("Do you want to play again (y/n)?")
    if play_again.lower() !="y":
        print("Thanks for playing!!!!")
        break
