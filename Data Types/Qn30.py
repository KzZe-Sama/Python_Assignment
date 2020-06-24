def does_exist(key,dictA):
    # Checking if key exists already
    if key in dictA:
        return True
    else:
        return False
# Data
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(does_exist(1,dic1))
print(does_exist(7,dic2))
print(does_exist(5,dic3))