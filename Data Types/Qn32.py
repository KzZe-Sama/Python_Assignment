# Lambda Function
x=lambda n:n*n
# Script that stores the keys and values in a dictionary
def script(n):
    result={}
    if n!=0:
        for i in range(1,n+1):
            result[i]=x(i)
    else:
        return "cannot iterate over 0"
    return result

print(script(5))
print(script(0))
print(script(1))
print(script(10))