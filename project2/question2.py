def heuristic_score(next_pos, goal_pos, score):
    distance = abs(next_pos[0] - goal_pos[0]) + abs(next_pos[1] - goal_pos[1])
    final_score = score - 100 * distance
    return final_score


def build_pq(current_pos, goal_pos, matrix):
    rtn = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == j == 0):
                new_x = current_pos[0] + i
                new_y = current_pos[1] + j
                if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix):
                    next_pos = (new_x, new_y)
                    score = matrix[next_pos[1]][next_pos[0]]
                    corresponding_score = heuristic_score(next_pos, goal_pos, score)
                    rtn.append((next_pos, corresponding_score))
    rtn.sort(key=lambda x: x[0][1], reverse=True)
    rtn.sort(key=lambda x: x[0][0], reverse=True)
    rtn.sort(key=lambda x: x[1], reverse=True)
    return rtn


if __name__ == '__main__':
    print(build_pq((0, 0), (2, 2), [[0, 150, -10], [100, 0, 20], [1, 1000, -10]]))
    print(build_pq((1, 1), (2, 2), [[0, 1000, -10], [100, 0, 1000], [1, 1000, -10]]))
    print(build_pq((2, 2), (0, 0), [[1000, 1000, -10], [100, 0, 1001], [1, 1000, 0]]))
