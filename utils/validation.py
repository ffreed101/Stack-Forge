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