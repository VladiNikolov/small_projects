import random
print("Guess the number")
input_number = int(input("Enter number between 1 and 20: "))
number = random.randint(1, 20)
if input_number == number:
    print("You Win")
else:
    print("Next Try")
print(f"Computer number is: {number}")

