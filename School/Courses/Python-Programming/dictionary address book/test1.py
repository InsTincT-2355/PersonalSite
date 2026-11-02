# Creates a dictionary
contacts = {
        "Joel":
              {"address": "1500 Anystreet", "city": "San Francisco",
                "state": "California", "postalCode": "94110",
                "phone": "555-555-1111"},
              
              
        "Adam":
              {"address": "1500 green st", "city": "San Francisco",
                "state": "California", "postalCode": "93110",
                "phone": "333-333-2222"},
            }









#This Function Displays all the Contacts (did not fully understand)
def display_list():
    for id, info in contacts.items():
        print("\nName:", id)
        for key in info:
            print(key + ':', info[key])
        



   
#This Function Allows The user to Search for A contact
def show_contact():
    
    

    while True:
        name=input("Please Provide me with a Name:  ").capitalize()

        print()
        print()
        
        
        if name in contacts:
            print("Name: ",name)
            print("Address: ",contacts[name].get('address'))
            print("City: ",contacts[name].get('city'))
            print("State: ",contacts[name].get('state'))
            print("Postal Code: ",contacts[name].get('postalCode'))
            print("Phone: ",contacts[name].get('phone'))
            response = input("Would you like to find another contact? (y/n): ").lower()
            print()
            if (response != "y"):
                 continue
            
            
            
        if name not in contacts:
            
            print("Sorry Invalid Contact Name.")
            response = input("Would you like to find another contact? (y/n): ").lower()
            print()
            if (response != "y"):
                return



#This function allows us to add and edit a contact
def add_edit_book(contacts, mode):
    name = input("Please provide me the Contact's Name: ").capitalize()
    if mode == "add" and name in contacts:
        print(" I'm sorry i couldn't add the contanct you mentioned, It is already in the catalogue.")
        print()
        response = input ("Would you like to edit the contact? (y/n): ").lower()
        if(response != "y"):
            return
    elif mode == "edit" and name not in contacts:
        print("I'm sorry, i couldn't edit the contact you specified as it is not in the catalogue.")
        print()
        response = input("Would you like to add it? (y/n): ").lower()
        if (response != "y"):
            return

    address = input("Address: ")
    city = input("City: ")
    state = input("state: ")
    postalCode = input("postalCode: ")
    phone = input("phone: ")

    
    
    # Create a dictionary for the book data
    contact = {"address": address,
            "city": city,
            "state": state,
            "postalCode": postalCode,
            "phone": phone}
    # Add the book data to the catalog using title as key
    contacts[name] = contact
    
    
    
#This function allows us to delete a contact
def delete_contact(contacts):
    name = input("Please provide me the name of the contact you would like to delete: ").capitalize()
    if name in contacts:
        del contacts[name]
        print(" The contact has been removed.")
    else:
        print("The contact you provided is not in the catalogue")
    
    
    
    
    
    
    
#Displays the Menu
def display_menu():
    
    
    
    
    
    
    
    
    print("Welcome to the Contacts Program")
    print()
    print()
    
    
    print("What would you like to do?")
    print()
    print()
    
    print("1) display -  List all Contacts")
    print("2) show - Show contact info")
    print("3) add -  Add contact")
    print("4) edit - Edit contact")
    print("5) del -  Delete contact")
    print("6) exit - Exit program")
    
    
    
    
    
#Main Program   
def main():
    
    print()
    print()
    display_menu()

    while True:
        print()
        command = input("Please Provide me with a command: ").lower()
        
        if command == "show":
            show_contact()

        elif command == "add":
            add_edit_book(contacts, mode="add")

        elif command == "edit":
            add_edit_book(contacts, mode="edit")
            
            
        elif command == "display":
            display_list()

        elif command == "del":
            delete_contact(contacts)


        elif command == "exit":
            print("Have a Great day !")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
