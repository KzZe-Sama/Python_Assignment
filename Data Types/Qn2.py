String=input("Enter A String:")
answer=""
lengthSting=len(String)
# Getting Values through indexes
if(lengthSting>2):
    answer=String[0]+String[1]+String[-2]+String[-1]
elif(lengthSting==2):
    answer=String[0]+String[1]+String[0]+String[1]
else:
    answer="Empty String"
print(answer)
