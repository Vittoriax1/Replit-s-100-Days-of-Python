# Day 8 of the 100 Days of Python with Replit.com

""" Today's focus is using all the skills you have learned so far:

input and output
concatenation
if statements
nested if statements
Build a custom affirmations generator to give the user a customized affirmation each day of the week. """

# Introduction

intro = "Wholesome Positivity Machine"
print(intro)
print("-" * 40)

# Ask the user for some information
# Extra challenge - standardize lettering for words

userName = input("What is your name? ").capitalize()
goal = input(userName + ", what is your goal? ").lower()
dayWeek = input("What day of the week is it, " + userName + "? ").lower()

# Ifs/Elifs/etc. - Honestly, I didn't want to type a lot here
if dayWeek == "monday":
  question = input("How do you feel today? <good/bad> ").lower()
  if question == "good":
    print("Well, " + userName + ", it\'s only Monday, but it\'s a great start to the week!")
  else:
    print("Well, " + userName + ", the week will definitely get better.")
elif dayWeek == "tuesday":
  print(userName + ", you will get a chance to enjoy " + goal + ". Do so with gusto, you beast.")
elif dayWeek == "wednesday":
  print("It\'s hump day, " + userName +". What are doing to keep going strong with " + goal + "?")
elif dayWeek == "thursday":
  print(userName + ", today is a most glorius day. You are special to me.")
elif dayWeek == "friday":
 print("Something, something, something. You are close to achieving " + goal + "!")
elif dayWeek == "saturday":
  print("It\'s the weekend. Get outside and spend the day in the sun.")
elif dayWeek == "sunday":
  print("Well, the week is almost over, but next week will be even better than this week!")
else:
  print("That\'s not a real day.  It must be a rough day, " + userName + ". I\'m so sorry. Just remember to keep your head up - you\'ve got this!")
