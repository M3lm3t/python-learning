
name = input ("What is your name? ")

#Remove whitespace and capatlise string
name = name.strip().title()

#Spilt users name into first and last name
first_name, last_name = name.split(" ")

#Greet User
print(f"Hello, {first_name}!")

