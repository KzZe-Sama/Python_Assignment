# data
items=(1,2,3,4,5)
items_list=list(items)
# Before Removing
print(items)
# Removing
items_list.remove(4)
items=tuple(items_list)
# After Removing
print(items)