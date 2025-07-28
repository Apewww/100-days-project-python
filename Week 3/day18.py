# introduction
# import json

# with open("Week 3\sample_data\json_data", "r") as file:
#     tasks = json.load(file)
#     print(tasks)

# tasks = [
#     {"task": "Complete Project", "status": "Incomplete"}
# ]

# with open("Week 3\sample_data/tasks.json", "w") as file:
#     json.dump(tasks, file, indent=4)

# with open("Week 3\sample_data/tasks.json", "r") as file:
#     tasks = json.load(file)
    
# tasks.append({"task": "Learn Python", "status": "Incomplete"})

# with open("Week 3\sample_data/tasks.json", "w") as file:
#     json.dump(tasks, file, indent=4)



# Mini To-Do App
import json
import os

# Define file name
json_file = 'Week 3\sample_data/my_tasks.json'

if not os.path.exists(json_file):
    with open(json_file, "w") as file:
        json.dump([], file)
        
# Step 1: Load task from JSON
def load_task():
    with open(json_file, 'r') as file:
        return json.load(file)
    
# Step 2: Save task to JSON
def save_task(tasks):
    with open(json_file, "w") as file:
        json.dump(tasks, file, indent=4)
    
# Step 3: Add a new Task
def add_task():
    tasks_name = input("Enter the task name: ").strip()
    tasks = load_task()
    tasks.append({"task": tasks_name, "status": "Incomplete"})
    save_task(tasks)
    print(f'Task "{tasks_name}" added succesfully')
    
# Step 4: View all Tasks
def view_tasks():
    tasks = load_task()
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}: {task['task']} -> {task['status']}")
    else:
        print("No Tasks Found")
        
# Step 5: Update Task Status
def update_status():
    tasks = load_task()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_status = input("Enter the new status (Complete/Incomplete): ").strip()
            tasks[task_index]['status'] = new_status
            save_task(tasks)
            print("Task status updated successfully")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number")
        
# Step 6: Delete a Tasks
def delete_task():
    tasks = load_task()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_task(tasks)
            print(f'Task"{deleted_task["task"]}" deleted succesfully')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid Input. Please enter a valid task number.")
        
# Step 7: Display Menu
def main_menu():
    print("\n----- Mini To-Do App -----")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update Task status")
    print("4. Delete a task")
    print("5. Exit")
    
# Step 8: Main Program Loop
while True:
    main_menu()
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_status()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Program ended. Thank you")
        break
    else:
        print("Invalid Input. Please enter valid choice (1-5)") 