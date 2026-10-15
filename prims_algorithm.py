# prims algorithm.
import heapq

def prims_algorithm(vertices_count, graph):
    visited = [False] * vertices_count
    min_heap = [(0, 0, -1)]
    mst_edges = []
    total_weight = 0
    edges_count = 0

    while min_heap and edges_count < vertices_count:
        weight, u, parent = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_weight += weight
        
        if parent != -1:
            mst_edges.append((parent, u, weight))
            edges_count += 1
            
        for next_weight, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (next_weight, v, u))
                
    if len(mst_edges) == vertices_count - 1 or vertices_count == 1:
        return total_weight, mst_edges
    else:
        return float('inf'), []

if __name__ == "__main__":
    V = 5
    adj_list = {i: [] for i in range(V)}
    
    def add_edge(u, v, w):
        adj_list[u].append((w, v))
        adj_list[v].append((w, u))

    add_edge(0, 1, 2)
    add_edge(0, 3, 6)
    add_edge(1, 2, 3)
    add_edge(1, 3, 8)
    add_edge(1, 4, 5)
    add_edge(2, 4, 7)
    add_edge(3, 4, 9)

    mst_weight, mst_structure = prims_algorithm(V, adj_list)
    
    print(f"Total MST Weight: {mst_weight}")
    for edge in mst_structure:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")
