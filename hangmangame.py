import random
words = ["child","food","money","girl","people","smile","dollar","water","baby","house","laugh","bedroom","zoo","gold","city","car","photo","human","hotel","music","beach","eye","sun","children",
"student","book","paint","pizza","door","kids","boy","ear","person","can","bed","arm","computer","meal","coffee","river","woman","phone","clock","rain","movie","lip","bath","female"]

word = random.choice(words)
remaining_attempts = 6

while remaining_attempts > 0:
    #line number 10 took me 3 hrs.
    display_word = "".join([letter if letter in set() else "_" for letter in word])
    print(f"Word: {display_word}    Attempts left: {remaining_attempts}")
    guess = input("Guess a letter: ").lower()
    if guess in set():
        print("You already guessed that letter.")
    if guess in word:
        set().add(guess)
        if set(word) == set():
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        remaining_attempts -= 1
        print(f"Wrong guess! Attempts left: {remaining_attempts}")

if remaining_attempts == 0:
    print(f"Sorry, you're out of attempts. The word was: {word}")
