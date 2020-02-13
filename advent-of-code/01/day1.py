# Task summary :
# input -> liste of numbers
# what to do -> divide by 3 rounded down -2, then add up to total
# result -> total

# define a var for total
total = 0

# import du fichier
input = open("fuel_input.txt","r")

# lecture du fichier
input_list = input.readlines()

# Set une var pour enmagasiner le total
mission_fuel_total = 0

for i in input_list :
    fuel = (int(i) // 3) - 2

    while fuel > 0 :
        mission_fuel_total += fuel
        fuel = (fuel // 3) - 2

print(mission_fuel_total)