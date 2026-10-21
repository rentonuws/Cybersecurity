def authenticate(username,password):
    if username == "admin" and password == "admin123":
        return True
    else:
        return False

valid = False

while not valid:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if authenticate(username,password):
        print("Login sucessful")
        valid = True
    else:
        print("Invalid username or password")