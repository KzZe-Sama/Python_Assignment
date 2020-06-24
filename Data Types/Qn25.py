def is_empty(data):
    for value in data:
        if len(value)!=0:
            return False
        else:
            return True
print(is_empty([{},{},{}]))
# Returns True
print(is_empty([{1,2},{},{}]))
# Returns False