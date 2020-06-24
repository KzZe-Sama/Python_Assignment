# FUnction that takes string and list as parameter
def insert_string(string,data):
    newList=[]
    for value in data:
        # Type Casting
        newValue=string+str(value)
        # Adding the new value in new list
        newList.append(newValue)
    return newList
print(insert_string('emp',[1,2,3,4,5]))
print(insert_string('go',["italy","spain","brazil"]))