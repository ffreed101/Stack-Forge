def displayMenu(menuTitle, menuOptions):

    print(f"\n--- {menuTitle} ---")

    for i in range(len(menuOptions)):
        if menuOptions[i] == menuOptions[-1]:
            print(f"0) {menuOptions[i]}")
        else:
            print(f"{i+1}) {menuOptions[i]}")