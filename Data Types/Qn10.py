# Input
String=input("Enter A String:")
String=String.strip()
# List
StringList=[]
StringResult=[]
Result=""
# Adding all char in List
for value in String:
    StringList.append(value)
# Appending all the even index char in new string
for index in range(len(StringList)):
    check= index%2
    if check==0:
        StringResult.append(StringList[index])
for char in StringResult:
    Result=Result+char
print(Result)


