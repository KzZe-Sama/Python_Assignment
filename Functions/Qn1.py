# function
def greatest_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
#passing parameters in function and displaying greatest one
print(f"{greatest_three(30,40,50)} is the greatest")
print(f"{greatest_three(300,500,900)} is the greatest")
print(f"{greatest_three(3,4,5)} is the greatest")