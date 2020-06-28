# Function
x=lambda a:int(a)
# Exception Handling
try:
    String=input("Enter A String: ")
    data=x(String)
except ValueError:
    print("The Data of the given String is not an Integer")
else:
    print("The Data of the given String an Integer")
