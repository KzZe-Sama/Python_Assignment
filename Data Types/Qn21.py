# Sorts from last -1 represents last element
def last(n):
    return n[-1]

def sort_data(data):
  #   Here key denotes how we are sorting our data
  return sorted(data, key=last)
items=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_data(items))