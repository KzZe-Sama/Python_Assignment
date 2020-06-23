# Input
String=input("Enter Words: ")
String=String.strip()
ListString=[]
# Initial Point
initialPoint=0
if " " in String:
    print("Please Enter Data only by comma separation")
    print("Eg:red,blue,white")
else:
    for i in range(len(String)):
        # When comma is found it appends the word with help of string slicing
        if String[i] == ",":
            ListString.append(String[initialPoint:i])
            initialPoint = i + 1
        #     when we reached at last if appends the final value with help of String Slicing
        if i == len(String) - 1:
            ListString.append(String[initialPoint:len(String)])
    SetList = set(ListString)
    finalList = list(SetList)
    # Sorting using sort function
    finalList.sort()
    Result=""
    # Displaying with comma separation
    for word in finalList:
        popIndex=finalList.index(word)
        # As we dont want our last word also to end with comma we use different adding logic here
        if popIndex==len(finalList)-1:
            Result = Result + word
        #     Adding with comma seperation
        else:
            Result = Result + word + ","
    print(Result)


