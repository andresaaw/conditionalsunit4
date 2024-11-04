password = "nothing"
special = -1
while len(password) < 8 or special == -1:
    print("You password must follow the criteria:\nAt least 8 characters\nAt least 1 exclamtion mark")
    password = input("Create a password: ")

    special = password.find('!')
    if special != -1:
        if len(password) >= 8:
            print("Your password has been validated.")
            exit
        else:
            print("Your password requires to be longer than 8 characters.")
    elif special == -1:
        print("Your password requires a exclamation mark.")

