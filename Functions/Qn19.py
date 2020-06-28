from functools import reduce
# Function
fibonic = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fibonic(14))