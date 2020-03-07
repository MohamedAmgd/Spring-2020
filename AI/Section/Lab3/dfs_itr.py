
from asyncio import LifoQueue
def dfs_iterative(graph, start):
    stack = LifoQueue(30)
    stack.put_nowait(start)
    path = []
    # stack, path = [start], []
    while not stack.empty():
        vertex = stack.get_nowait()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in reversed(graph[vertex]):
            stack.put_nowait(neighbor)

    return path


graph1 = {1: [2, 3], 2: [4, 5],
          3: [5], 4: [6], 5: [6],
          6: [7], 7: []}

print(dfs_iterative(graph1, 1))

graph2 = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': [],
         'F': []}
print(dfs_iterative(graph2, 'A'))
