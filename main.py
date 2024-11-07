class Item:
    def __init__(self, itemNum, tags):
        self.itemNum = itemNum
        self.tags = []

class Tags:
    def __init__(self, tagNum, pieceCount):
        self.tagNum = tagNum
        self.pieceCount = pieceCount

def displayGreeting():
    print("Welcome to Stack Forge!")

def displayMenu(menuTitle, menuOptions):

    print(f"\n--- {menuTitle} ---")

    for i in range(len(menuOptions)):
        if menuOptions[i] == menuOptions[-1]:
            print(f"0) {menuOptions[i]}")
        else:
            print(f"{i+1}) {menuOptions[i]}")

def getAndValidateInput(choices):
    # Makes the little choice guide that goes in parentheses using all available choices
    choiceGuideText = "/".join(choices)

    # Get Input
    userChoice = input(f"Enter your choice({choiceGuideText}): ")

    # Validate Input
    while userChoice not in choices:
        print("\nInvalid Selection. Please try again. \n")
        userChoice = input(f"Enter your choice({choiceGuideText}): ")

    return userChoice


def main():

    # Menu Lists. Might Dictionary this later.
    mainMenuOptions = ["Create Item", "Query Item", "View Items", "Edit Item", "Delete Item", "Exit"]
    mainMenuChoices = ["1", "2", "3", "4", "5", "0"]

    displayGreeting()

    while True:
        displayMenu("Main Menu", mainMenuOptions)
        match getAndValidateInput(mainMenuChoices):
            case "1":
                # Implement create item
                pass
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