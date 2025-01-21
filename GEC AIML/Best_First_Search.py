graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# Heuristic values for each node
heuristic = {
    0: 10,
    1: 8,
    2: 5,
    3: 7,
    4: 3,
    5: 0  # Assuming node 5 is the goal
}

# Initialization
start_node = 0
goal_node = 5
priority_queue = []
heapq.heappush(priority_queue, (heuristic[start_node], start_node))  # (heuristic, node)
visited = set()
path = []

# Best-First Search
while priority_queue:
    # Get the node with the smallest heuristic value
    _, current = heapq.heappop(priority_queue)
    
    if current in visited:
        continue
    
    # Mark the current node as visited and add it to the path
    visited.add(current)
    path.append(current)
    
    # If the goal is reached, stop
    if current == goal_node:
        break
    
    # Add neighbors to the priority queue
    for neighbor in graph[current]:
        if neighbor not in visited:
            heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

# Output the result
print("Best-First Search Traversal:", path)
