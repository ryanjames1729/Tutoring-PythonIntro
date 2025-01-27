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
    print()
    print("HP: ", playerHP)
    print("Stamina: ", playerStamina)
    print("Inventory: ", playerInventory)
    time.sleep(3)

def livingRoom():
    os.system('clear')
    print("You are in the living room.")
    print("Your options are:")
    print("1. Go to the kitchen.")
    print("2. Go to the bedroom.")
    print("3. Go to the porch.")
    print("4. Go to the dining room.")
    print("5. See my stats.")
    choice = input(">")
    if choice == "1":
        kitchen()
    elif choice == "2":
        bedroom()
    elif choice == "5":
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
    print("2. See my stats.")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        showStats()
        kitchen()
    else:
        print("Sorry, thats not an option.")
        time.sleep(3)
        kitchen()

def bedroom():
    os.system('clear')
    print("You are in the bedroom.")
    print("Your options are:")
    print("1. Go to the living room.")
    print("2. Go to the bathroom.")
    print("3. See my stats.")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        pass
        # add the bathroom code later
    elif choice == "3":
        showStats()
        bedroom()
    else:
        print("Sorry, thats not an option.")
        time.sleep(3)
        bedroom()

start()