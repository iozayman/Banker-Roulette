import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ").lower()
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = [name.capitalize() for name in names]
le = len(names)-1 
chosen = names[random.randint(0, le)]

print(f"{chosen} is going to buy the meal today!")
