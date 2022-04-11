adjacency_list = {
    "A" : ["B","C"],
    "B" : ["D","E"],
    "C" : ["B","F"],
    "D" : [],
    "E" : ["F"],
    "F" : []
}

status = {} # 1,2,3
parent = {}
dfs_traversal_output = []

#when a vertex is not visited - 1
#when first explored - 2
#when vertex is fully explored - 3

for node in adjacency_list.keys():
    status[node] = "1"
    parent[node] = None
print("-----------------------------Before traversal--------------------")
print("The status and parent of all the nodes at the beginning : ")
print(status)
print(parent)

def dfs_algorithm(u):
    status[u] = "2"
    dfs_traversal_output.append(u)

    for v in adjacency_list[u]:
        if status[v] == "1":
            parent[v] = u
            dfs_algorithm(v)
    status[u] = "3"
dfs_algorithm("A")
print("The depth first traversal is : ")
print(dfs_traversal_output)
print("-----------------------After traversal------------------- ")
print("The parent and status after traversal :")
print(parent)
print(status)