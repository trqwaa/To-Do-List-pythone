
#_________________________________________________________________________________________________________________________________________________________________________________________________

#============LISTS============
menu = {
    1: "Add task",
    2: "Show tasks",
    3: "Delete task",
    4: "Exit"
}
user_list = []
#_____________________________

#============Menu(Ready V-1)============

while True:
    
    print('========== Welcome to the TO-DO-LIST menu ==========')
    for key, value in menu.items():
        print(f"{key}. {value}")

    menu_input = input("Let's make your chouse: " )

#_____________________________

#============Add task(Ready V-1)============

    if menu_input == '1':
        print('========== Add task ==========')

        add_task_input = input("Let's write down the list: ")
        user_list.append(add_task_input)
        print( add_task_input + " was added")

#_____________________________

#============Show tasks(Ready V-1)============
    elif menu_input == '2':

        print('========== Show tasks ==========')

        print(user_list)

        print('________________________________')

#_____________________________

#============Delete task(NEED TO WORK)============

    elif menu_input == '3':
        print('========== Delete task ==========')
        for x, worts in enumerate(user_list, start=1):
            delete_task_user = int(input("Select a number to delete|" + str(user_list) + ": " ))
            if delete_task_user == x:
                user_list.remove(worts)
                print("was removed " + "'" + worts + "'")
        print("your list at the moment: " + ", ".join(map(str, user_list)))

 #_____________________________  
 
#============Exit(is being created)============

    elif menu_input == '4':
        None

#_____________________________





