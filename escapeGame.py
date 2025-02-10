import os, time

playerName = ""
playerHP = 100
playerInventory = []
playerStamina = 100

def start():
    global playerName
    print("Welcome to the Escape Game.")
    print("What would you like your player to be called?")
    playerName = input(">")
    print("Welcome, ", playerName)
    livingRoom()

def showStats():
    global playerInventory, playerStamina
    print()
    print("HP: ", playerHP)
    print("Stamina: ", playerStamina)
    print("Inventory: ", playerInventory)
    if "mountain dew" in playerInventory:
        print("Do you want to drink the mountain dew?")
        choice = input(">")
        if choice == "yes" or choice == "y":
            playerStamina = playerStamina + 15
            playerInventory.remove("mountain dew")
            print("The sugary rush from doing the dew gave you 15 points to your stamina.")
    time.sleep(3)

def livingRoom():
    os.system('clear')
    print("You are in the living room.")
    print("Your options are:")
    print("1. Go to the kitchen.")
    print("2. Go to the bedroom.")
    print("3. Go to the porch.")
    print("4. Go to the dining room.")
    print("5. Search the living room.")
    print("6. See my stats.")
    choice = input(">")
    if choice == "1":
        kitchen()
    elif choice == "2":
        bedroom()
    elif choice == "3":
        porch()
    elif choice == "4":
        diningRoom()
    elif choice == "5":
        print("You searched the whole room and found nothing.")
        time.sleep(3)
        livingRoom()
    elif choice == "6":
        showStats()
        livingRoom()
    else:
        print("Sorry, thats not an option.")
        time.sleep(3)
        livingRoom()

def kitchen():
    os.system('clear')
    print("You are in the kitchen.")
    print("Your options are:")
    print("1. Go to the living room.")
    print("2. Go to the dining room.")
    print("3. Open the refrigerator.")
    print("4. See my stats.")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        diningRoom()
    elif choice == "3":
        if "mountaind ew" not in playerInventory:
            print("You open the refrigerator and found mountain dew. Do you want to pick it up?")
            choice = input(">")
            if choice == "y" or choice == "yes":
                playerInventory.append("mountain dew")
                print("You picked up the mountain dew and added it to your inventory.")
        else:
            print("You searched the room and found nothing.")
        time.sleep(3)
        kitchen()
    elif choice == "4":
        showStats()
        kitchen()
    else:
        print("Sorry, thats not an option.")
        time.sleep(3)
        kitchen()

def bedroom():
    global playerStamina, playerInventory
    os.system('clear')
    print("You are in the bedroom.")
    print("Your options are:")
    print("1. Go to the living room.")
    print("2. Go to the bathroom.")
    print("3. Search the bedroom.")
    print("4. Go to sleep.")
    print("5. See my stats.")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        bathroom()
    elif choice == "3":
        if "book" not in playerInventory:
            print("You found a book. Do you want to pick it up?")
            choice = input(">")
            if choice == "y" or choice == "yes":
                playerInventory.append("book")
                print("You picked up the book and added it to your inventory.")
        else:
            print("You searched the room and found nothing.")
        time.sleep(3)
        bedroom()
    elif choice == "4":
        print("You lay down on the bed to take a nap.")
        time.sleep(5)
        playerStamina += 10
        print("You earned 10 stamina points!")
        time.sleep(3)
        bedroom()
    elif choice == "5":
        showStats()
        bedroom()
    else:
        print("Sorry, thats not an option.")
        time.sleep(3)
        bedroom()

def bathroom():
    os.system('clear')
    print("You are in the bathroom.")
    print("Your options are:")
    print("1. Go to the bedroom.")
    print("2. Search the bathroom.")
    print("3. See my stats.")
    choice = input(">")
    if choice == "1":
        bedroom()
    elif choice == "2":
        if "friendly ghost" not in playerInventory:
            print("You found a friendly ghost. Do you want to be friends with the ghost?")
            choice = input(">")
            if choice == "y" or choice == "yes":
                playerInventory.append("friendly ghost")
                print("Great! The ghost will follow you around the house.")
        else:
            print("You searched the room and found nothing.")
        time.sleep(3)
        bathroom()
    elif choice == "3":
        showStats()
        bathroom()
    else:
        print("Sorry, thats not an option.")
        time.sleep(3)
        bathroom()

def porch():
    os.system('clear')
    print("You are in the porch.")
    print("Your options are:")
    print("1. Go to the living room.")
    print("2. Search the porch.")
    print("3. See my stats.")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        if "dead spider" not in playerInventory:
            print("You found a dead spider. Do you want to pick it up?")
            choice = input(">")
            if choice == "y" or choice == "yes":
                playerInventory.append("dead spider")
                print("You picked up the dead spider and added it to your inventory.")
        else:
            print("You searched the room and found nothing.")
        time.sleep(3)
        porch()
    elif choice == "3":
        showStats()
        porch()
    else:
        print("Sorry, thats not an option.")
        time.sleep(3)
        porch()

def diningRoom():
    os.system('clear')
    print("You are in the dining room.")
    print("Your options are:")
    print("1. Go to the living room.")
    print("2. Go to the kitchen")
    print("3. Read a book.")
    print("4. See my stats.")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        kitchen()
    elif choice == "3":
        print("You grab a book off the bookshelf and it reveals a hidden door.")
        print("Do you want to open the door?")
        choice = input(">")
        if choice == "yes" or choice == "y":
            if "friendly ghost" in playerInventory:
                escape()
            else:
                print("Sorry, this door is locked.")
                time.sleep(3)
                diningRoom()
        else:
            diningRoom()
    elif choice == "4":
        showStats()
        diningRoom()
    else:
        print("Sorry, thats not an option.")
        time.sleep(3)
        diningRoom()

def escape():
    print("Your friendly ghost helped unlock the hidden door.")
    print("You can see a way out but you have to get past the dementor.")
    if "book" in playerInventory:
        print("Your book starts to glow and opens up to the petronus spell.")
        print("You cast the spell and the dementor goes away.")
        print("You get out of the house and win the game!")
    else:
        print("You don't know how to defeat the dementor and it takes 50 points from your health.")
        playerHP = playerHP - 50
        print("You are sent back to the living room.")
        time.sleep(3)
        playerInventory.clear()
        livingRoom()

start()