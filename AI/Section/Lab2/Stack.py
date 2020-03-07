
# from queue import LifoQueue
from asyncio import LifoQueue
L = LifoQueue(maxsize=6) 


print(f'size={L.qsize()}') 

# Data Inserted as 5->9->1->7, 
# same as Queue 
L.put_nowait(5) 
L.put_nowait(9) 
L.put_nowait(1) 
L.put_nowait(7) 
L.put_nowait(9) 
L.put_nowait(10) 
print("Full: ", L.full()) 
print("Size: ", L.qsize()) 

# Data will be accessed in the 
# reverse order Reverse of that 
# of Queue 
print(L.get_nowait()) 
print(L.get_nowait()) 
print(L.get_nowait()) 
print(L.get_nowait()) 
print(L.get_nowait()) 
print("Empty: ", L.empty()) 
