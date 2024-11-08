from models.item import Item

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