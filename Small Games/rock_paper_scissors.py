import random

print("Rock, paper, scissors, Shoot!")
my_list = ["rock", "paper", "scissors"]
computer_counter = 0
human_counter = 0

while human_counter < 2 or computer_counter < 2:
    if computer_counter == 2 or human_counter == 2:
        break
    computer_input = random.choice(my_list)
    human_input = input("You: ")
    print(f"Computer: {computer_input}")

    if computer_input == human_input:
        print(f"Try again.")
    elif computer_input == "rock" and human_input == "paper":
        human_counter += 1
        print("You win!")
    elif computer_input == "scissors" and human_input == "paper":
        computer_counter += 1
        print("Computer wins!")
    elif computer_input == "paper" and human_input == "rock":
        computer_counter += 1
        print("Computer wins!")
    elif computer_input == "paper" and human_input == "scissors":
        human_counter += 1
        print("You win!")
    elif computer_input == "rock" and human_input == "scissors":
        computer_counter += 1
        print("Computer wins!")
    elif computer_input == "scissors" and human_input == "rock":
        human_counter += 1
        print("You win!")
print()
print("The final result is:")
print(f"Computer {computer_counter} : {human_counter} You")
