key=[56,67,90]
values=['a','b','c']

print(dict(zip(key,values)))

d = {}
for i, k in enumerate(key):
    d[k] = values[i]
print(d)

d = {k: values[i] for i, k in enumerate(key)}
print('D',d)

d = dict([(key[i], values[i]) for i in range(len(key))])
print(d)

for i in range(len(key)):
    dict(key[i],values[i])