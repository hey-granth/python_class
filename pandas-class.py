import pandas as pd
# s = pd.Series([145,142,38,13],name='counts')
# print(s)
# print(s.index)
#
# t = pd.Series([145,142,38,13],name='counts',index=['john','bob','Rohan','jolly'])
# print(t)
#
# nan_ex = pd.Series([2,None,3,None])
# print(nan_ex)
#
# create a series
s = pd.Series([1, 2, 3, 4, 5])
print(s)
print(s.count())

x = pd.read_csv('stores.csv')
print(x)
print(x.head())

for item in x:
    print(item)

for idx in s.keys():
    print(idx, '=>', s[idx])

