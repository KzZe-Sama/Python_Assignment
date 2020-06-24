# Function that iterates all keys and values of a dictionary
def iterate(data):
    for keys,values in data.items():
        print(keys,values)
# Data
dataA={1:10,2:20,3:30,5:50}
dataB={101:"John",102:"Mary",103:"Edward"}
# invoking function
iterate(dataA)
iterate(dataB)