def navigate_user():
    while True:
        user_input = input(
            "\nWelcome to our login system \nType login or register: ")
        if user_input == "register":
            return register_user()
        elif user_input == "login":
            return login_user()
        elif user_input == "":
            print("The option can not be left blank.")
        else:
            print("Invalid Option")


def register_user():
    print("\n ---CREATE YOUR ACCOUNT--- \n")
    first_name = input("FirstName: ")
    last_name = input("LastName: ")
    username = input("Username: ")
    password = input("Password: ")
    # the file database should be created first for it to work
    if first_name == last_name == username == password == "":
        print("None of the fields can  be left blank.")
        return navigate_user()
    f = open('database.txt', 'a')
    f.write(f"{first_name} ")
    f.write(f"{last_name} ")
    f.write(f"{username} ")
    f.write(f"{password} \n")
    f.close()
    print("User Created sucessfuly")
    return navigate_user()


def login_user():
    print("\n  __login your Account__\n  ")
    while True:
        user_name = input("Username: ")
        pass_word = input("password: ")
        if user_name == "" and pass_word == "":
            print("Username or Password can not be left blank.")
            return login_user()
        # The file database should be created first for it to work
        f = open("database.txt", "r")
        data = f.readlines()
        f.close()
        store_single_data = []
        for single_data in data:
            store_single_data.append(single_data)
        for latter in store_single_data:
            replaced_char = latter.replace("\n", "")
            l = replaced_char.split(" ", 4)
            u = l[2:3]
            p = l[3:4]
            f = l[0:4]

        if u[0] == user_name and p[0] == pass_word:
            print("Welcome " + f[0].capitalize() + " " + f[1].capitalize())
            break
        else:
            print("Invalid username or password")


navigate_user()
