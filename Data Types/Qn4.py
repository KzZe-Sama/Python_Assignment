string_one=input("Enter First String:")
string_second=input("Enter Second String:")
# Getting Values from indexes
swapA1=string_one[0]
swapA2=string_one[1]
swapB1=string_second[0]
swapB2=string_second[1]
string_one=string_one.replace(swapA1,swapB1)
string_one=string_one.replace(swapA2,swapB2)
string_second=string_second.replace(swapB1,swapA1)
string_second=string_second.replace(swapB2,swapA2)
final_String=string_one+" "+string_second
print(final_String)