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

destinations = ['New York City', 'Berlin', 'Amsterdam', 'Tokyo', 'Barcelona']
restaurants_new_york_city = ["Delmonico's", "Lombardi's", 'Keens Steakhouse', 'The Rainbow Room', "Katz's Delicatessen"]
restaurants_berlin = ['Skykitchen', 'Hasty Pastry', 'Burger Turm', 'Hackethals', 'Sapori di Casa']
restaurants_amsterdam = ['Baaz Amsterdam', 'The Pantry', 'Chez Lorraine', 'Restaurant Bougainville', 'Ta Toru']
restaurants_tokyo = ['Gyopa Gyoza Roppongi', 'Jiromaru Akihabara', 'Ise Sueyohsi', 'Han no Daidokoro Honten', 'Ninja Shinjuku Ajito']
restaurants_barcelona = ['BelleBuon', 'La Pasta Lab', 'Bodega Biarritz', 'Locavore Barcelona', 'Sumac & Mambo']
modes_of_transportation = ['Rental Car', 'Train', "Bicycle", 'Taxi', 'Walking' ]
list_of_entertainment_new_york_city = ['Showtime at the Apollo', 'Manhattan Sky Tour', '9/11 Ground Zero Tour','One World Observatory', 'Times Square'  ]
list_of_entertainment_berlin = ['Love Parade', 'Berlin Icebar Experience', 'Cosmic Comedy Club', 'Tresor', 'Sachsenhausen Concentration Camp Memorial Tour']
list_of_entertainment_amsterdam = ['Red Light District', 'Anne Frank House', 'Vondelpark', "CoffeeShops", 'Heineken Experience' ]
list_of_entertainment_tokyo = ['Climb Mt. Fuji', 'Fight Ninjas', 'Tokyo Disney', 'Otaku Tour', 'Tokyo Tower']
list_of_entertainment_barcelona = ['Running of the Bulls','Beaches', 'Tapas and Wine Experience', 'CosmoCaxia', 'Erotica Museum of Barcelona' ]

print('Welcome to the day trip generator, where your trip will be planned out for you.')

def select_entertainment(list_of_entertainment_new_york_city):
        random_entertainment = random.choice(list_of_entertainment_new_york_city)
        print(f'We have selected {random_entertainment} for your enjoyment!')
        answer = input('Does this selection work for you? [y/n]: ')
        while answer == 'n':
            random_entertainment = random.choice(list_of_entertainment_new_york_city)
            print(f"Sorry that destination doesn't work for you, how about {random_entertainment}?")
            answer = input('Does this selection work for you? [y/n]: ')
        if answer == 'y':
            print(f'Glorious! Have a great time!')
        return random_entertainment

def select_random_restaurant(restaurants_new_york_city):
        random_restaurant = random.choice(restaurants_new_york_city)
        print(f'We have selected {random_restaurant} for your dining needs!')
        answer = input('Does this selection work for you? [y/n]: ')
        while answer == 'n':
            random_restaurant = random.choice(restaurants_new_york_city)
            print(f"Sorry that destination doesn't work for you, how about {random_restaurant}?")
            answer = input('Does this selection work for you? [y/n]: ')
        if answer == 'y':
            print(f'Sweet! Very nice choice. Bon Apetit!')
        return random_restaurant

def select_random_restaurant(restaurants_berlin):
        random_restaurant = random.choice(restaurants_berlin)
        print(f'We have selected {random_restaurant} for your dining needs!')
        answer = input('Does this selection work for you? [y/n]: ')
        while answer == 'n':
            random_restaurant = random.choice(restaurants_berlin)
            print(f"Sorry that destination doesn't work for you, how about {random_restaurant}?")
            answer = input('Does this selection work for you? [y/n]: ')
        if answer == 'y':
            print(f'Sweet! Very nice choice. Bon Apetit!')
        return random_restaurant

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
random_destination = select_random_destination(destinations)
if random_destination == 'New York City':
        select_random_restaurant(restaurants_new_york_city)
elif random_destination == 'Berlin':
        select_random_restaurant(restaurants_berlin)
elif random_destination == 'Barcelona':
        select_random_restaurant(restaurants_barcelona)
elif random_destination == 'Amsterdam':
        select_random_restaurant(restaurants_amsterdam)
else:
        select_random_restaurant(restaurants_tokyo)


select_random_destination(destinations)
select_random_restaurant(restaurants_new_york_city)
select_random_restaurant(restaurants_berlin)
select_random_restaurant(restaurants_amsterdam)
select_random_restaurant(restaurants_barcelona)
select_random_restaurant(restaurants_tokyo)
select_entertainment(list_of_entertainment_new_york_city)
select_entertainment(list_of_entertainment_amsterdam)
select_entertainment(list_of_entertainment_barcelona)
select_entertainment(list_of_entertainment_berlin)
select_entertainment(list_of_entertainment_tokyo)


