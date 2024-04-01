import numpy as np
x = np.random.choice(range(1,100))
print("This is a number guessing game, you will get 5 chances to guess a random number from 1 - 100.")
print(" ")
for o in range(1, 100):
    a = int(input("what is your guess?"))
    if a == x:
        print(f"congrats, you got it, {x} was the correct number!")
        quit()
    elif a > x:
        print(f"sorry, {a} is too big, try again")
    elif a < x:
        print(f"sorry, {a} is too small, try again")
print(f"{x} was the number, sorry, you didn't get it, try again sometime.")
