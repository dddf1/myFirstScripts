from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")
print("GO!")

player = input("Make your choice, Rock, Paper or Scissors:").lower()

if player == "rock" or player == "paper" or player == "scissors":
    rnd_num = randint(0, 2)
    if rnd_num == 0:
        computer = "rock"
    elif rnd_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
        else:
            print("Computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
        else:
            print("Computer wins!")
    else:
        if computer == "paper":
            print("Player wins!")
        else:
            print("Computer wins!")

else:
    print("Something went wrong. Please enter Rock, Paper or Scissors")




