import time
import random
import string
timeout = time.time() + 120
letters = list(string.ascii_uppercase)
score = 0

for o in range(26):    
    letter = random.choice(letters)
    print(f'{letter} is your letter.')
    catergories = ['Movie', 'Author', 'Things That Make You Smile', 'Items in an Office', 'Insects', 'Food', 'Expensive Items', 'Gifts', 'Vegetable', 'Four letter word']
       
    for o in range(10):
        catergory_current = random.choice(catergories)
        catergories.remove(catergory_current)
        word = input(f'Name a word sarting with {letter} that relates to {catergory_current}\n')
        score+=1
        if word == 'skp':
            score-=1
        if timeout < time.time() or len(catergories) == 0:
            print(f"\n {score} was your score!")
            quit()
            
            
# Useful link: https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time