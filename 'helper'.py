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