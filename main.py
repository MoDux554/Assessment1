import time

inventory = {}
Weapons = {}

health = 20 #if it reaches 0 the it is game over

hunger = 0 #if it reaches 10 the health begins to reduce gradually


Choice = ""
weaponChoice = ""
Restore = ""
Yes = ["y", "Y", "yes", "Yes"]
No = ["n", "N", "no", "No"]
Confirm = ["a", "A"]
LMR = ["Left", "Middle", "Right"]
Fight = ["Fight", "fight", "f", "F"]
Run = [ "Run", "run", "r", "R"]
Close = ["B", "b"]
OpenInventory = ["Item", "I", "i"]
SkeletonLance = ["Skeleton Lance", "skeleton lance", "sk", "SK","s", "S"]
Torch = ["Torch", "torch", "t", "T"]



Round = 0
valueChange = 0
Event = 0

print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")



def FightOptions():
   global Choice
   global weaponChoice
   global usr_input
   global inventory

   while True:
        if Event == "FightWithSkeleton":
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
                print(Weapons)
                weaponChoice = (input("Which weapon do you wish to use? input 1 or 2 to use either the Torch or the Skeleton Lance"))
                if weaponChoice in Torch:
                    break
                elif weaponChoice in SkeletonLance:
                    break
                else:
                    continue
            elif Choice in OpenInventory:
                UseItems()
                break
            else:
                continue


def UsedTorch():

    if Weapons["Torch"] > 0:
     Weapons["Torch"] -= 1
     print(Weapons)

def UsedSkeletonLance():
    if Weapons["Skeleton Lance"] > 0:
        Weapons["Skeleton Lance"] -= 1
        print(Weapons)

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
    OptionsConfirm()


def PlayerGetsHungry():
    global hunger
    global health

    hunger += 5
    print("Your stomach growls...")
    OptionsConfirm()


    if hunger == 10:
        health -= 2
        print("Hunger:", hunger)
        OptionsConfirm()
        print("Health remaining:", health)
    elif hunger > 10:
        hunger = 10
        health -= 2
        print("Hunger:", hunger)
        OptionsConfirm()
        print("Health remaining:", health)
    else:
        print("Hunger:", hunger )


def PlayerHealthChanges(): #changes to the player's stats during and outside of battle
    global health

    if Event == "FightWithSkeleton":
         health -= 3
         print("3 damage was dealt!")
         OptionsConfirm()
         print("(Health remaining):", health)
         OptionsConfirm()

    elif Event == "RunningFromSkeleton":
        health -= 5
        print("5 damage was dealt!")
        OptionsConfirm()
        print("Health remaining", health)
        OptionsConfirm()


    elif Event == "BattleWithThree":
        health -= 5
        print("5 damage was dealt!")
        OptionsConfirm()
        print("(Health remaining):", health)




def RestoreHP(): #called when the player uses the Med Kit item
    global health
    health +=5

    if health > 20:
        health = 20 #this allows the player to restore their HP back to just 20 and not above it
        print("Health:", health)
        inventory["Med Kit"] -=1
        OptionsConfirm()
        print(inventory)
        OptionsConfirm()
    else:          #this takes into account of the health not being above 20/below 20
        print("Health:", health)
        inventory["Med Kit"] -= 1
        OptionsConfirm()
        print(inventory)
        OptionsConfirm()


def UseItems(): #the player is asked which item they want to use, each item has their own set function
   print(inventory)
   while True:
       select_item = input("Input an item or press the B button to close the inventory")
       if select_item in inventory:
           if select_item == "Med Kit":
               MedKit()
               break
           elif select_item == "Plate of Steak":
               Steak()
               break
       elif select_item in Close:
           break
       else:
           continue

def MedKit(): #the player is asked if they want to use the Med Kit which will call the RestoreHP function as long as they have more than 0.
    while True:
        if inventory["Med Kit"] >= 0:
            print("This will restore 5 HP, do you want to use it? ")
            Restore = input("Yes/No:")
            if Restore in Yes:
                RestoreHP()
            elif Restore in No:
                break
        else:
            print("You no longer have this item!")
            OptionsConfirm()

def Steak(): #the player is asked if they want to eat the Steak which will call the ReduceHunger function as long as they have more than 0
    while True:
        if inventory["Plate of Steak"] > 0:
            print("This will reduce your hunger by 3. Do you want to eat it?")
            Restore = input("Yes/No:")
            if Restore in Yes:
                ReduceHunger()
            elif Restore in No:
                break
            else:
                continue
        else:
            print("You no longer have this item!")
            OptionsConfirm()


def AddToInventory(): #Adds things the player picks up during the game into the inventory, these correspond
                       #to the "events" the player is in.
    if Event == 0:
        inventory["Sticks"] = 5
        print("The bunch of sticks were added to the inventory")
        OptionsConfirm()
        print(inventory)

    elif Event == "MakingSomeLight":  # the torch is added here so that more can be added to it from the user input
        Weapons["Torch"] = 0
        global valueChange #this variable is referenced outside of the PlayerInventory function
        while True:
            try:
                valueChange = int(input("How many of your sticks would you like to light up?"))
                if valueChange <=5 and valueChange >=1:
                    inventory["Sticks"] -= valueChange
                    Weapons["Torch"] += valueChange
                    print(inventory)
                    OptionsConfirm()
                    print("The torches were added to your weapons.")
                    OptionsConfirm()
                    print(Weapons)
                    break
                else:
                    print("Please enter in a number between 1 and 5.")#occurs when the player enters a number less than one or more than #5
                    OptionsConfirm()
                    continue
            except ValueError: #occurs when the player doesnn't even enter in a number
                print("please enter in a number.")
                OptionsConfirm()

    elif Event == "FightWithSkeleton":
        print("the Skeleton Lance was added to your weapons.")
        OptionsConfirm()
        Weapons["Skeleton Lance"] = 10 #the player gains 10 Skeleton Lances
        print("Your torch has run out!")
        UsedTorch() #since the torch was used in this fight, it would be reduced by one in its quantity
        OptionsConfirm()

    elif Event == "AfterSkeletonFight":
        inventory["Med Kit"] = 5 #the player gains 5 Med Kits
        print("The Med Kit was added to your inventory.")
        OptionsConfirm()
        print(inventory)
        OptionsConfirm()

    elif Event == "GettingHungry":
        inventory["Plate of Steak"] = 5
        print("The Plate of Steak was added to your inventory.")
        OptionsConfirm()
        print(inventory)

    elif Event == "BattleWithThree":
        inventory["Key"] = 1
        print("The Key was added to your inventory")
        OptionsConfirm()
        print(inventory)
        OptionsConfirm()



while True: #This is where all the events of the game play out
    if health == 0:
        Event = "Death"


    if Event == 0:
        OptionsConfirm()
        print(" 'Nghh...' ")
        time.sleep(1)
        print(" 'My head... where I am..?' ")
        time.sleep(1)
        print("""I took in my surroundings as my consciousness slowly reformed.
It seems that I am in a dark room, there were no window so I couldn't tell
what the time was. The room itself was mostly dark. Looking down  I saw
a bunch of sticks lying around, which I picked up.""")

        OptionsConfirm()
        AddToInventory()
        Event = "MakingSomeLight"

    elif Event == "MakingSomeLight":
        PlayerGetsHungry()
        print("'Oh I think I see some fire there, maybe I can make a couple of torches?'")
        OptionsConfirm()
        AddToInventory()
        print("I used one of the torches to look around my surrondings again, until I found the exit of this room.")
        OptionsConfirm()
        print("'Yes! A way out!'")
        OptionsConfirm()
        print("I then left the room without looking back. Outside was a corridor, where I saw another door opened.")
        OptionsConfirm()
        Event = "EnteringTheDoor"

    elif Event == "EnteringTheDoor":
        PlayerGetsHungry()
        print("'I am not going to get much done standing out here'")
        OptionsConfirm()
        print("I walked through and nothing at first seemed conspicuous. That was until... I came across a pile of bones and a skull.")
        OptionsConfirm()
        print("'Wh-What...?'")
        OptionsConfirm()
        print("""I didn't have much time to think more about what I was seeing as the bones and skull began to move, 
they rearranged themselves until it resembled an actual body.""")
        OptionsConfirm()
        print("Once that was complete, the skeleton took notice of my presence and started to run at me!")
        OptionsConfirm()
        Event = "FightWithSkeleton"

    elif Event == "FightWithSkeleton":
        print("'What should I do?!'")
        time.sleep(1.5)
        FightOptions() #for this fight the player has the choice to fight or run
        if usr_input in Fight:
            print("""Here goes nothing!' Gripping the torch tightly I swiped the flame at the alive skeleton.
the flames made contact with the skeleton for a brief moment.""")
            OptionsConfirm()
            print("In retaliation, the skeleton swipped its hand at me! their claws slashed against my side once!")
            PlayerHealthChanges()
            print("""Dismissing the pain burning in my side I swiped the torch at it again, aiming for the head this time
around. The head was reduced to nothing but ash, causing the rest of the body to collapse into a heap of bones!""")
            OptionsConfirm()
            AddToInventory()
            Event = "AfterSkeletonFight"

        elif usr_input in Run:
            Event = "RunningFromSkeleton"
            if Event == "RunningFromSkeleton":
                print("'I don't think fighting that thing is such a good idea!' I turned back and begin to run from the skeleton.")
                OptionsConfirm()
                print("It gave chase and eventually it caught up to me. It closed the distanced and swipped at my back!")
                OptionsConfirm()
                PlayerHealthChanges()
                if health <=0:
                    Event = "Death" #if the player's health reaches zero the death event carries out
                else:
                    Event = "FightWithSkeleton" #sets the player back to the fight or run option.

    elif Event == "AfterSkeletonFight":
        PlayerGetsHungry()
        print("I walked on some more until I came across another object on the ground.")
        OptionsConfirm()
        print("'Looks like a first aid kit, this will be helpful, my side is still hurting after that encounter with the skeleton.'")
        OptionsConfirm()
        AddToInventory()
        print("""If you want to open up the inventory, press the I button on your keyboard. This way you will be able to use items to restore your HP.
Why don't you try it now?""")
        usr_input = input(":")
        if usr_input in OpenInventory:
            UseItems() #the player will be given the choice to use the Med Kit
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
        print("My head quickly snapped to noise reverberating across the room. What I was saw, was a three headed dog!")
        OptionsConfirm()
        print("Once all six eyes locked onto me I realised that running would not be an option.")
        OptionsConfirm()
        Event = "BattleWithThree"
        if Event == "BattleWithThree":
            while Round < 3: #when Round reaches 3, the battle will end
                FightOptions()
                if Choice in Fight and weaponChoice in Torch and Weapons["Torch"] > 0: #This will only run if the player has more than 0 torches.
                    print("I used the torch in an attempt to burn  off one of the heads.")
                    UsedTorch()
                    Round += 1
                    OptionsConfirm()
                    weaponChoice = "" #resets the weapon choice
                    Choice = "" #resets the general choice
                    print("The dog was screeching whilst consumed by the fire until the its voiced died out and stopped moving...")
                    OptionsConfirm()
                    PlayerHealthChanges() #Damage is done by the enemy
                    OptionsConfirm()
                elif Choice in Fight and weaponChoice in SkeletonLance and Weapons["Skeleton Lance"] > 0: #This only runs if the player has more than 0 lances.
                    print("I used the Lance to stab one of the heads in the eyes...")
                    UsedSkeletonLance()
                    Round += 1
                    OptionsConfirm()
                    weaponChoice = "" #Resets the weapon choice
                    Choice = "" #Resets the general choice
                    print("One of the dogs lost its composure and started thrashing around, until suddenly it stopped moving... ")
                    OptionsConfirm()
                    PlayerHealthChanges() #Damage is done by the enemy
                    OptionsConfirm()
                elif Choice in Fight and weaponChoice in SkeletonLance and Weapons["Skeleton Lance"]<= 0:
                    print("You no longer have this weapon!")
                    Choice = "" #Resets the general choice
                    weaponChoice = "" #Resets the weaponChoice
                    OptionsConfirm()
                    continue

                if Choice in OpenInventory:
                    UseItems()
                    PlayerHealthChanges()
                    Choice = "" #Resets the general choice
                    OptionsConfirm()

                if Round == 3 and health != 0 and health >0:
                    print("The three headed dog has fallen!")
                    OptionsConfirm()
                    print("'Thank goodness...'")
                    OptionsConfirm()
                    AddToInventory()
                    Event = "ReachingTheEnd"

                elif health <= 0:
                    Event = "Death"


    elif Event == "ReachingTheEnd":
        print("With the three headed dog no longer a threat I proceeded onwards.")
        OptionsConfirm()
        print("'Hopefully I won't run into anymore bizzare creatures.'")
        OptionsConfirm()
        print("Eventually I reached a huge red door, which had a lock in it.")
        OptionsConfirm()
        print("'This key should be helpful.'")
        OptionsConfirm()
        inventory["Key"] -= 1
        print("You used the key to unlock the door.")
        OptionsConfirm()
        print("""The door opened without any issues, and with it, I actually saw the outside. I finally made my way out of this
weird building, and I can now retrun to my normal life.""")
        OptionsConfirm()
        print("The End.")
        break


    elif Event == "Death":
        print("You have died. Game over...")
        OptionsConfirm()
        break