############################################
###### CRUD-BASED TO-DO LIST PROGRAM #######

from time import sleep

path_file = input("\n\nEnter the path of the folder contains the file you want to save/modify: \n> ")

if path_file == '':
    print("\nNo path provided. Exiting the program.")
    exit()
    
else:
    print("\nCreating the file if it doesn't exist...")
    sleep(2)
    path_file = path_file.strip() + "\\todo_list.txt"

with open(path_file, 'w') as file:
    file.close()

while True:
    try:
        print("\n----------------TO-DO LIST---------------")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("\nEnter your choice: \n> ")
        
        if choice == '1':
            while True:
                task = input("Enter the task to add. Enter '0' to go back: ")
                
                if task.lower() == '0':
                    print("\nCancelled adding task.\n")
                    break
                else:
                    with open (path_file, 'a') as file:
                        file.write(task + '\n')
                        print(f">> Task '{task}' added successfully.\n")
                continue
            
            
        elif choice == '2':    
            with open (path_file, 'r') as file:
                tasks = file.readlines()
                if tasks:
                    print("\n\nYour tasks are:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task.strip()}")
                        
                else:
                    print("\nNo tasks found.")
                        
        elif choice == '3':
            
            while True:
                print('\nChoose the task number to update: ')
                with open(path_file, 'r') as file:
                    tasks = file.readlines()
                    if tasks:
                        for i, task in enumerate(tasks, start=1):
                            print(f"{i}. {task.strip()}")
                            
                        while True:
                            try:
                                task_number = int(input("\nEnter the task number to update. Enter '0' to go back: "))
                                if task_number == 0:
                                    break
                                elif 1 <= task_number <= len(tasks):
                                    updated_task = input("Updated Task: ")
                                    tasks[task_number - 1] = updated_task + '\n'
                                    
                                    with open(path_file, 'w') as file:
                                        file.writelines(tasks)
                                    
                                    print(f">> Task {task_number} updated successfully.\n")
                                    print("\nUpdated task list:")
                                    with open(path_file, 'r') as file:
                                        tasks = file.readlines()
                                        if tasks:
                                            for i, task in enumerate(tasks, start=1):
                                                print(f"{i}. {task.strip()}")
                                    continue
                                
                                else:
                                    print("Invalid task number. Please try again.")
                            except ValueError:
                                print("Invalid input. Please enter a valid task number.")
                    else:
                        print("\nNo tasks found.")
                        break   
                     
                break
        
        
        elif choice == '4':
            
            while True:
                print('\nChoose the task number to delete: ')
                with open(path_file, 'r') as file:
                    tasks = file.readlines()
                    if tasks:
                        for i, task in enumerate(tasks, start=1):
                            print(f"{i}. {task.strip()}")
                
                        while True:
                            try:
                                task_number = int(input("\nEnter the task number to delete. Enter '0' to go back: "))
                                if task_number == 0:
                                    break
                                elif 1 <= task_number <= len(tasks):
                                    tasks.pop(task_number - 1)
                                    
                                    with open(path_file, 'w') as file:
                                        file.writelines(tasks)
                                    
                                    print(f">> Task {task_number} deleted successfully.\n")
                                    
                                    if len(tasks) == 0:
                                        print("\nNo tasks found.")
                                        break
                                    
                                    print("\nUpdated task list:")
                                    with open(path_file, 'r') as file:
                                        tasks = file.readlines()
                                        if tasks:
                                            for i, task in enumerate(tasks, start=1):
                                                print(f"{i}. {task.strip()}")
                                    continue
                                
                                else:
                                    print("Invalid task number. Please try again.")
                            except ValueError:
                                print("Invalid input. Please enter a valid task number.")
                    else:
                        print("\nNo tasks found.")
                        break        
                break
                        
        elif choice == '5':
            print("\nExiting the program.\n")
            break
    
    except ValueError:
        print("\nInvalid input. Please enter a valid choice (1 - 5).")
