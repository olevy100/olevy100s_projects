import random
secret_number = random.choice(range(1, 101))
print("""This is a number guessing game, you will get 5 chances to guess a random number
from 1 - 100.""")
print(" ")
for x in range(5):
    a = int(input("what is your guess?"))
    if a == secret_number:
        print(f"congrats, you got it, {x} was the correct number!")
        quit()
    elif a < secret_number:
        print(f"sorry, {a} is too small, try again")
    elif a > secret_number:
        print(f"sorry, {a} is too big, try again")
print("sorry, you didn't get it, try again sometime.")
