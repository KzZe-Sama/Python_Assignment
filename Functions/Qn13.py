# function
x=lambda data: tuple(sorted(data))

# datas
dataA=(1,3,6,4,9,11,8)
dataB=(20,10,30,15)
print("Unsorted")
print(dataA)
print("Sorted")
print(x(dataA))
print("Unsorted")
print(dataB)
print("Sorted")
print(x(dataB))