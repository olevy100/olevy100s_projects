import random
import time
def dead():
    dead = True
words = input('Enter names seperated by spaces, press enter when you are done:')
names = words.split(' ')
print(names)
while True:
    if len(names) == 1:
        winner = random.choice(names)
        time.sleep(3)
        print(f"The winner of the annual hunger games is {winner}")
        quit()
    nameone = random.choice(names)
    nametwo = random.choice([ele for ele in names if ele != nameone])
    
    situations = [f'{nameone} kill themself',f'{nameone} and {nametwo} form an alliance',f'{nameone} kills {nametwo}', f'{nameone} and {nametwo} share supplies', f'{nameone} finds supplies from the cornucopia', f"{nameone} sees {nametwo}'s fire"]
    situation = random.choice(situations)
    print(situation)
    if situation == f'{nameone} kill themself':
        print(f"{nameone} is dead")
        names.remove(nameone)
        print(" ")
        time.sleep(3)
    if situation == f'{nameone} kills {nametwo}':
        print(f"{nametwo} is dead")
        names.remove(nametwo)
        print(" ")
        time.sleep(3)
    print(f"{len(names)} remain")