def script(data):
    total=0
    # only if dictionary is not empty
    if len(data)!=0:
        for value in data.values():
            total=total+value
    return total
# Data
dataA={1:10,2:20,3:30,4:40,5:50,6:60}
dataB={"A":1000,"B":2000,"C":3000,"D":4000}
print(script(dataA))
print(script(dataB))
