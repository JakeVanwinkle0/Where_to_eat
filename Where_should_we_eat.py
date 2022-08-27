import random 

# Creating a function that takes a mood as an input and returns a style of food to get from it
# Use the intergers stored in places_we_want_to_try to list new resturants you and your partner want to try!
dict_of_foods = {"Comf":"American, Chinese or Italian", "Adven":"Indian or Greek", "NS":"It's a Chipotle Angle", "OF":"Trappers, Burch or Order Pizza"}
places_we_want_to_try = [1,2,3,4,5,6]

"""
    Arugments for Where_to_eat to choose from are Comfort food, Adventerous, Not sure, Somwhere new and Old Favorite
"""

def Where_to_eat():
    input1 = input("What are you in the mood for?\n")
    if input1 == "Comfort food":
        print(dict_of_foods["Comf"])
    if input1 == "Adventerous":
        print(dict_of_foods["Adven"])
    if input1 == "Not sure":
        print(dict_of_foods["NS"])
    if input1 == "Old Favorite":
        print(dict_of_foods["OF"])
    if input1 == "Somewhere new":
        print(random.choice(places_we_want_to_try))

Where_to_eat()
