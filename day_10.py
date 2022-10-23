# Learning Python
# GDSC 30 days challenge

import random

# 1- Capital Quiz

NI_States = {'Abia State' : 'Umuahia',
'Adamawa State' :	'Yola',
'Akwa Ibom State' :	'Uyo',
'Anambra State' :	'Awka',
'Bauchi State':	'Bauchi',
'Bayelsa State' :	'Yenagoa',
'Benue State' :	'Makurdi',
'Borno State' :	'Maiduguri',
'Cross River State' :	'Calabar',
'Delta State' :	'Asaba',
'Ebonyi State' :	'Abakaliki',
'Edo State' :	'Benin City',
'Ekiti State' :	'Ado-Ekiti',
'Enugu State' :	'Enugu',
'Federal Capital Territory' :	'Abuja',
'Gombe State' :	'Gombe',
'Imo State' :	'Owerri',
'Jigawa State' :	'Dutse',
'Kaduna State' :	'Kaduna',
'Kano State' :	'Kano',
'Katsina State' :	'Katsina',
'Kebbi State' :	'Birnin Kebbi',
'Kogi State' :	'Lokoja',
'Kwara State' :	'Ilorin',
'Lagos State' :	'Ikeja',
'Nasarawa State' :	'Lafia',
'Niger State' :	'Minna',
'Ogun State' :	'Abeokuta',
'Ondo State' :	'Akure',
'Osun State' :	'Oshogbo',
'Oyo State' :	'Ibadan',
'Plateau State' :	'Jos',
'Rivers State' :	'Port Harcourt',
'Sokoto State' :	'Sokoto',
'Taraba State' :	'Jalingo',
'Yobe State' :	'Damaturu',
'Zamfara State' :	'Gusau'}

state_list = []

for key in NI_States:
    state_list.append(key)

i = 0
j = 0

while ((i + j) != 36):
    random_state = random.choice(state_list)
    user_ans = input(f"What is the capital of {random_state} in Nigeria ? : ")

    if (user_ans.lower() != NI_States[random_state].lower()) :
        print("Incorrect answer !")
        i = i + 1
    else :
        print("Correct answer !")
        j = j + 1
    state_list.remove(random_state)

print(f"In the 36 states you found {j} correct capitals and {i} incorrect capitals.\n")

# 2- GALILEAN MOONS OF JUPITER

moon_name = ['Io', 'Europa', 'Ganymede', 'Callisto']
moon_mean_radius = {'Io' : '1821.6', 'Europa' : '1560.8', 'Ganymede' : '2634.1', 'Callisto' : '2410.3'}
moon_surface_gravity = {'Io' : '1.796', 'Europa' : '1.314', 'Ganymede' : '1.428', 'Callisto' : '1.235'}
moon_orbital_period = {'Io' : '1.769', 'Europa' : '3.551', 'Ganymede' : '7.154', 'Callisto' : '16.689'}

user_input = input("Enter the name of a Galilean moon of Jupiter then I will display the moon’s mean radius, surface gravity, and orbital period : ")

for name in moon_name :
    if user_input.lower() == name.lower() :
        print(f"Moon name : {name}\nMeans Radius : {moon_mean_radius[name]}\nSurface Gravity : {moon_surface_gravity[name]}\nOrbital Period : {moon_orbital_period[name]}\n")
if (user_input.lower() != moon_name[0].lower() and user_input.lower() != moon_name[1].lower() and user_input.lower() != moon_name[2].lower() and user_input.lower() != moon_name[3].lower()) :
    print("The moon name you've enterred does not exist in the list !")
