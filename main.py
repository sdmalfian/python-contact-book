"""
Contact Book Application By Sadam Alfian.
"""
contacts = {
    1 : {
        "name" : "Emil",
        "number" : 219818,
        "address" : "76 Buttonwood Street Valdosta"
    },
    2 : {
        "name" : "Tobias",
        "number" : 2871238,
        "address" : "566 Panama City, FL 32404"
    },
    3 : {
        "name" : "Linus",
        "number" : 12323,
        "address" : "76 Bellevue St. Beaver Falls"
    }
}

# Creating a menu display
def showMenu():
    print("Welcome to Contact Books. What do you want to do?")
    print("1. View contact")
    print("2. Change contact")
    print("3. Add contact")
    print("4. Delete contact")
    print("5. Exit")

    selectMenu()

def selectMenu():
    repeat = True
    while repeat == True:
        try:
            option = int(input("Choose[1-5]: "))
        except ValueError:
            print("Please input number.")
            # fill the option with value so the program won't error
            option = 0
        if option > 0 and option < 6: repeat = False
        if option == 1:
            showContacts()
            showMenu()
        elif option == 2:
            print("\n==============")
            print("Change Contact")
            print("==============")
            #updateContact()
            #showMenu()
        elif option == 3:
            print("\n===========")
            print("Add Contact")
            print("===========")
            #addContact()
            #showMenu()
        elif option == 4:
            #deleteContact()
            #showMenu()
            print("4 selected")
        elif option == 5:
            print("Good bye!")
            break
        else: 
            print("Option unavailable.")

def showContacts():
    # manual numbering 
    num = 1
    print("================================================================================")
    print("|No.| Name            | Number           | Address:                            |")
    print("================================================================================")
    for contact in contacts.values():
        # format to left-align and give some spacing
        print("|{no} .| {name:<15} | {number:<15}  | {address:<35} |"
        .format(no = num, name = contact["name"], 
                number = contact["number"], address = contact["address"]))
        num += 1
    print("================================================================================")

showMenu()