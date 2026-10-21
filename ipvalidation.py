def validate_ip(ip):
    ip = ip.replace(" ","")
    dot = 0
    for check in ip:
        if check == ".":
            dot = dot + 1
        elif not check.isdigit():
            return False
    if dot == 3:
        parts = ip.split(".")
        for part in parts:
            if int(part) > 255:
                return False
        return True
    else:
        return False

valid = False

"""
while not valid:
    ip = input("Please enter an IP address: ")
    if validate_ip(ip):
        print("Valid IP address")
        valid = True
    else:
        print("Invalid IP address")
"""
