# Data
items=['20002','abcde','dad','humming','counter','madam']
count=0
# for each loop
for item in items:
    if len(item)>=2:
        if item[0]==item[-1]:
            count=count+1
print(count)