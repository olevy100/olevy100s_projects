#alphabetical order
print("Hello, I am the sorting bot. To try me out, type some words, and I'll sort them alphebetically")
print(" ")
wrd_input = input("Enter words separated by spaces, press enter when you're done: ")
words = wrd_input.split()
sorted_words = sorted(words)
print("Sorted words:", *sorted_words)

print(" ")

#numerical order
print("How about I sort some number in numerical order for you now?")
user_input = input("Enter a list of numbers separated by spaces, when you are done, press enter. ")
numbers = [int(num) for num in user_input.split()]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", *sorted_numbers)

