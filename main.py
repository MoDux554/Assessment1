##IDEAS FOR TEXT BASED ADVENTURE
##You are currently sealed off in an alternative dimension,
##The dimension is home to alien creature, their weakness is...

#Write some pseudocode in tandum with the actual code!

#REQUIRED:
#inventory - done using a function, includes either a dictionary, list, or tuple or a combination of the three#the
#the inventory function should be called whenever the player finds something new to add, a weapon breaks, or if they
#want to open up the inventory themselves(OPTIONAL)
#if player picks up something i is added in the inventory
#checks for which scene the player is in when picking up an item

import time

inventory = {}

Event = 0



print(".")
time.sleep(2)
print("..")
time.sleep(2)
print("...")



def PlayerInventory():
    if Event == 0:
        inventory["Stick"] = 5
        print("The stick was added to the inventory")
        print(inventory)


while True:
    if Event == 0:
        usr_input = str(input("Press A to wake up"))
        if usr_input == "A" or usr_input == "a":
            print(" 'Nghh...' ")
            time.sleep(1)
            print(" 'My head... where I am..?' ")
            usr_input = input("I took in my surroundings as my consciousness slowly reformed. Right next to me was "
                              "a stick on the ground" '(pick up? y/n)')

            if usr_input == "y":
                PlayerInventory()
            break

        elif usr_input != "A" or usr_input !="a":
            continue

