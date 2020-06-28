print("The Program checks if the decimal number falls in range of 8 bit or not\n")
# Range FUnction to find if number lies between 0-255 which is range of 8 bit values
def checkRange(num):
    if 255 >= num >= 0:
        return True
    else:
        return False
# main method python
if __name__=="__main__":
    # input
    n=int(input("Enter A Number which lies in range of 8 bit:"))
    check=checkRange(n)
    # Control statement
    if check:
        print("Number lies in 8 bit range")
    else:
        print("Number Doesnot lie in 8 bit range\nNote:0-255 is range for 8 bit value")


