# Day 6 of the 100 Days of Python with Replit.com

""" The elif command (which stands for 'elseif') allows you to ask 2, 3, 4 or 142 questions using the same input! This command must be in a certain place. You can have as many elif statements as you want, but they must go in between if and else and have the same indentation. The print statements in your elif command need to line up with the indent of the other print statements."""

# Example 1

print("SECURE LOGIN")
print("+" * 10)
userName = input("Please enter the username> ")
password = input("Please enter the password> ")
if userName == "toor" and password == "toor":
  print("Welcome, " + userName)
elif userName == "root" and password == "root":
  print("Welcome back, greatest sysadmin ever!")
else:
  print("Go away!")

# Challenge: Basically like the example. You must include 3 users and the else command for all others.

print("SECURE LOGIN")
print("+" * 10)
userName = input("Please enter the username> ")
password = input("Please enter the password> ")
if userName == "toor" and password == "toor":
  print("Welcome, " + userName)
elif userName == "root" and password == "root":
  print("Welcome back, greatest sysadmin ever!")
elif userName == "admin" and password == "Passw0rd!":
  print("Oh admin, my admin. Welcome back.")
else:
  print("Go away!")
