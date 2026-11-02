import db
from objects import Task, TaskList

# reads the function that gets the description of the task stores in a list
def display_task_list_names():
    task_list_names = db.get_task_list_names()
    print("Task Lists:")
    for i,description in enumerate(task_list_names, start=1):
        print(f"{i}. {description}")


# Lists the tasks based on description we chose.
def list_tasks(tasks):
    for i,type in enumerate(tasks, start=1):
        print(f"{i}. {type}")
        
#Adds a task 
def add_task(tasks):
    description = input("Task description: ")
    task = Task(description)
    tasks.addTask(task)
# deletes a task
def delete_task(tasks):
    number = int(input("Number: "))
    task = tasks.getTask(number)
    tasks.removeTask(task)
#Marks task as done
def complete_task(tasks):
    number = int(input("Number: "))
    task = tasks.getTask(number)
    task.completed = True
    print(f'Task "{task.description}" completed.\n')

def display_menu():
    print("The Task List program\n")
    print("COMMAND MENU")
    print("list     - List all tasks")
    print("add      - Add a task")
    print("complete - Complete a task")
    print("delete   - Delete a task")
    print("exit     - Exit program\n")

def main():
    display_menu()
    display_task_list_names()

    # select task list
    names = db.get_task_list_names()
    num = int(input("Enter number to select task list: "))
    name = names[num - 1]
    tasks = db.get_task_list(name)
    print(f"{name} task list was selected.\n")

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_tasks(tasks)
        elif command.lower() == "add":
            add_task(tasks)
        elif command.lower() == "delete":
            delete_task(tasks)
        elif command.lower() == "complete":
            complete_task(tasks)
        elif command.lower() == "exit":
            db.write_task_list(name, tasks)
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()