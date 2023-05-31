#!/usr/bin/env python
# coding: utf-8

# In[4]:


import collections 
from collections import defaultdict
graph = defaultdict(list)

def dfs(visited, graph, root,goal):
    if root not in visited:
        visited.add(root)
        print(root, end=" ")

        for neighbor in graph[root]:
            if neighbor!=goal:
                if neighbor not in visited:

                    dfs(visited, graph, neighbor,goal)

            else:
                print(goal)
                break


n=int(input("\nEnter the number of nodes: "))
for i in range(1, n+1):
    node=input("\nEnter the node: " + str(i)+ " ")
    graph[node]=[]
    adj=int(input("\nEnter the number of nodes adjacent to "+node+ ": "))
    for j in range(1,adj+1):
        adj_node=input("\nEnter the adjacent node: "+ str(j)+ ": ")
        graph[node].append(adj_node)

print("\nGraph is-->", graph)
visited=set()

print("\n-------------DFS----------------")
a=input("\nEnter the start node: ")
g=input("\nEnter the goal node: ")
dfs(visited, graph, a, g)


# In[ ]:




