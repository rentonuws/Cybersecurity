def check(password):
    allowcha = '!"£$%'
    dig = 0
    UAlph = 0
    LAlph = 0
    Symb = 0    
    
    if len(password) < 10:
        return False

    for i in password:
        if i.isupper():
            UAlph = UAlph + 1
        elif i.islower():
            LAlph = LAlph + 1
        elif i.isdigit():
            dig = dig + 1
        elif i in allowcha:
            Symb = Symb + 1
        elif i == " ":
            return False

    if UAlph >= 1 and LAlph >=1 and dig >=2 and Symb >=1:
        return True
    else:
        return False

valid = False

while not valid:
    password = input("Please enter a password: ")
    if check(password):
        print("Password accepted")
        valid = True
    else:
        print("Password doesn't match the minimum requirement, please re-enter")
    