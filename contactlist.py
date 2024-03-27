while True:
    c = input("would you like to create a new contact?")
    if c == 'no' or c == 'No' or c == 'Nah' or c == 'nah' or c =='No thanks' or c == 'No Thanks'  or c == 'no Thanks' or c == 'no thanks' or c == 'No Thank You' or c == 'No thank you' or c == 'no thank you':
        quit()
    con = input("what would you like to call your contact?")
    pnum = input("what is their phone number?")
    adress = input("what is their home adress?")
    info = (f"{con}'s phone number is {pnum} and they live at {adress}.")
    print(info)
    print(" ")
    continue