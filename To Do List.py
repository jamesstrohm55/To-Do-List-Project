todolist = []

def add_tasks(): #Add your tasks here
    task = input("What would you like to add to your To Do list?\n")

    if task in todolist:
        print(f"{task} already in your To Do List!\n")
    else:
        print(f"{task} has been added to you To Do List.")
    

    todolist.append(task) #Save task in list


def remove_tasks(): #Delete Tasks
    task = input("What task do you want to delete?\n")

    if task in todolist:
        todolist.remove(task)
        print(f"{task} was removed from your To Do list.\n")
    else:
        print(f"{task} is not currently in your To Do List.\n")
        
def view_tasks(): #Viewing tasks
    if not todolist:
        print("No current tasks.")
    else:
        print("\nYour Current Tasks: ")
        for task in todolist:
            print(f"\nTask: {task}")

def menu(): #User input needed to select what option they want
    while True:
        print("\n---Task Manager---")
        print("\n1. Add Task")
        print("\n2. Remove Task")
        print("\n3. View Tasks")
        print("\n4. Exit Program")

        choice = int(input("Choose a selection on the menu (1-4)"))

        if choice ==  1:
            add_tasks()
        elif choice == 2:
            remove_tasks()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            print("Exiting Application, Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1-4\n")


#Run application
menu()
