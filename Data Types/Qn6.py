String=input("Enter A String:")
String=String.strip()
result=""
start=0
end=0
# Spliting the words
subString=String.split(" ")
# Checking if not or poor exists
notCheck= "not" in subString
poorCheck="poor" in subString
# extracting the not and poor positions
if notCheck and poorCheck:
    for i in range(len(subString)):
        if(subString[i]=="not"):
            start=i
        if(subString[i]=="poor"):
            end=i
else:
    for word in subString:
        result=result+" "+word
# Checking their positions
if notCheck and poorCheck:
    if start<end:
        for i in range(len(subString)):
            if i==start:
                result=result+" "+"good!"
                break
            else:
                result=result+" "+subString[i]
                continue
    else:
        for word in subString:
            result=result+" "+word
print(result)