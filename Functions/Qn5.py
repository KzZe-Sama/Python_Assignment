def fact(n):
    factNum=1
    # Checking if number is  greater than 0
    if n>0:
        for i in range(n,0,-1):
            factNum=factNum*i
        return factNum
    # Checking if number is 0
    elif n==0:
        return factNum
    # checking if number is less than 0
    else:
        return "only gives factorial for non zero integer"
# Input
ask=int(input("Enter a number:"))
print(fact(ask))
