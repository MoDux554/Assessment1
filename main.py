##IDEAS FOR TEXT BASED ADVENTURE
##You are currently sealed off in an alternative dimension,
##The dimension is home to alien creature, their weakness is...

#REQUIRED: Inventory, different paths which affect the outcome of the game

import time

Event = 0



print(".")
time.sleep(2)
print("..")
time.sleep(2)
print("...")

while True:
    event = 0
    usr_input = str(input("Press A to wake up"))
    if usr_input == "A" or usr_input == "a":
        print("Nghh...")
        time.sleep(1)
        print("My head... where I am..?")
        print(" 'I took in my surroundings while  ")
        break

    elif usr_input != "A" or usr_input !="a":
        continue


