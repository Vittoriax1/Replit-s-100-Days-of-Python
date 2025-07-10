# This is the input command -ie. user input. This doesnt do anything
input("What is your name? ")

# This is asking for user input and then outputting the input. 
myName = input("What is your name? ")
print("Hello, " + myName)

# The programming challenge is for the program to get to know the user. It needs to ask for a person's name, favorite food, favorite music, and where the live.
print("Getting to know you")
print()
userName = input("What is your name? ")
faveFood = input("What is your favorite food? ")
faveMusic = input("What is your favorite music? ")
whereLive = input("Where do you live? ")
print("Welcome," + userName + " from " + whereLive + ". I also like to eat " + faveFood + " while listening to " + faveMusic "!")
