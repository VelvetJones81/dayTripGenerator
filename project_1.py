# Day Trip Generator
#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.
#(5 points): As a user, I want a destination to be randomly selected for my day trip.
#(5 points): As a user, I want a restaruant to be randomly selected for my day trip.
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don't like one.
#(10 points): As a user, I want to be able to confirm that my  day trip is "complete" once I like all of the random selections.
#(10 points): As a user, I want to display my completed trip in the console.
#(5 points): As a developer, I want all of my funtions to have a Single Responsibility. Remember, each function should do just one thing!

import random

destinations = ['Bikini Bottom', 'Townsville', 'International Space Station', 'Stormwind', 'Silvermoon City'  ]
list_of_restaurants = ["Krusty Krab", "Good Burger", "Soul Food Cafe", "Chuck E. Cheese", "Tiana's Palace"]
modes_of_transportation = ['Rickshaw', 'Train', "Bicycle", 'Horse & Buggy', 'Walking' ]
list_of_entertainment = ['Criminal Activity', 'Jellyfishing', 'General Hooliganism', 'Go to a museum', 'Poke a bear']

def display_greeting():
    print('Welcome to the day trip generator, where your trip will be planned out for you.')

def select_random_destination(destinations):
    random_destination = random.choice(destinations)
    print(f'We have selected {random_destination} for you!')
    answer = input('Does this selection work for you? [y/n]: ')
    while answer == 'n':
        random_destination = random.choice(destinations)
        print(f"Sorry that destination doesn't work for you, how about {random_destination}?")
        answer = input('Does this selection work for you? [y/n]: ')
    if answer == 'y':
        print(f"Awesome! We got that selected for you. Let's keep going!")
    return random_destination
def select_random_restaurant(list_of_restaurants):
    random_restaurant = random.choice(list_of_restaurants)
    print(f'We have selected {random_restaurant} for your dining needs!')
    answer = input('Does this selection work for you? [y/n]: ')
    while answer == 'n':
        random_restaurant = random.choice(list_of_restaurants)
        print(f"Sorry that restaurant doesn't work for you, how about {random_restaurant}?")
        answer = input('Does this selection work for you? [y/n]: ')
    if answer == 'y':
        print(f"Sweet! We got that selected for you. Bon Apetit! Let's keep going!")
    return random_restaurant
def select_random_entertainment(list_of_entertainment):
    random_entertainment = random.choice(list_of_entertainment)
    print(f'We have selected {random_entertainment} for you to enjoy!')
    answer = input('Does this selection work for you? [y/n]: ')
    while answer == 'n':
        random_entertainment = random.choice(list_of_entertainment)
        print(f"Sorry that entertainment doesn't work for you, how about {random_entertainment}?")
        answer = input('Does this selection work for you? [y/n]: ')
    if answer == 'y':
        print(f"Glorious! I hope you have a wonderful time! Let's keep going!")
    return random_entertainment
def select_random_transportation(mode_of_transportation):
    random_transportation = random.choice(mode_of_transportation)
    print(f'We have selected {random_transportation} for your mobile needs!')
    answer = input('Does this selection work for you? [y/n]: ')
    while answer == 'n':
        random_transportation = random.choice(mode_of_transportation)
        print(f"Sorry that transportation doesn't work for you, how about {random_transportation}?")
        answer = input('Does this selection work for you? [y/n]: ')
    if answer == 'y':
        print(f"Perfect! Now you can move around while you're there. Let's keep going!")
    return random_transportation
def trip_comfirmation(destination, transportation, entertainment, restaurant):
    print('------------------------------------------------------------------')
    print(f'You will be going to {destination}.') 
    print(f'Where you will be traveling by {transportation}.')
    print(f'While you are there you will be eating at {restaurant}') 
    print(f'And you will be partaking in {entertainment} for your enjoyment')
    print('------------------------------------------------------------------')
    answer = input('Does this itenerary work for you? [y/n]: ')
    if answer == 'y':
        print('Have an amazing trip. Thank you for using our Random Day Trip Generator!')
    elif answer == 'n':
        run_day_trip
def run_day_trip():
    display_greeting()
    confirmed_destination = select_random_destination(destinations)
    confrimed_transportation = select_random_transportation(modes_of_transportation)
    confirmed_entertainment = select_random_entertainment(list_of_entertainment)
    confirmed_restaurant = select_random_restaurant(list_of_restaurants)
    trip_comfirmation(confirmed_destination, confrimed_transportation, confirmed_entertainment, confirmed_restaurant)

run_day_trip()

