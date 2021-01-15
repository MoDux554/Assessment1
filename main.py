import time

inventory = {}

health = 20 #if it reaches 0 the it is game over

hunger = 0 #if it reaches 10 the health begins to reduce gradually


Restore = ""
Yes = ["y", "Y", "yes", "Yes"]
No = ["n", "N", "no", "No"]
Confirm = ["a", "A"]
LMR = ["Left", "Middle", "Right"]
Fight = ["Fight", "fight", "f", "F"]
Run = [ "Run", "run", "r", "R"]
OpenInventory = ["I", "i,"]

valueChange = 0

Event = 0

print(".")
time.sleep(2)
print("..")
time.sleep(2)
print("...")



def FightOptions():
   global usr_input
   while True:
        usr_input = input("Fight/Run:")
        if usr_input in Fight:
            break
        elif usr_input in Run:
            break
        else:
            continue


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
        health -= 1

    if Event == "Middle Door":
         health -= 3
         print("3 damage was dealt!")
         print("(Health remaining):", health)

def RestoreHP():
    global health

    if health > 20:
        health = 20 #this allows the player to restore their HP back to just 20 and not above it
        print("Health:", health)
    else:
        health +=5
        print("Health:", health)

def UseItems():

   print(inventory)
   while True:
       select_item = input("Input an item or press the B button to close the inventory")
       if select_item in inventory:
           if select_item == "Med Kit":
               print("This will restore 5HP. Do you want to use it?")
               Restore = input(":")
               if Restore in Yes:
                   RestoreHP()
                   break



def AddToInventory(): #Adds things the player picks up during the game into the inventory, these correspond
                       #to the "events" the player is in.
    if Event == 0:
        inventory["Sticks"] = 5
        print("The bunch of sticks were added to the inventory")
        print(inventory)

    elif Event == 1:
        # The torch is added here so that more can be added to it from the user input
        inventory["Torch"] = 0
        global valueChange #this variable is referenced outside of the PlayerInventory function
        while True:
            try:
                valueChange = int(input("How many of your sticks would you like to light up?"))
                if valueChange <=5 and valueChange >=1:
                    inventory["Sticks"] -= valueChange
                    inventory["Torch"] += valueChange
                    print(inventory)
                    break
                else:
                    print("Please enter in a number between 1 and 5") #occurs when the player enters a number less than one or more than #5
                    continue
            except ValueError:
                print("please enter in a number")

    elif Event == "Middle Door":
        print("the Skeleton Lance was added to your inventory.")
        inventory["Skeleton Lance"] = 10
        print("Your torch has run out!")
        inventory["Torch"] -= 1
        print(inventory)

    elif Event == "AfterSkeletonFight":
        inventory["Med Kit"] = 5
        print("The Med Kit was added to your inventory.")
        print(inventory)



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
        AddToInventory()
        Event = 1

    elif Event == 1:
        print("'Oh I think I see some fire there, maybe I can make a couple of torches?'")
        OptionsConfirm()
        AddToInventory()
        Event = 2

    elif Event == 2:
        print("I used one of the torches to look around my surrondings again, until I found the exit of this room")
        OptionsConfirm()
        print("'Yes! A way out!'")
        print("I then left the room without looking back. Outside was a corridor. And in front were 3 doors ")
        OptionsConfirm()
        Event = "Door Choice"

    elif Event == "Door Choice":
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
        print("'You can't wrong with the middle door' I thought to myself.")
        OptionsConfirm()
        print("I walked through and nothing at first seemed conspicuous. That was until... I came across a pile of bones and a skull.")
        OptionsConfirm()
        print("'Wh-What...?'")
        OptionsConfirm()
        print("I didn't have much time to think more about what I was seeing as the bones and skull began to move, they rearranged themselves until it resembled an actual body.")
        OptionsConfirm()
        print("Once that was complete, the skeleton took notice of my presence and started to run at me!")
        OptionsConfirm()
        print("'What should I do?!'")
        time.sleep(1.5)
        FightOptions()
        if usr_input in Fight:
            print("'Here goes nothing!' Gripping the torch tightly I swiped the flame at the alive skeleton./n/"
                  "the flames made contact with the skeleton for a brief moment.")
            OptionsConfirm()
            print("In retaliation, the skeleton swipped its hand at me, their claws slashed against my side once")
            PlayerStatsBehaviour()
            OptionsConfirm()
            print("""Dismissing the pain burning in my side I swiped the torch at it again, aiming for the head this time
            around. The head was reduced to nothing but ash, causing the rest of the body to collapse into a heap of bones.""")
            OptionsConfirm()
            AddToInventory()
            Event = "AfterSkeletonFight"

        elif usr_input in Run:
            print("'I don't think fighting that thing is such a good idea!' And with that I ran away.")
            OptionsConfirm()
            print("""I ended up back in the hall way and tried to catch my breath. It didn't seem like
             the skeleton was pursuing me anymore. """)
            Event = "Door Choice"
    elif Event == "AfterSkeletonFight":
        print("I walked on some more until I came across another object on the ground")
        OptionsConfirm()
        print("'Looks like a first aid, this will be helpful, my side is still hurting after that encourer with the skeleton.'")
        AddToInventory()
        print("""If you want to open up the inventory, press the I button on your keyboard. This way you will be able to use items to restore your HP.
        Why don't you try it now?""")
        usr_input = input(":")
        if usr_input in OpenInventory:
            UseItems()
            Event = "Next"

    elif Event == "Next":
        print("this is the next event")
        break