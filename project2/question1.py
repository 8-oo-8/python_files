def road_to_freedom(current_pos, goal_pos, matrix):
    heuristics = {}
    positions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    for index in range(0, len(positions)):
        i = positions[index][0]
        j = positions[index][1]
        new_x = current_pos[0] + i
        new_y = current_pos[1] + j
        if 0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix):
            next_pos = (new_x, new_y)
            next_score = matrix[next_pos[1]][next_pos[0]]
            next_distance = abs(goal_pos[0] - next_pos[0]) + abs(goal_pos[1] - next_pos[1])
            heuristic = next_score - 100 * next_distance
            if heuristic not in heuristics.keys():
                heuristics[heuristic] = next_pos
            else:
                previous_distance = abs(heuristics[heuristic][0] - goal_pos[0]) + abs(
                    heuristics[heuristic][1] - goal_pos[1])
                if previous_distance > next_distance:
                    heuristics[heuristic] = next_pos
    highest_score = max(heuristics.keys())
    return heuristics[highest_score]


if __name__ == '__main__':
    print(road_to_freedom((0, 0), (2, 2), [[0, 1000, -500], [1500, 1000, 1000], [-500, 0, 1000]]))
    print(road_to_freedom((0, 1), (2, 0), [[1000, 0, 1500], [1000, 1000, 0], [-500, 0, 0]]))
    print(road_to_freedom((1, 1), (1, 2), [[1000, 1000, 1500], [1000, 0, 0], [1500, 1000, 1000]]))
