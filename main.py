
import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n");
print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")

selected_difficulty = int(input());
difficulty = 3;

if selected_difficulty == 1:
    difficulty = 10;
elif selected_difficulty == 2:
    difficulty = 5;
else:
    difficulty = 3;

print(f"You have {difficulty} chances to guess the correct number.");


target = 4;
#random.randint(0,100);

print("Let's start the game!");
x =199;

while x != target and difficulty > 0:
    print("Enter your guess:")
    x = int(input())

    if(x == target):
        print(f"Congratulations! You guessed the correct number in {selected_difficulty - difficulty} attempts.");
        break;

    if target > x:
        print(f"Incorrect! The number is greater than {x}.");
    else:
        print(f"Incorrect! The number is smaller than {x}.");

    difficulty= difficulty -1 ;

if difficulty == 0:
    print("Bestie you lost");
