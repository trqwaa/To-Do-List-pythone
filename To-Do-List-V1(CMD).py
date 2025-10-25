
#_________________________________________________________________________________________________________________________________________________________________________________________________

#============LISTS============
menu = {
    1: "Add task",
    2: "Show tasks",
    3: "Delete task",
    4: "Exit"
}
user_list = []
#============Menu(Ready V-1)============

while True:
    
    print('========== Welcome to the TO-DO-LIST menu ==========')
    print("\n" * 2)
    for key, value in menu.items():
        print(f"{key}. {value}" )
    print("\n")   
    menu_input = input("Let's make your chouse: " )
    print("\n" * 2)
#============Add task(Ready V-1)============

    if menu_input == '1':
        print('========== Add task ==========')
        print("\n" * 2)

        add_task_input = input("Let's write down the list: ")
        user_list.append(add_task_input)
        print( add_task_input + " was added")
        print("\n" * 2)
#============Show tasks(Ready V-1)============
    elif menu_input == '2':

        print('========== Show tasks ==========')
        print("\n")

        for x, worts in enumerate(user_list, start=1):
            print(f"{x}. {worts}")

#============Delete task(Ready V-1)============

    elif menu_input == '3':
        print('========== Delete task ==========')
        print("\n" * 2)
        for x, worts in enumerate(user_list, start=1):
            print(f"{x}. {worts}")
        delete_task_user = int(input("Select a number to delete: " ))
        print("\n")
        removed_item = user_list[delete_task_user - 1]
        del user_list[delete_task_user - 1]
        print("\n")
        print("was removed " + "'" + removed_item + "'")
        print("\n")
        print("your list at the moment: " + ", ".join(map(str, user_list)))
        print("\n" * 2)
#============Exit(Ready V-1)============

    elif menu_input == '4':
        print('========== Exit ==========')
        print("\n" * 2)
        Exit_user = input("Do you want to leave ?----Yes/No----:  ").lower()
        print("\n")
        if Exit_user == 'yes':
            print('Byeeee!')
            break
        else:
            None






