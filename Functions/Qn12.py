# Functions
def multi(num,*args):
    ans=num
    for value in args:
        ans=ans*value
    return ans
# Asking input from user
ask=int(input("Enter A Number:"))
print(multi(ask,1))
print(multi(ask,10))
print(multi(ask,5,2,3))
