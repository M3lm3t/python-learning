#Calculator

x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

#Adding a comma to break up large numbers
print(f"{z:,}")