tasks = []
def add_task(task):
    tasks.append({"task":task , "status" : False})
    print("task added successfully")
    

def delete_task(task_no):
    if task_no <= len(tasks):
        tasks.pop(task_no - 1)
        print("task is deleted successfully")
    else :
        print("task not found")

        

def display_task():
    print("No.  Task          Status")
    for indx , task in enumerate(tasks, 1):
        symbol = "✓" if task["status"] else "✗"   
        print(f"{indx}  {task['task']}  {symbol}" )

def task_completed(task_no):
    tasks[task_no - 1]["status"] = True
    print("Task is marked successfully")


def main():
    while True:
        print("The To-Do list --------------------------------------")
        print("Options : ")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Task")
        print("4. Mark Task as complete")
        print("5. Exit")

        choice = (input("choose an option :"))

        if choice == "1":
            task = input("Enter the task :")
            add_task(task)
        elif choice == "2":
            task_no = int(input("Enter task number :"))
            delete_task(task_no)
        elif choice =="3":
            display_task()
        elif choice =="4":
              task_no = int(input("Enter task number :"))
              task_completed(task_no)  
        elif choice == "5":
            print("Exiting.........")
            break
        else:
            print("invalid choice")   


if __name__ == "__main__":
    main()                     




        
