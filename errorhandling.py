#11/13/24
try:
    print(5/10)
    #This will produce an error
except TypeError: #Name of Error
    print("Error Lmao")
    #Covering up errors by just saying this shit
except ZeroDivisionError:
    print("Error Stuff")
finally:
    print("It happens")
    #always happens no matter what