#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BFS
import collections
from collections import defaultdict

graph=defaultdict(list)

def bfs(graph, root, goal):
    visited, queue=set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex=queue.popleft()
        print(str(vertex) + " ",end=" ")
        if vertex!=goal:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        else:
            queue=[]


n=int(input("\nEnter the number of nodes: "))
for i in range(1,n+1):
    node=input("\nEnter the node: " + str(i) + " : ")
    graph[node]=[]
    adj=int(input("\nEnter the number of nodes adjacent to " + node + ":"))
    for j in range(1, adj+1):
        adj_node=input("\nEnter the adj node " + str(j) +" : ")
        graph[node].append(adj_node)

print("\nGraph is --> ", graph)
visited=set()


while True:
    print("\n----------------BFS for a graph------------------")
    a=input("\nEnter the start node: ")
    g=input("\nEnter the goal node: ")
    bfs(graph,a,g)



# In[ ]:




