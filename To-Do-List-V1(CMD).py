#Hi! I've started developing my new project called "TO-DO-LIST."

#This is a list project where you can record and save the data you need. You can view the list, add items to it, delete, or exit the application, and all the data will remain saved!

#In this project, I want to apply my basic Python knowledge and learn how to work with more diverse tools and libraries available in Python.

#Let's start with version V-1!!!!!

#_________________________________________________________________________________________________________________________________________________________________________________________________
#list_user = []

menu = {
    1: "Add task",
    2: "Show tasks",
    3: "Delete task",
    4: "Exit"
}

while True:
    print('========== Welcome to the TO-DO-LIST menu ==========')
    for key, value in menu.items():
        print(f"{key}. {value}")

    user = input("Let's make your chouse: " )
    if user == 1:
        print






