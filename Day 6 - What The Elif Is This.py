# Day 6 of the 100 Days of Python with Replit.com

""" The elif command (which stands for 'elseif') allows you to ask 2, 3, 4 or 142 questions using the same input! This command must be in a certain place. You can have as many elif statements as you want, but they must go in between if and else and have the same indentation. The print statements in your elif command need to line up with the indent of the other print statements."""

# Example 1

print("SECURE LOGIN")
userName = input("Please enter the username: ")
if userName == "toor":
  print("Welcome, " + userName)
elif userName == "root":
  print("Welcome back, greatest sysadmin ever!")
else:
  print("Go away!")
