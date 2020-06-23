# DATA
# Largest Number Finder
items=[300,500,600,800,900,1000,100,1500]
largestNum=0
for item in items:
    # Control Statement
    if largestNum<item:
        largestNum=item
print(f"{largestNum} is the largest of them all.")