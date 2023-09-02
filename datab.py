# Function to load tasks from a file
def load_tasks(filename):
    tasks = []
    with open(filename, "r") as file:
        for line in file:
            task, priority,completed = line.strip().split(",")
            tasks.append({"task": task, "completed": completed == "True", "priority": priority})
    return tasks

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['priority']}, {task['completed']}\n")

#Function to delete tasks to a file
def delete_task(filename, task_index):
    tasks = []
    with open(filename, 'r') as file:
        tasks = file.readlines()
    
    if (1<=task_index<=len(tasks)):
        del tasks[task_index - 1]
        with open(filename, "w") as file:
            file.writelines(tasks)
    else:
        print("Invalid task number.")

# Function to update status of a to-do
def update_status(filename, task_index):
    tasks = []
    with open(filename, "r") as file:
        tasks = file.readlines()
    
    if (1<=task_index<=len(tasks)):
        task, priority,completed = tasks[task_index - 1].strip().split(",")
        if completed == "False":
            completed = "True"
        else:
            completed = "True"
        tasks[task_index - 1] = f"{task},{priority},{completed}\n"

        with open(filename, "w") as file:
            file.writelines(tasks)
    else:
        print("Invalid task number.")

# Function to update priority of a to-do
def update_priority(filename, task_index, new_priority):
    tasks = []
    with open(filename, "r") as file:
        tasks = file.readlines()
    
    if (1<=task_index<=len(tasks)):
        task, priority,completed = tasks[task_index - 1].strip().split(",")
        tasks[task_index - 1] = f"{task},{new_priority},{completed}\n"
        

        with open(filename, "w") as file:
            file.writelines(tasks)
    else:
        print("Invalid task number.")