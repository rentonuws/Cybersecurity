def calculate_failed_percentage(failed,total):
    result = failed / total * 100
    if result > 100:
        return "Impossible, Total number of failed shouldn't be more than total attempted."
    elif result >=50:
        return "HIGH RISK"
    elif result >= 25:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

try:
    failed = int(input("Please enter the number of failed login attempts: "))
    total = int(input("Please enter the total number of login attempts: "))
    print(calculate_failed_percentage(failed,total))
except ValueError:
    print("Please enter a number only.") 
except ZeroDivisionError:
    print("Total login attempts cannot be zero." \
    )   