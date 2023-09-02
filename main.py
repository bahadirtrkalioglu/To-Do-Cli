import datab
import tabulate


def print_tasks(tasks):
    counter = 1
    print("...:::TO-DOS:::...")
    table = [["Index", "Task", "Priority","Status"]]
    for task in tasks:
        status = "✅" if task["completed"] else "❎"
        table.append([counter, task["task"], task["priority"],status])
        counter += 1
    print(tabulate.tabulate(table, tablefmt="fancy_grid", headers="firstrow"))
        

def main():
    tasks = datab.load_tasks("db.txt")
    if tasks == []:
        print("It seems that you haven't added TO-DO, let's add one.")
    else:
        print("Tasks have loaded!\n")
    is_continue = True
    print("print 'help' to learn commands\n\n")

    while is_continue:
        prompt = input("prompt: ").lower()
        if(prompt == 'help'):
            print("...:::TO-DO:::...")
            print("'new' for create new to-do\n'print' for print all to-dos\n'exit' for exiting\n'del' to enter delete mode\n'update' for update status-priority of a to-do\n")
        
        if(prompt == 'new'):
            name = input("Enter To-Do name: ")
            priority = input("Enter priority ('low' - 'mid' - 'high'): ").lower()
            if (priority == "low" or priority=="mid" or priority == "high"):
                new_task = {"task": name, "completed": "False", "priority": priority}
                tasks.append(new_task)
                datab.save_tasks("db.txt", tasks)
            else:
                print("Please enter a true priority value!")
                continue
                
        if(prompt == 'exit'):
            datab.save_tasks("db.txt", tasks)
            is_continue = False
        
        if(prompt == 'print'):
            print_tasks(tasks)
            

        if(prompt == 'del'):
            print_tasks(tasks)
            task_index = input("Enter task number to delete, for exit delete mode type 'exit': ")
            if(task_index == 'exit'):
                continue
            else:
                datab.delete_task("db.txt", int(task_index))
                tasks = datab.load_tasks("db.txt")
                datab.save_tasks("db.txt", tasks)
            
        if(prompt == 'update'):
            print_tasks(tasks)
            update_method = input("Please type an update method (priority-status): ").lower()
            if (update_method == "status"):
                task_index = input("Enter task number to update, for exit update mode type 'exit': ")
                if(task_index == 'exit'):
                    continue
                else:
                    datab.update_status("db.txt", int(task_index))
                    tasks = datab.load_tasks("db.txt")
                    datab.save_tasks("db.txt", tasks)
            else:
                task_index = input("Enter task number to update, for exit update mode type 'exit': ")
                if task_index == "exit":
                    continue
                else:
                    priority_type = input("Enter priority ('low' - 'mid' - 'high'): ").lower()
                    if (priority_type == "low" or priority_type=="mid" or priority_type == "high"):
                        datab.update_priority("db.txt", int(task_index), priority_type)
                        tasks = datab.load_tasks("db.txt")
                        datab.save_tasks("db.txt", tasks)
                    else:
                        print("Please enter a true priority value!")
                        continue




if __name__ == "__main__":
    main()