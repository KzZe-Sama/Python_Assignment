String=input("Enter A String:")
firstChar=String[0]
#dummy variable for answer
result=firstChar
# Iterating from 1 index
for i in range(1,len(String)):
    if(String[i]==firstChar):
        result=result+"$"
    else:
        result=result+String[i]
print(result)
