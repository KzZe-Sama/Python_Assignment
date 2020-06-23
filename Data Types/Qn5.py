# Input
String=input("Enter A String:")
String=String.strip()
length=len(String)
result=""
# Control Statement
if(length<3):
    result=String
else:
    check=""
    check=String[-3]+String[-2]+String[-1]
    if(check=="ing"):
        result=String+"ly"
    else:
        result=String+"ing"
print(result)
