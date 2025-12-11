# 1. try, # except, # else, # finally


try: 
    # print(1 + 1)  # This will raise a TypeError
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
        print("Division by zero is not allowed.")
except:
        print("An error occurred.")
else:
        print("No errors occurred.")
finally:
        print("Execution completed.")
