while True:
    wanttoplay = input("Do you want to play Rock Paper Scissors?")
    if wanttoplay == 'no' or wanttoplay == 'No' or wanttoplay == 'n' or wanttoplay == 'N':
        quit()
        
    import numpy as np
    rock, paper, scissors = ["rock", 'paper', 'scissors']
    moves = [rock, paper, scissors]
    attack = np.random.choice(moves) 
    defense = input("write 'rock', 'paper', or 'scissors' to move (remember to write in lowercase):")

    rock > scissors
    scissors > paper
    paper > rock
    
    if defense > attack:
        print('Congrats, you won!')
    if defense < attack:
        print ('Sorry, you lost.')
    if defense == attack:
        print('it was a tie, try again')
    