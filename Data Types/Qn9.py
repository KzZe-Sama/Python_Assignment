# Input String
string=input("Enter a String:")
string=string.strip()
# getting first and last values of string
storeFirstChar=string[0]
storeLastChar=string[-1]
newString=""
# Creating List
for i in range(0,len(string)):
    if i==0 :
        newString=newString+storeLastChar
    elif i==len(string)-1:
        newString=newString+storeFirstChar
    else:
        newString=newString+string[i]
print(newString)
