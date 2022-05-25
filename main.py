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
            updateContact()
            showMenu()
        elif option == 3:
            print("\n===========")
            print("Add Contact")
            print("===========")
            addContact()
            showMenu()
        elif option == 4:
            deleteContact()
            showMenu()
        elif option == 5:
            print("Good bye!")
            break
        else: 
            print("Option unavailable.")

def showContacts():
    # Numbering
    num = 1
    print("================================================================================")
    print("|No.| Name            | Number           | Address:                            |")
    print("================================================================================")
    for contact in contacts.values():
        # format to left-align and give some space
        print("|{no} .| {name:<15} | {number:<15}  | {address:<35} |"
        .format(no = num, name = contact["name"], 
                number = contact["number"], address = contact["address"]))
        num += 1
    print("================================================================================")

def addContact():
    # get the last key from the contacts and add 1 to it
    contact_order = list(contacts.keys())[-1] + 1

    # get input from the user to be saved as a new contact
    while True:
        try:
            name = str(input("Enter contact name: "))
            number = int(input("Enter contact number: "))
            address = str(input("Enter contact address: "))
            # add data to contacts
            contacts[contact_order] = {
                "name" : "{}". format(name),
                "number" : number,
                "address" : "{}".format(address)
            }
            print("Data " + name + " added succesfully!\n")
            break
        except ValueError:
            print("Wrong input. Please enter a correct format.\n")
            break

def updateContact():
    isUpdate = False
    showContacts()
    # get data from user
    oldName = str(input("Enter contact name you want to change: "))
    # check the name
    for contact in contacts.values():
        if oldName in contact.values():
            print("Data " + oldName + " found!")
            try:
                newName = str(input("Enter contact new name: "))
                newNumber = int(input("Enter contact number: "))
                newAddress = str(input("Enter contact address: "))
                # update contact
                contact.update({"name" : "{}". format(newName)})
                contact.update({"number" : newNumber})
                contact.update({"address" : "{}". format(newAddress)})
                isUpdate = True
                print("Data '{}' succesfully changed to '{}'.\n".format(oldName, newName))
                
            except ValueError:
                print("Format error. Please enter a correct number.") 

    if isUpdate == False:
        print("Data not found. Please enter a correct name\n")
        showMenu()

def deleteContact():
    isDelete = False
    showContacts()
    name = str(input("Enter contact's name you want to delete: "))
    for contact_id, contact_info in list(contacts.items()):
        if contact_info["name"] == name:
            del contacts[contact_id]
            showContacts()
            print("Data '{}' deleted Succesfully!\n".format(name))
            isDelete = True
    if isDelete == False: print("Data not found!\n")

#code
showMenu()