# function
def unique(data):
    setData=set(data)
    data=list(setData)
    data=sorted(data)
    return data
# data
items=[1,2,3,3,4,4,5,5]
print(items)
print(unique(items))