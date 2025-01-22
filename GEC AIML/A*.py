import heapq

# Node and heuristic setup
start = "A"  # Starting node
goal = "G"   # Goal node
nodes = {
    "A": {"B": 1, "C": 4},   # A has children B and C, costs 1 and 4 respectively
    "B": {"D": 2, "E": 5},   # B has children D and E, costs 2 and 5 respectively
    "C": {"E": 1},           # C has child E, cost 1
    "D": {"G": 3},           # D has child G, cost 3
    "E": {"G": 1},           # E has child G, cost 1
    "G": {}                  # G has no children, it's the goal
}

# Heuristic values (estimated cost to reach the goal)
heuristic = {
    "A": 6,  # Estimated cost to reach G from A
    "B": 5,
    "C": 2,
    "D": 1,
    "E": 1,
    "G": 0  # The goal node has a heuristic of 0
}

# Open list (priority queue) and closed list
open_list = []
closed_list = set()

# Starting node setup
heapq.heappush(open_list, (heuristic[start], 0, start))  # (f_score, g_score, node)
g_score = {start: 0}  # Starting node has a g_score of 0
came_from = {}  # To reconstruct the path

while open_list:
    # Pop the node with the lowest f_score
    current_f, current_g, current_node = heapq.heappop(open_list)

    # If the current node is the goal, reconstruct the path
    if current_node == goal:
        path = []
        while current_node in came_from:
            path.append(current_node)
            current_node = came_from[current_node]
        path.append(start)
        path.reverse()
        print("Path found:", path)
        break

    closed_list.add(current_node)

    # Explore neighbors
    for neighbor, cost in nodes[current_node].items():
        if neighbor in closed_list:
            continue

        tentative_g_score = current_g + cost

        # If the neighbor is not in the open list or we found a better path to it
        if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
            g_score[neighbor] = tentative_g_score
            f_score = tentative_g_score + heuristic[neighbor]
            heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))
            came_from[neighbor] = current_node
else:
    print("No path found.")



