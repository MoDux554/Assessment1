import time

inventory = {}

Yes = ["y", "Y", "yes", "Yes"]
No = ["n", "N", "no", "No"]
Confirm = ["a", "A"]

valueChange = 0

Event = 0

print(".")
time.sleep(2)
print("..")
time.sleep(2)
print("...")




def PlayerInventory(): #Adds things the player picks up during the game into the inventory, these correspond
                       #to the "events" the player is in.
    if Event == 0:
        inventory["Sticks"] = 5
        print("The sticks were added to the inventory")
        print(inventory)

    elif Event == 1:
        # The litstick is added here so that more can be added to it from the user input
        inventory["LitStick"] = 0
        global valueChange #this variable is referenced outside of the PlayerInventory function
        while True:
            try:
                valueChange = int(input("How many of your sticks would you like to light up?"))
                if valueChange <=5 and valueChange >=1:
                    inventory["Sticks"] -= valueChange
                    inventory["LitStick"] += valueChange
                    print(inventory)
                    break
                else:
                    print("Please enter in a number between 1 and 5")
                    continue
            except ValueError:
                print("please enter in a number")



while True: #This is where all the events of the game play out
    if Event == 0:
        usr_input = str(input("Press A to wake up"))
        if usr_input in Confirm:
            print(" 'Nghh...' ")
            time.sleep(1)
            print(" 'My head... where I am..?' ")
            usr_input = input("I took in my surroundings as my consciousness slowly reformed. Right next to me were a bunch of sticks "
                              "on the ground" '(pick them up? y/n)')
            if usr_input in Yes:
                PlayerInventory()
                Event = 1
            elif usr_input in No:
                Event = 1
        else:
            continue #if the user inputs anything that is not in the yes,no or confirm lists, the first if statement
                      #wil be repeated


    if Event == 1:
        print("As you walk along, you notice some fire on the wall")
        if "Sticks" in inventory:#checks if the sticks are in the player's inventory system
            usr_input = input("do you want to use your stick to make a torch?")
            if usr_input in Yes:
                PlayerInventory()
                Event = 2
            elif usr_input in No:
                Event = 2
        else:
            print("you have nothing on your person to make a torch")
            Event = 2

    if Event == 2:
        pass