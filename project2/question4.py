def eve_final_adventure(current_pos, goal_pos, initial_treasure, matrix):
    # 8 neighbours to check
    positions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    INF = float('inf')
    # (x, y) the coordinate *mapping* to (shortest distance to this coordinate, list of coordinate visited)
    toll_costs = {(x, y): (INF, []) for x in range(len(matrix[0])) for y in range(len(matrix))}
    toll_costs[current_pos] = (0, current_pos)
    PQ = [(0, current_pos)]
    routes = []
    remaining_treasure = initial_treasure

    while len(PQ) != 0:
        PQ.sort(key=lambda x: x[0])
        curr_cost, curr_node = PQ.pop(0)
        for index in range(len(positions)):
            new_x = curr_node[0] + positions[index][0]
            new_y = curr_node[1] + positions[index][1]
            if 0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix):
                expected_cost = matrix[new_y][new_x]
                existing_cost_to_next_node = toll_costs[(new_x, new_y)][0]
                if existing_cost_to_next_node > curr_cost + expected_cost:
                    update_tuple = (curr_cost + expected_cost, [curr_node])
                    toll_costs[(new_x, new_y)] = update_tuple
                    PQ_node_list = []
                    for j in range(len(PQ)):
                        PQ_node_list.append(PQ[j][1])
                    if (new_x, new_y) not in PQ_node_list:
                        PQ.append((curr_cost + expected_cost, (new_x, new_y)))

    routes.append(goal_pos)
    while current_pos not in routes:
        focus = routes[0]
        predecessor_list = toll_costs[focus][1]
        if not predecessor_list:
            return None
        routes.insert(0, predecessor_list[0])
    for coordinates in routes:
        curr_score = matrix[coordinates[1]][coordinates[0]]
        remaining_treasure -= curr_score
    return remaining_treasure, routes


if __name__ == '__main__':
    grid = [[1000, 200, float('inf'), 1, 10000, 3, 1],
            [0, 200, float('inf'), 1, 10000, 3, 0],
            [1000, 200, float('inf'), 1, 10000, 3, 1],
            [1000, 200, float('inf'), 1, 10000, 3, 1],
            [1000, 200, float('inf'), 1, 10000, 3, 1],
            [1000, 200, float('inf'), 1, 10000, 3, 1],
            [1000, 200, 1, 1, 10000, 3, 1]]
    print(eve_final_adventure((0, 1), (6, 1), 100000, grid))
    INF = float('inf')
    print(eve_final_adventure((2, 2), (0, 0), 100000, [[0, INF, INF], [INF, INF, INF], [INF, INF, 0]]))
    print(eve_final_adventure((1, 0), (2, 3), 1000, [[100, 0, 100, 100], [1000, 1000, 1000,
                                                                          1000], [10000, 10000, 10000, 10000],
                                                     [100000, 100000, 0, 100000]]))
