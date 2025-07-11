# Day 3 of the 100 Days of Python with Replit.com

# This is mad-libs type of challenge. The challenge asks you to ask your users to list a bunch of information about them: 
# things they like, things they hate, names of family and friends... it's up to you how many and what kinds of things you pick. Keep it wacky!

# I think I am going to use a story from a mad libs site.

userName = input("Please enter your name to begin this story: ")
print()
print("Welcome", userName, ", let's get some information from you first so we can create a story.")

# Getting user input for mad libs
things = input("Please enter the plural version of a thing: ")
adjective = input("Please enter an adjective: ")
songTitle = input("Please enter the name of a song: ")
celeb = input("Please enter the name of a famous person: ")
feeling = input("Please enter a feeling: ")
verb = input("Please enter a verb: ")
place = input("Please enter the name of a special place: ")
food = input("Please enter the name of a favorite type of food: ")
things2 = input("Please enter the plural version of a different thing: ")
person = input("Please enter the name of a person: ")

print()
print("Here is your story, ",userName)
print()
print("I just got back from a pizza party with", person, ". Can you believe")
print("we got to eat", adjective, "pizza in", place, "?!?! Everyone got")
print("to choose their own toppings. I made", person, "a", things, "pizza, which is")
print("my favorite! They even stuffed the crust with", things2, ". How", feeling, "!")
print("If that wasn't good enough already,", celeb,"was there singing", songTitle,".")
print("I was so inspired by the music, I had to get up out of my seat and", verb,"!")
