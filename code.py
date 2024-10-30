password = "nothing"
special = -1
while len(password) < 8 or special == -1:
    print("You password must follow the criteria:\nAt least 8 characters\nAt least 1 special character")
    password = input("Create a password: ")
    if len(password) < 8:
        print("You password must have at least 8 characters.")

    special = password.find('!')
    if special == -1:
        print("You must have a special character in you password.")
    
print("Your password has been successfully validated.")