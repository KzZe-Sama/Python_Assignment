def add_key(data):
   #  List for keys and values
   keyLists=[]
   valuesList=[]
   for key,values in data.items():
       keyLists.append(key)
       valuesList.append(values)
   #     Common Difference between the last and second last element of keys and values
   common_DKeys = keyLists[-1] - keyLists[-2]
   common_DValues = valuesList[-1] - valuesList[-2]
   newKey = keyLists[-1] + common_DKeys
   newValue = valuesList[-1] + common_DValues
   data[newKey] = newValue
   return data
# Data
firstDict={1:10,2:20,3:30,4:40}
secondDict={2:20,4:40}
# Invoking function
print(add_key(firstDict))
print(add_key(secondDict))