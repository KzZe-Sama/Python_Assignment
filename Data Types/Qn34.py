def con_dict(dictA,dictB):
    # Creating empty lists
    keyLists = []
    valuesList = []
    # Adding all keys and values in lists
    for key, values in dictB.items():
        keyLists.append(key)
        valuesList.append(values)
    length=len(keyLists)
    i=0
    # While loop until i is not equal to length of the keyList
    while i!=length:
        dictA[keyLists[i]]=valuesList[i]
        i=i+1
    return dictA
# Data
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dicA={101:"Ram",201:"Sita",202:"Geeta"}
dicB={1001:20001,2001:40001}
print(con_dict(dic1,dic2))
print(con_dict(dicA,dicB))
