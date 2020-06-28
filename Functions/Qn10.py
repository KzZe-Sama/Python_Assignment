#Function
def even_num(data):
    evenList=[]
    for value in data:
        if value%2==0:
            evenList.append(value)
    return evenList
# Data
dataA=[1,2,3,4,5,6,7,8,9,10]
dataB=[11,22,33,44,55,66,77,88]
print(even_num(dataA))
print(even_num(dataB))