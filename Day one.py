input = open("Elves_Input.txt") # Load the data

elves_formatted = input.read().split("\n\n") #Split the data on double line break

Elves_calories = [sum(map(int, x.split())) for x in elves_formatted] # Sum each item in list splitting on line break

Elves_calories.sort(reverse=True) # order by descending


Max_Elves_Calories = Elves_calories[0] # Max value

print(Max_Elves_Calories)

Top_3_Elves_Calories = Elves_calories[:3] # Top 3

print(sum(Top_3_Elves_Calories))