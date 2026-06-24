import heapq

def a_star_search(graph, heuristic, start, goal):

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    f_cost = {node: float('inf') for node in graph}
    f_cost[start] = heuristic[start]

    while open_set:

        current = heapq.heappop(open_set)[1]

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, g_cost[goal]

        for neighbor, cost in graph[current].items():

            temp_g_cost = g_cost[current] + cost #total travel cost

            if temp_g_cost < g_cost[neighbor]:

                came_from[neighbor] = current
                g_cost[neighbor] = temp_g_cost

                f_cost[neighbor] = ( 
                    g_cost[neighbor] +
                    heuristic[neighbor]
                )

                heapq.heappush(
                    open_set,
                    (f_cost[neighbor], neighbor)
                )

    return [], 0