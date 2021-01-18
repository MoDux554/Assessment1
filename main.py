import time

inventory = {}
Weapons = {}

health = 20 #if it reaches 0 the it is game over

hunger = 0 #if it reaches 10 the health begins to reduce gradually


Restore = ""
Yes = ["y", "Y", "yes", "Yes"]
No = ["n", "N", "no", "No"]
Confirm = ["a", "A"]
LMR = ["Left", "Middle", "Right"]
Fight = ["Fight", "fight", "f", "F"]
Run = [ "Run", "run", "r", "R"]
Close = ["B", "b"]
OpenInventory = ["Item", "I", "i"]

weaponChoice = ""
Round = 0

valueChange = 0

Event = 0

print(".")
time.sleep(2)
print("..")
time.sleep(2)
print("...")



def FightOptions():
   while True:
        if Event == "Middle Door":
            usr_input = input("Fight/Run:")
            if usr_input in Fight:
                break
            elif usr_input in Run:
                break
            else:
                continue

        elif Event == "BattleWithThree":
            Choice = input("What do you want to do? (Fight/Items)")
            if Choice in Fight:
                weaponChoice = int(input("Which weapon do you wish to use? input 1 or 2 to use either the Torch or the Skeleton Lance"))
                print(Weapons)
                if weaponChoice == 1:
                    UsedTorch()
                    break
                elif weaponChoice == 2:
                    UsedSkeletonLance()
                    break
            elif Choice in OpenInventory:
                UseItems()
                break
            else:
                continue


def UsedTorch():
    if Weapons["Torch"] > 0:
     Weapons["Torch"] -= 1
     print(Weapons)

    else:
        print("You no longer have this weapon!")

def UsedSkeletonLance():
    if Weapons["Skeleton Lance"] > 0:
        Weapons["Skeleton Lance"] -= 1
        print(Weapons)

    else:
        print("You no longer have this weapon!")

def OptionsConfirm(): #this function is called upon everytime the player is asked to input the A button to continue dialouge
    global usr_input
    while True:
        usr_input = input("Press A")
        if usr_input in Confirm:
            break
        else:
            continue


def ReduceHunger():
    global hunger
    hunger -= 3
    print("Hunger:", hunger)


def PlayerGetsHungry():
    global hunger
    global health

    hunger += 5
    print("Your stomach growls...")
    print("Hunger:", hunger)

    if hunger == 10:
        health -= 3
        print("Hunger:", hunger)
        print("Health:", health)
    elif hunger > 10:
        hunger = 10
        health -= 3
        print("Hunger:", hunger)
        print("Health:", health)


def PlayerHealthChanges(): #changes to the player's stats during and outside of battle
    global health

    if Event == "Middle Door":
         health -= 3
         print("3 damage was dealt!")
         print("(Health remaining):", health)

    if Event == "BattleWithThree":
        health -= 10
        print("10 damage was dealt!")
        print("(Health remaining):", health)


def RestoreHP():
    global health

    health += 5
    if health > 20:
        health = 20 #this allows the player to restore their HP back to just 20 and not above it
        print("Health:", health)
        inventory["Med Kit"] -=1
        print(inventory)


def UseItems():
   print(inventory)
   while True:
       select_item = input("Input an item or press the B button to close the inventory")
       if select_item in inventory:
           if select_item == "Med Kit":
               MedKit()
           elif select_item == "Plate of Steak":
               Steak()
       elif select_item in Close:
           break
       else:
           continue

def MedKit():
    while True:
        print("This will restore 5 HP, do you want to use it? ")
        Restore = input("Yes/No:")
        if Restore in Yes:
            RestoreHP()
        elif Restore in No:
            break
def Steak():
    while True:
        print("This will reduce your hunger by 3. Do you want to eat it?")
        Restore = input("Yes/No:")
        if Restore in Yes:
            ReduceHunger()
        elif Restore in No:
            break


def AddToInventory(): #Adds things the player picks up during the game into the inventory, these correspond
                       #to the "events" the player is in.
    if Event == 0:
        inventory["Sticks"] = 5
        print("The bunch of sticks were added to the inventory")
        print(inventory)

    elif Event == 1:
        # The torch is added here so that more can be added to it from the user input
        Weapons["Torch"] = 0
        global valueChange #this variable is referenced outside of the PlayerInventory function
        while True:
            try:
                valueChange = int(input("How many of your sticks would you like to light up?"))
                if valueChange <=5 and valueChange >=1:
                    inventory["Sticks"] -= valueChange
                    Weapons["Torch"] += valueChange
                    print(inventory)
                    break
                else:
                    print("Please enter in a number between 1 and 5") #occurs when the player enters a number less than one or more than #5
                    continue
            except ValueError:
                print("please enter in a number")

    elif Event == "Middle Door":
        print("the Skeleton Lance was added to your inventory.")
        Weapons["Skeleton Lance"] = 10
        print("Your torch has run out!")
        UsedTorch()
        print(inventory)

    elif Event == "AfterSkeletonFight":
        inventory["Med Kit"] = 5
        print("The Med Kit was added to your inventory.")
        print(inventory)

    elif Event == "GettingHungry":
        inventory["Plate of Steak"] = 5
        print("The Plate of Steak was added to your inventory.")
        print("Plate of Steak")

    elif Event == "BattleWithThree":
        inventory["Key"] = 1
        print("The Key was added to your inventory")
        OptionsConfirm



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
            PlayerHealthChanges()
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
        OptionsConfirm()
        AddToInventory()
        print("""If you want to open up the inventory, press the I button on your keyboard. This way you will be able to use items to restore your HP.
        Why don't you try it now?""")
        usr_input = input(":")
        if usr_input in OpenInventory:
            UseItems()
            Event = "GettingHungry"
        else:
            continue

    elif Event == "GettingHungry":
        PlayerGetsHungry()
        OptionsConfirm()
        print("'Oh man, I guess I must have been here for a while, I don't think I've eaten in a couple of hours...'")
        OptionsConfirm()
        print("'Hopefully I can get out of here soon...'")
        OptionsConfirm()
        print("I continued my walk along the corridor despite my persistent hunger pangs.")
        OptionsConfirm()
        print("Eventually I cam across another room, and the lights were on.")
        OptionsConfirm()
        print("'Is this... A kitchen?'")
        OptionsConfirm()
        print("""Sure enough it was a kitchen, housing the usual appliances you would find. A micorwave, fridge, stove and oven.
        Nothing looked out of the ordinary.""")
        OptionsConfirm()
        print("""I eventually found a plate on the counter which has some steak on it.""")
        OptionsConfirm()
        print("""'Finders keepers...' I took the steak without a care in the world. I was too hungry to be concerned about whether
        or not the food was poisoned or edible in the first place.'""")
        OptionsConfirm()
        AddToInventory()
        OptionsConfirm()
        ReduceHunger()
        Event = "ThreeHeads"


    elif Event == "ThreeHeads":
        print("After regaining my energy, I left the kitchen.")
        OptionsConfirm()
        print("But then...")
        OptionsConfirm()
        print("*ROAR!*")
        OptionsConfirm()
        print("My head quickly snapped to noise reverberating across the room. What I was saw, was a three headed dog")
        OptionsConfirm()
        print("Once all six eyes locked onto me I realised that running would not be an option.")
        OptionsConfirm()
        Event = "BattleWithThree"
        if Event == "BattleWithThree":
            while Round < 3: #when Round reaches 3, the battle will end
                FightOptions()
                if weaponChoice == 1:
                    print("I used the torch in an attempt to burn  off one of the heads.")
                    OptionsConfirm()
                    PlayerHealthChanges() #Damage is done by the enemy
                    OptionsConfirm()
                    Round += 1 #After this the battle loops back to the FightOptions function
                elif weaponChoice == 2:
                    print("I used the Lance to stab one of the heads in the eyes...")
                    OptionsConfirm()
                    print("One of the dogs lost its composure and started thrashing around, until suddenly it stopped moving... ")
                    OptionsConfirm()
                    PlayerHealthChanges() #Damage is done by the enemy
                    OptionsConfirm()
                    Round += 1 #After this the battle loops back to the FightOptions function
                if Round == 3:
                    print("The three headed dog has fallen!")
                    OptionsConfirm()
                    print("'Thank goodness...'")
                    OptionsConfirm()
                    AddToInventory()
                    Event = "ReachingTheEnd"
    elif Event == "ReachingTheEnd":
        print("With the three headed dog no longer a threat I proceeded onwards.")
        OptionsConfirm()
        print("'Hopefully I won't run into anymore bizzare creatures'")
        OptionsConfirm()
        print("Eventually I reached a huge red door, which had a lock in it")
        OptionsConfirm()
        print("'Perhaps this key I got recently will help?")
        OptionsConfirm()
        UseItems()
