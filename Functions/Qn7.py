# Function that checks and counts upper and lower cases in a string
def count_cases(String):
    String=String.strip()
    upperCount=0
    lowerCount=0
    for char in String:
        if char==" ":
            continue
        elif char.isupper():
            upperCount=upperCount+1
        else:
            lowerCount=lowerCount+1
    return upperCount,lowerCount
if __name__=="__main__":
    enter=input("Enter a String:\n")
    (a,b)=count_cases(enter)
    print(f"Upper Cases:{a}")
    print(f"Lower Cases:{b}")

