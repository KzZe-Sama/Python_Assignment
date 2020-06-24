def con_dict(dictA,dictB,dictC):
    # Creating empty lists
    keyLists = []
    valuesList = []
    # Adding all keys and values in lists
    for key, values in dictB.items():
        keyLists.append(key)
        valuesList.append(values)
    for key, values in dictC.items():
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
dic3={5:50,6:60,7:70}
print(con_dict(dic1,dic2,dic3))
