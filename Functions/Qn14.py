# Function
keySort=lambda a:a['age']
# data
dataA=[{"Name":"John","age":40,"Job":"Doctor"},{"Name":"Ibrahim","age":25,"Job":"Medic"},{"Name":"Anna","age":22,"Job":"Accountant"},{"Name":"Tommy","age":35,"Job":"BusinessMan"},{"Name":"Clara","age":22,"Job":"Engineer"}]
x=sorted(dataA,key=keySort)

print(x)