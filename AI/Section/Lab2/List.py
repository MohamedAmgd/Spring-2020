List = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (List)          # Prints complete list
print (List[0])       # Prints first element of the list
print (List[-1])      # prints last element of the list
print (List[1:3])     # Prints elements starting from 2nd till 3rd 
print (List[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (List + tinylist) # Prints concatenated lists

print (List[::1])
print (List[::-1])
print (List[::2])
print (List[::-2])
print (List[1::2])
print (List[3::-1])


List[0] = 222
print (List)

for x in List:
  print(x)
  
print(len(List))

List.append("orange")
print(List)

List.insert(1, "orange")
print(List)

List.remove("orange") 
#  remove first match 
print(List)

List.pop()  
# last element
print(List)

List.pop(0)
print(List)

del List[0]
print(List)

List.clear()
print(List)
List.append(1)
del List
#print(List)
#List.append(2)

#list() Constructor

thislist = list(["apple", "banana", "cherry"])
print(thislist)

print(thislist.count("apple"))

cars = ['Ford', 'BMW', 'Volvo']
thislist.extend(cars)
print(thislist)

points = [1, 4, 5, 9]
thislist.extend(points)
print(thislist)

x = thislist.index("cherry")
print(x)

thislist.reverse()
print(thislist)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)
cars.sort(reverse=True, key=myFunc)
print(cars)

L = [3,5,1,7,9,0]
print(min(L))
print(max(L))
print(sum(L))

import numpy as np
L= [1,2,1,3,1]
print(list(np.unique(L)))
