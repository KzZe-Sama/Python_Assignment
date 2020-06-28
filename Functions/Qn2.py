# function to sum all data in list
def sum_all(data):
    total=0
    if len(data) !=0:
        for value in data:
            total = total + value
        return total
    else:
        return "Empty List!"
# invoking the function with list
print(sum_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_all([10, 20, 30]))
print(sum_all([]))

