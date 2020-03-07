# Dictionary
Dict = {}
Dict['one'] = "This is one"
Dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(Dict)
print(Dict['one'])  # Prints value for 'one' key
print(Dict[2])  # Prints value for 2 key
print(tinydict)  # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values

Dict = {"A": 3.5, "D": 1.2, "B": 4}

# sorted by value
print(sorted(Dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))

for x in sorted(Dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
    print(x[0], " : ", x[1])

# sorted by key
for i in sorted(Dict):
    print(i, " : ", Dict[i])
