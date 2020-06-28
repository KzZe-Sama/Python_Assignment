# function
nonZero=True
def check_prime(num):
    isPrime = False
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            nonZero = True
            break
        else:
            isPrime = True
    return isPrime

# input
ask=int(input("Enter A number: "))
# checking if input is 1 or 0
if ask == 0 or ask == 1:
    print( f"{ask} is neither prime nor composite")
else:
    returnValue=check_prime(ask)
    if returnValue:
        print(f"{ask} is Prime")
    elif not returnValue:
        print(f"{ask} is Composite")
