print("To create a table for a y = mx + b equation, answer the questions below:")
m = float(input("what is the slope of the line:"))
m = round(m, 5)
b = float(input("what is the y-intercept of the line:"))
b = round(b,)
print(f"y = {m}x + {b}")
print("x | y")
x = 0
print(f"0 | {b}")
for o in range(10):
    x = x + 1
    mx = m * x
    y = mx + b
    print(f"{x} | {y}")
