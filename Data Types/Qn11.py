# Input
string=input("Enter A Sentence\n")
# Spliting the words
listString=string.split()
# Set for unique words
setList=set(listString)
dictSet={}
# mapping keys with values
for word in setList:
    dictSet[word]=listString.count(word)
print(dictSet)
