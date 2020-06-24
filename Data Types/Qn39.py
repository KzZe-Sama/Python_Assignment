def add_item(data,*args):
    listData=list(data)
    for value in args:
        listData.append(value)
    newData=tuple(listData)
    return newData
# Data
data=(1,2,3,4)
# Before Adding
print("Before Adding")
print(data)
# Adding data
print("After Adding:")
print("adding 5,6,7,8",add_item(data,5,6,7,8))
print("adding 5",add_item(data,5))
