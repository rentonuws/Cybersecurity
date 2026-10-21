from ipvalidation import validate_ip

ipaddr = ["192.168.0.1","10.0.0.1","192.168.10.17","10.13.10.1","8.8.8.8"]

print(f"The first IP is {ipaddr[0]} and the last IP is {ipaddr[len(ipaddr)-1]}")

def add_IP(ans):
    valid = False
    while not valid:
        ip = input("Please input an IP you want to add to the list: ")
        if validate_ip(ip):
            count = 0
            valid = True
            ip = ip.replace(" ","")
            for ipfind in ipaddr:
                if ipfind == ip:
                    count = 1
            if count == 1:
                print(f"{ip} existed, Nothing to change.")
            else:
                ipaddr.append(ip)
        else:
            validans = False
            while not validans:
                ans = input("Invalid IP address. Enter 0 to try again or enter 1 to skip: ")
                if not ans.isdigit():
                    print("Please enter 0 or 1 only.")
                else:
                    if ans == "0" or ans == "1":
                        validans = True
                        if ans == "1":
                            valid = True
                    else:
                        print("Please enter 0 or 1 only.")

def replace_IP(ans):
    valid = False
    position = 0
    i = 0

    while not valid:
        print(ipaddr)
        exist_ip = input("Please enter the IP you want to be changed: ")
        if validate_ip(exist_ip):
            exist_ip = exist_ip.replace(" ","")
            for ipfind in ipaddr:
                if ipfind == exist_ip:
                    position = i
                else:
                    i = i+1
            valid = True
        else:
            validans = False
            while not validans:
                ans = input("Invalid IP address. Enter 0 to try again or enter 1 to skip: ")
                if not ans.isdigit():
                    print("Please enter 0 or 1 only.")
                else:
                    if ans == "0" or ans == "1":
                        validans = True
                        if ans == "1":
                            valid = True
                        else:
                            print("Please enter 0 or 1 only.")
    valid = False
    while not valid:
        new_ip = input("Please enter the IP you want to replace: ")
        if validate_ip(new_ip):
            valid = True
            new_ip = new_ip.replace(" ","")
            ipaddr[position] = new_ip
        else:
            validans = False
            while not validans:
                ans = input("Invalid IP address. Enter 0 to try again or enter 1 to skip: ")
                if not ans.isdigit():
                    print("Please enter 0 or 1 only.")
                else:   
                    if ans == "0" or ans == "1":
                        validans = True
                        if ans == "1":
                            valid = True
                        else:
                            print("Please enter 0 or 1 only.")


def check_IP(ans):
    valid = False
    found = 0

    while not valid:
        exist_ip = input("Please enter the IP you want to search: ")
        if validate_ip(exist_ip):
            valid = True
            exist_ip = exist_ip.replace(" ","")
            for ipfind in ipaddr:
                if ipfind == exist_ip:
                    found = 1
            if found == 1:
                print(f"{exist_ip} found")
            else:
                print("It's not on the list")
        else:
            validans = False
            while not validans:
                ans = input("Invalid IP address. Enter 0 to try again or enter 1 to skip: ")
                if not ans.isdigit():
                    print("Please enter 0 or 1 only.")
                else:
                    if ans == "0" or ans == "1":
                        validans = True
                        if ans == "1":
                            valid = True
                        else:
                            print("Please enter 0 or 1 only.")

def remove_IP(ans):
    valid = False
    while not valid:
        exist_ip = input("Please enter the IP you want to be removed: ")
        if validate_ip(exist_ip):
            exist_ip = exist_ip.replace(" ","")
            if exist_ip in ipaddr:
                valid = True
                ipaddr.remove(exist_ip)
                print(f"{exist_ip} have been removed")
            else:
                print(f"{exist_ip} doesn't exist.")
        else:
            validans = False
            while not validans:
                ans = input("Invalid IP address. Enter 0 to try again or enter 1 to skip: ")
                if not ans.isdigit():
                    print("Please enter 0 or 1 only.")
                else:
                    if ans == "0" or ans == "1":
                        validans = True
                        if ans == "1":
                            valid = True
                        else:
                            print("Please enter 0 or 1 only.")

def check_exist(ans):
    valid = False
    while not valid:
        exist_ip = input("Please enter the IP you want to be changed: ")
        if validate_ip(exist_ip):
            valid = True
            exist_ip = exist_ip.replace(" ","")
            for ipfind in ipaddr:
                if ipfind == exist_ip:
                    valid = True
                    print(f"{exist_ip} found.")
        else:
            validans = False
            while not validans:
                ans = input("Invalid IP address. Enter 0 to try again or enter 1 to skip: ")
                if not ans.isdigit():
                    print("Please enter 0 or 1 only.")
                else:
                    if ans == "0" or ans == "1":
                        validans = True
                        if ans == "1":
                            valid = True
                        else:
                            print("Please enter 0 or 1 only.")

valid = False
while not valid:
    ans = input("1. Adding a new IP\n2. Replace an IP\n3. Delete Existing IP\n4. Check IP is exist or not\n5. Total number of IPs\n6. Display all IPs on lists\n7. exit\n")
    if ans == "1":
        add_IP(ans)
    elif ans == "2":
        replace_IP(ans)
    elif ans == "3":
        remove_IP(ans)
    elif ans == "4":
        check_IP(ans)
    elif ans == "5":
        print(f"Total number of IPs is {len(ipaddr)}")
    elif ans == "6":
        print(ipaddr)
    elif ans == "7":
        valid = True
    else:
        print("Invalid answered, please try again.")    