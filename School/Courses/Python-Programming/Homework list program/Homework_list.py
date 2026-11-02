import csv
from objects import Homework, HomeworkList

def display_menu():
    print("The Homework List program")
    print()
    print("Command Menu")
    print("List                 - List all homework")
    print("add                  - Add  homework")
    print("complete             - Mark homework complete")
    print("delete               - Delete homework item")
    print("exit                 - Exit program")

def get_homeworkList():
    FILENAME= "Homework_list.csv"
    homeworkList = HomeworkList("Software Design")
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            #Convert row to homework Object
            homework = Homework(row[0])
            if row[1] == "True":
                homework.completed = True
            homeworkList.addHomework(homework)
        return homeworkList
            

def list_homeworkList(homeworkList):
    if homeworkList.getCount() == 0:
        print("There are no homeworks. \n")
    else:
        i = 1
        for homework in homeworkList:
            print(str(i) + ". " + str(homework))
            i+=1



def add_homework(homeworkList):
    description = input("Description of Homework:  ")
    homework = Homework(description)
    homeworkList.addHomework(homework)
    


def complete_homework(homeworkList):
    number = int(input("Number:  "))
    homework = homeworkList.getHomework(number)
    homework.completed = True
    print()

def delete_homework(homeworkList):
    number = int(input("Number:  "))
    homework = homeworkList.getHomework(number)
    homeworkList.removeHomework(homework)

def write_homeworkList(name, homeworkList):
    #Convert the Homework list object to a list of lists
    rows= []
    for homework in homeworkList:
        row = []
        row.append(homework.description)
        row.append(homework.completed)
        rows.append(row)
        
    #Write the list of lists to csv file
    FILENAME = "Homework_list.csv"
    with open(FILENAME, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
          
    


def main():
    display_menu()

    homeworkList = get_homeworkList()
    print("Software Design Homework List")

    while True:
        command = input ("Command:  ")
        
        if command.lower() == "list":
            list_homeworkList(homeworkList)

        elif command.lower() == "add":
            add_homework(homeworkList)

        elif command.lower() == "complete":
            complete_homework(homeworkList)
            
        
        elif command.lower() == "delete":
            delete_homework(homeworkList)
        
        
        elif command.lower() == "exit":
            write_homeworkList("Software Design", homeworkList)
            print("Bye")
            break
            
        else:
            print("Invalid command")
            
if __name__ == "__main__":
    main()
    
    
        
        