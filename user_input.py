#taking user input
name=input("Enter your name: ")
age = int(input("Enter your age: "))
location=input("Where are you from? ")

#printing user input
print("\nHello, {}!".format(name.title()))
print("You are {} years old.".format(age))
print("You are from {}, aren't you?".format(location.title()))
                