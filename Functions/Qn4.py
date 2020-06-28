# Function that reverses string
def reverse_string(string):
    new_string=""
    for value in string:
        new_string=value+new_string
    return new_string
print(reverse_string("hello"))
print(reverse_string("madam"))

