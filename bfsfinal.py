from queue import Queue

# a dictionary indicating the nodes and the number of there adjacent nodes
adjacent_nodes_list = {
    "A" : ["B","C","D"],
    "B" : ["E"],
    "C" : ["B","G"],
    "D" : ["C","G"],
    "E" : ["C","F"],
    "F" : ["C","H"],
    "G" : ["F","H","I"],
    "H" : ["E","I"],
    "I" : ["F"]
}


#data structures required during the algorithm

visited = {}
parent = {}
queue = Queue()
level = {}

bfs_output_list = []

for node in adjacent_nodes_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1 # can be infinity also 
print(visited)
print(level)
print(parent)

#for the source node 
source_node = "A"
visited[source_node] = True
level[source_node] = 0
parent[source_node] = None
queue.put(source_node)

while not queue.empty():
    u = queue.get()
    bfs_output_list.append(u)
    
    for v in adjacent_nodes_list[u]:
        if not visited[v]:
            visited[v] = True
            level[v] = level[u] + 1
            parent[v] = u
            queue.put(v)
print(bfs_output_list)
print(parent)       
print(level)
