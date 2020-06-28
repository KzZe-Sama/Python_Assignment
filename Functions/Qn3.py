# function to multiply all data in list
def sum_all(data):
    total=1
    if len(data) !=0:
        for value in data:
            total = total * value
        return total
    else:
        return "Empty List!"
# invoking the function with list
print(sum_all([1, 2, 3, 4, 5]))
print(sum_all([-10, 200, 5]))
print(sum_all([]))

