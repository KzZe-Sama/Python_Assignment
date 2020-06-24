# Data
dataA={1:10,2:20,3:30,4:40,5:50,6:60}
dataB={"A":1000,"B":2000,"C":3000,"D":4000}
# Before Removing
print("The Data:")
print(dataA)
print(dataB)
print("Removing 1 from dataA and B from dataB")
# Removing
dataA.pop(1)
dataB.pop("B")
print(dataA)
print(dataB)
