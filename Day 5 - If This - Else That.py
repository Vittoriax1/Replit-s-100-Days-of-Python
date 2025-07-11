# Day 5 of the 100 Days of Python with Replit.com

# This lesson is about 'if' statements.

# Example 1
myName = input("What is your name? ")
if myName == "Name":
  print("Hello " + myName + ", welcome back!")
else:
  print("Hello, " + myName)

# Example 2
anotherEx = input("Hi there! What is your name? ")
if anotherEx == "jenn":
  print("Welcome back, " + anotherEx + "! You are the noobest coder ever.")
else:
  print(anotherEx + ", it's nice to meet you.")

# Day 5 Challenge: Build a Which Character Are You? Game?

print("Which Harry Potter character are you?")
print()
print("-" * 60)
print()

loyal = input("Q1. Do you feel like you can understand snakes? ")
if loyal == "yes":
  print("Then you might be Harry Potter!")
else:
  study = input("Q2. Do you like to study? ")
  if study == "yes":
    print("Then you might be Heromine Granger!")
  else:
   siblings = input("Q3. Do you have more than 2 siblings? ")
  if siblings == "yes":
     print("Then you might be Ron Weasley!")
