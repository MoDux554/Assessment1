import time

inventory = {}

health = 20 #if it reaches 0 the it is game over

hunger: 0 #if it reaches 10 the health begins to reduce gradually

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



def PlayerStatsBehaviour():
    global hunger
    global health

    if hunger == 10:
        health =- 1


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
                    print("Please enter in a number between 1 and 5") #occurs when the player enters a number less than one or more than #5
                    continue
            except ValueError:
                print("please enter in a number")



while True: #This is where all the events of the game play out
    if Event == 0:
        usr_input = str(input("Press A to wake up"))
        if usr_input in Confirm:
            print(" 'Nghh...' ")
            time.sleep(2)
            print(" 'My head... where I am..?' ")
            time.sleep(2)
            print("""I took in my surroundings as my consciousness slowly reformed.
            It seems that I am in a dark room, there is no window so I can't tell
            what the time is. The room itself is mostly dark. Looking down  I see
            a bunch of sticks lying around, which I picked up""")
            usr_input = input("Press A")
            if usr_input in Confirm:
                PlayerInventory()
                Event = 1
            else:
                continue
        else:
            continue #if the user inputs anything that is not in confirm the statement will repeat


    if Event == 1:
        print("'Oh I think I see some fire there, maybe I can make a couple of torches?'")
        usr_input = input("Press A")
        if usr_input in Confirm:
            PlayerInventory()
            Event = 2
        else:
            continue

    if Event == 2:
        print("After making some torches I looked around some more until I found the exit of this room")
        usr_input = input("Press A")
        if usr_input in Confirm:
            print("'Yes! A way out!'")
            break
        else:
            continue


