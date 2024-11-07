class Item:
    def __init__(self, itemNum):
        self.itemNum = itemNum
        self.tags = []

    def createTag(self):
        while True:
            try:
                tag_number = input("Enter tag number: ")
                if not tag_number.isdigit():
                    raise ValueError("Tag number should contain only numbers.")

                piece_count = int(input("Enter piece count: "))
                new_tag = Tag(tag_number, piece_count)
                self.tags.append(new_tag)
                print(f"Tag {tag_number} with piece count {piece_count} added.")

                # Check if the user wants to add another tag
                add_more = input("Add another tag? (Y/N): ").upper()
                if add_more != "Y":
                    break
            except ValueError as e:
                print(f"Invalid input: {e}")

class Tag:
    def __init__(self, tagNum, pieceCount):
        self.tagNum = tagNum
        self.pieceCount = pieceCount

def createItem():
    print()
    while True:
        itemNum = input("Enter new item number: ")
        if len(itemNum) != 5:
            print("Invalid item number: Must be 5 digits long. ")
        elif itemNum.isdigit() == False:
            print("Invalid item number: Must contain only numbers. ")
        else:
            break

    newItem = Item(itemNum)

    while True:
        initWithTags = input("Would you like to add tags now? (Y/N): ").upper()

        if initWithTags == "Y":
            print("You chose to add tags.")
            newItem.createTag()
            break
        elif initWithTags == "N":
            # Skip adding tags
            print("You chose not to add tags.")
            break
        else:
            print("Invalid selection. Please try again.")

def createTags(item):
    pass


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