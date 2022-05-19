import random
print("Guess the number")
input_number = int(input("Please enter number between 1 and 5: "))
number = random.randint(1, 5)
count = 1
while input_number != number:
    print(f"Try again : Try № {count}")
    input_number = int(input("Please enter number between 1 and 5: "))
    count += 1
else:
    print(f"Success")
    print(f"You win from the {count} attempt!")