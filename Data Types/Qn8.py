# Input
String=input("Enter A String:")
print(String)
# Input index nth value
n=int(input("Which index you want to remove:"))
# Replacing the index with empty char
String=String.replace(String[n],"")
print(String)