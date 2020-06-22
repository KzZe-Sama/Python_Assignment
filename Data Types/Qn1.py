#Input
string=input("Enter a String:")
charList=[]
charCounts={}
# Creating List for the all chars
for value in string:
    charList.append(value)
# print(charList)
#Set of the unique element in the list
charSet=set(charList)
# Iterating each values and adding them in a dictionary
for value in charSet:
    charCounts[value]=charList.count(value)
print(charCounts)

