


                                #============functions(Ready V-2)============




#============Menu(Ready V-2)============

def show_menu(menu):
        print('========== Welcome to the TO-DO-LIST menu ==========')
        print("\n" * 2)
        for key, value in menu.items():
            print(f"{key}. {value}" )
        print("\n")   
        menu_input = input("Let's make your chouse: " )
        print("\n" * 2)
        return menu_input
#============Add task(Ready V-2)============

def add_task(user_list):
        print('========== Add task ==========')
        print("\n" * 2)

        add_task_input = input("Let's write down the list: ")
        user_list.append(add_task_input)
        print( add_task_input + " was added")
        print("\n" * 2)
        return user_list


#============Show tasks(Ready V-2)============
def Show_tasks(user_list):
        print('========== Show tasks ==========')
        print("\n")

        for x, worts in enumerate(user_list, start=1):
            print(f"{x}. {worts}")
#============Delete task(Ready V-2)============
def Delete_task(user_list):
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
        return user_list
#============Exit(Ready V-2)============
def Exit():
        print('========== Exit ==========')
        print("\n" * 2)
        Exit_user = input("Do you want to leave ?----Yes/No----:  ").lower()
        print("\n")
        if Exit_user == 'yes':
            print('Byeeee!')

            return True
        elif Exit_user == 'no':
            return False
        else:
              None
#_________________________________________________________________________________________________________________________________________________________________________________________________
                                #============Main list============
#============listS============
menu = {
    1: "Add task",
    2: "Show tasks",
    3: "Delete task",
    4: "Exit"
}
user_list = []

while True:
      choice = show_menu(menu)

      if choice == '1':
            user_list = add_task(user_list)
      elif choice == '2':
            Show_tasks(user_list)
      elif choice == '3':
            user_list = Delete_task(user_list)
      elif choice == '4':
            if Exit():
                  break
            