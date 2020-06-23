def longestOne(Sentence):
    Sentence=Sentence.strip()
    # Spliting the words in list
    SentenceList=Sentence.split()
    length=0
    longWord=""
    for word in SentenceList:
        # Checking the word length on loop with respect to previous length
        if(length<len(word)):
            length=len(word)
            longWord=word
    return length,longWord
# Input
String=input("Enter A Sentence\n")
print("The String of Longest Word Found Was:",longestOne(String)[0],"and the word was ",longestOne(String)[1])

