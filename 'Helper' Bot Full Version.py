print("Hello, I am the helper bot, I can help you with anything, but I excel in banking and money")
print(" ")
print(" ")
def sum(a, b):
    return (a + ' ' + b)
a = input('what is your first name: ')
b = input('what is your last name: ')
g = input('what is your title (Mr, Ms, Dr, etc.):')
print(f'your name is {sum(a, b)}')
h = sum(a, b)
c = sum(g, h)
i = sum(g, b)
print('hello' +' ' + i )
d = input('how can I help you today ' + i + '? Describe what you need in one word.')
if(d == 'banking' or d ==  'Banking' or d == 'money' or d == 'Money'):
    f = input("oh yeah, I'm good at that " + i + ", what do you need specifically?")
    print("I'm sorry, I can't help you with " + f + ". It's quittin' time for me. Try speaking to my manager tommorow.")
else: 
    e = input('how can I help you with ' + d)
    print("sorry, I cannot help you with that yet, I haven't been programmed for it.")
    print(':/')

    boy = ['John', 'Paul', 'George', 'Ringo', 'Oren', "Liam", "Noah", "Oliver", "James", "Elijah", "William", "Henry", "Lucas",
    "Benjamin","Theodore","Mateo","Levi","Sebastian","Daniel","Jack","Michael","Alexander","Owen","Asher","Samuel","Ethan","Leo"
    "Jackson","Mason","Ezra","John","Hudson","Luca","Aiden","Joseph","David","Jacob","Logan","Luke","Julian","Gabriel","Grayson",
    "Wyatt","Matthew","Maverick","Dylan", "Greyson","Rowan","Adam","Nicholas","Theo", "Xavier","Hunter","Dominic","Jace","Gael",
    "River","Thiago","Kayden","Damian", "August", "Carson", "Austin", "Myles","Seok-yeol" ]
    girl= [ "Olivia", "Emma", "Charlotte", "Amelia", "Sophia", "Isabella", "Ava", "Mia","Evelyn","Luna","Harper",
    "Camila","Sofia","Scarlett","Elizabeth","Eleanor","Emily","Anna","Iris","Bella","Eloise", "Skylar","Jade","Gabriella",
    "Ariana","Maria", "Jeong-un"]
    last = ["Starr","Lennon", "McCartney", "Harrison", "Levy", "Yun", "Kim",  "Smith ", "Johnson", "Williams", "Brown", "Jones", 
    "Miller", "Davis ", "Garcia " , "Rodriguez ", "Wilson ", "Martinez ", "Anderson ", "Taylor " , "Thomas " , "Hernandez ", "Moore ",
    "Martin ", "Jackson ", "Thompson ", "White ", "Lopez ", "Lee " , "Gonzales ", "Smith ", "Johnson ", "Williams ", "Jones " , "Brown ",
    "Davis " ]
import numpy as np
print(" ")
print(" ")
print("Hello, I am the random name generator, pleasure to meet you " + c + ".")
j = input("do you want to try me out?")

if (j == 'yes' or j == 'Yes' or j == 'sure' or 'Sure'):
    k = input('do you want to generate a name?')
    if k == 'yes' or k == 'Yes':
     
        l = input("If you would like a girl's name, type 'girl', if you would like a boy's name, type 'boy'")
        if l == "girl" or l == "Girl":
            print('Your new name is ' + np.random.choice(girl) + ' ' + np.random.choice(last) + " I hope that I've helped you, but I have to go now")
        if l == 'boy' or l == 'Boy':
            print('Your new name is ' + np.random.choice(boy) + ' ' + np.random.choice(last) + ". I hope that I've helped you, but I have to go now")
    if (k != 'yes' or k !='Yes'):
        quit()
    if (k == 'no' or k == 'No'):
        quit()
    else: print("goodbye")
    quit()
if j == 'no' or j == "No":
    print("alright, goodbye")
    quit()
else:
    print("alright, goodbye")
    quit()
