def main_menu():
    print("welcome to to_do list application")
    print("select from below")
    print("1.Add task")
    print("2.delete task")
    print("3.view task")
    print("4.update task")
def view_task(tasks):
    if len(tasks)>0:
        print("Your existing tasks are :")
        for task in tasks:
            task_index=tasks.index(task)
            print(f"{task_index+1}.{task}")
    else:
        print("------*Your tasks list is empty*------")
        main_menu()

def add_task(list):
    current_task=input("Enter the task you want to add")
    list.append(current_task)
    print("Your task added successfully")
    print("Updated task list")
    view_task(list)
    print("--------------------------")

def update_task(list):
    if len(list)>0:
        update_task_sno=int(input("Enter the number of the task you want to update"))
        updated_task=input(f"Enter the updated task {update_task_sno}")
        list[update_task_sno-1]=updated_task
        print("Your task updaed successfully")
        print("Updated task list")
        view_task(list)
        print("--------------------------")
    else:
        print("------*Your tasks list is empty please return to main menu*------")
        main_menu()

def delete_task(list):
    if len(list)>0:
        delete_task_sno=int(input("Enter the number of the task you want to delete"))
        list.pop(delete_task_sno-1)
        print("Your task deleted successfully")
        print("Updated task list")
        view_task(list)
        print("--------------------------")
    else:
        print("------*Your tasks list is empty*------")
        main_menu()
main_menu()


tasks=[]
while True:
    user_inp=int(input("Enter a number to select option : "))
    match user_inp:
        case 1:
            add_task(tasks)
        case 2:
            delete_task(tasks)
        case 3:
            view_task(tasks)
        case 4:
            update_task(tasks)
        case default:
            print("Something went wrong please try again ")
