import time

inventory = {}

health = 20 #if it reaches 0 the it is game over

hunger: 0 #if it reaches 10 the health begins to reduce gradually

Yes = ["y", "Y", "yes", "Yes"]
No = ["n", "N", "no", "No"]
Confirm = ["a", "A"]
LMR = ["Left", "Middle", "Right"]

valueChange = 0

Event = 0

print(".")
time.sleep(2)
print("..")
time.sleep(2)
print("...")



def OptionsConfirm(): #this function is called upon everytime the player is asked to input the A button to continue dialouge
    global usr_input
    while True:
        usr_input = input("Press A")
        if usr_input in Confirm:
            break
        else:
            continue




def PlayerStatsBehaviour():
    global hunger
    global health

    if hunger == 10:
        health =- 1


def PlayerInventory(): #Adds things the player picks up during the game into the inventory, these correspond
                       #to the "events" the player is in.
    if Event == 0:
        inventory["Sticks"] = 5
        print("The bunch of sticks were added to the inventory")
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
        OptionsConfirm()
        print(" 'Nghh...' ")
        time.sleep(2)
        print(" 'My head... where I am..?' ")
        time.sleep(2)
        print("""I took in my surroundings as my consciousness slowly reformed.
                        It seems that I am in a dark room, there were no window so I couldn't tell
                        what the time was. The room itself was mostly dark. Looking down  I saw
                        a bunch of sticks lying around, which I picked up""")

        OptionsConfirm()
        PlayerInventory()
        Event = 1

    if Event == 1:
        print("'Oh I think I see some fire there, maybe I can make a couple of torches?'")
        OptionsConfirm()
        PlayerInventory()
        Event = 2

    if Event == 2:
        print("I used one of the torches to look around my surrondings again, until I found the exit of this room")
        OptionsConfirm()
        print("'Yes! A way out!'")
        print("I then left the room without looking back. Outside was a corridor. In front were 3 doors ")
        OptionsConfirm()
        print("'Hmmm, which door to take?'")
        time.sleep(2)
        usr_input = input("Left/Middle/Right? :")
        if usr_input in LMR:
            if usr_input == "Left":
                Event = "Left Door"
            elif usr_input == "Right":
                Event = "Right Door"
            elif usr_input == "Middle":
                Event = "Middle Door"
        else:
            continue



    elif Event == "Left Door":
        print("I went through the left door")
        break
    elif Event == "Right Door":
        print("I took the door on the right")
        break
    elif Event == "Middle Door":
        print("'You can't wrong with the middle door' I thought to myself")
        break



