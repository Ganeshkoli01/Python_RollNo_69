
# ZeroDivisionError: division by zero

try:
    num = int(input("Enter No: "))
    result = 10/num
    print(f"Result is: {result}")
except Exception:
    print("Invalid Input")                        
else:                         
    print("No Exception")
finally:
    print("Remaning Code")
