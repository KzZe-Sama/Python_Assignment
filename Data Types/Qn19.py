# DATA
# Smallest Number Finder
items=[300,500,600,800,900,1000,100,1500]
smallestNum=items[0]
for item in items:
    # Control Statement
    if smallestNum>item:
        smallestNum=item
print(f"{smallestNum} is the smallest of them all.")