from object import Website, WebsiteList
import db

#importing the files


# function to display the menu for user to choose
def display_menu():
    print("COMMAND MENU")
    print("list - list all websites")
    print("add - add a website")
    print("delete - delete a website")
    print("exit - exit program")


# choice list is entered this function is called
def list_websites(website_list):
    websites = website_list.get_website()
    for website in websites:
        print(website[0] + " - " + website[1])  # print all the list of websites stored in the list


# choice add is entered this function is called
def add_website(website_list):
    name = input("Enter website name: ")
    url = input("Enter website URL: ") # take name and url of website as input from user
    website = Website(name, url)
    website_list.add_website([website.get_name(), website.get_url()]) # add them to the list of websites
    db.write_csv_file("websites.csv", [[website.get_name(), website.get_url()]],'a') # append the new website detail into the csv by calling the created write_csv
    print(name + " was added.\n")


#choice delete is entered this function is called
def delete_website(website_list):
    name = input("Enter website name: ")  # takes only the name of website as input to be deleted
    website_to_delete = None
    for website in website_list.get_website():  # search the name of website in list to delete
        if website[0] == name:
            website_to_delete = website
            break
    if website_to_delete:  # if website is in list then delete the website from list
        website_list.remove_website(website_to_delete)
        db.write_csv_file("websites.csv", website_list.get_website(),'w') # Write the entire updatedwebsite list to the file after deletion
        print(name + " was deleted.\n")
    else:
        print("No website was found with that name.\n")


# main driver function to call other functions
def main():
    display_menu()

    website_list = WebsiteList()

    website_csv_file_name = "websites.csv"
    website_list_data = db.read_csv_file(website_csv_file_name)
    for website_data in website_list_data:
        website = Website(website_data[0], website_data[1])
        website_list.add_website([website.get_name(), website.get_url()])

    while True:
        command = input("Enter command: ")
        if command == "list":
            list_websites(website_list)
        elif command == "add":
            add_website(website_list)
        elif command == "delete":
            delete_website(website_list)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()
