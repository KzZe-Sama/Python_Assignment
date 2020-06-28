# Data
listA=[1,2,3,4,5]
listB=[2,4,6]
# function
inter=list(filter(lambda el:el in listA,listB))
print(f"{listA} intersects {listB} = {inter}")