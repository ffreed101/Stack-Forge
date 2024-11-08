from utils.menu import displayMenu
from utils.validation import getAndValidateInput
from utils.item_functions import createItem

def createTags(item):
    pass

def displayGreeting():
    print("Welcome to Stack Forge!")

def main():

    # Menu Lists. Might Dictionary this later.
    mainMenuOptions = ["Create Item", "Query Item", "View Items", "Edit Item", "Delete Item", "Exit"]
    mainMenuChoices = ["1", "2", "3", "4", "5", "0"]

    items = []

    displayGreeting()

    while True:
        displayMenu("Main Menu", mainMenuOptions)
        match getAndValidateInput(mainMenuChoices):
            case "1":
                items.append(createItem())
            case "2":
                # Implement query item
                pass
            case "3":
                # Implement view items
                pass
            case "4":
                # Implement edit item
                pass
            case "5":
                # Implement delete item
                pass
            case "0":
                print("\nClosing...")
                break
            case _:
                print("\nERROR: Validation Issue. Restarting menu...")

main()