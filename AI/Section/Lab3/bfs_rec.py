
def bfs_recursive(graph, vertex, path=[]):
    if vertex not in path:
      path += [vertex]
    temp =[]
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path += [neighbor]
            temp += [neighbor]

    for v in temp:
        path = bfs_recursive(graph, v, path)

    return path


graph1 = {1: [2, 3], 2: [4, 5],
          3: [5], 4: [6], 5: [6],
          6: [7], 7: []}

print(bfs_recursive(graph1, 1))

graph2 = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': [],
         'F': []}
print(bfs_recursive(graph2, 'A',[]))



