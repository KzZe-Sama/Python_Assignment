def check_empty(data):
    # Checking if list is empty
    if len(data)==0:
        return True
    else:
        return False
# Data
dataA=[]
dataB=[""]
dataC=[1,2]
print(check_empty(dataA))
print(check_empty(dataB))
print(check_empty(dataC))