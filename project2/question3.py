def eve_shortest_path(start_pos, goal_pos, matrix):
    positions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    node = start_pos
    unexplored = [node]
    explored = set()
    movements = {}
    route = []

    while len(unexplored) != 0:
        node = unexplored.pop(0)
        explored.add(node)
        movements[node] = []

        for index in range(0, len(positions)):
            child = (node[0] + positions[index][0], node[1] + positions[index][1])
            # Goal Found
            if child == goal_pos:
                route.append(node)
                route.append(child)
                while start_pos not in route:
                    for key in movements.keys():
                        if node in movements[key]:
                            route.insert(0, key)
                            node = key
                score = 0
                for position in route:
                    score += matrix[position[1]][position[0]]
                return route, score
            # Adding children to unexplored queue
            if 0 <= child[0] < len(matrix[0]) and 0 <= child[1] < len(matrix) and child not in explored:
                unexplored.append(child)
                movements[node].append(child)
                explored.add(child)


if __name__ == '__main__':
    print(eve_shortest_path((0, 0), (3, 1), [[0] * 4] * 4))
    print(eve_shortest_path((0, 0), (3, 6), [[0, 0, -1000, -1000, -1000, 0, 0, 0]] * 6 + [[0, 0,
                                                                                           10000, 0, -1000, 0, 0, 0]]))
    print(eve_shortest_path((0, 5), (7, 5), [[-146, 66, -715, -612, -545, 387, -699, 564,
                                              591], [740, 775, 626, -875, -776, 795, 958, 639, 279],
                                             [-421, -242, -838, -106, -671,
                                              -115, 881, -851, -614],
                                             [705, -925, -532, -418, 403, -221, -797, -891, -246], [894, 856,
                                                                                                    -967, -187, -49,
                                                                                                    715, -262, 716,
                                                                                                    -287],
                                             [458, -980, 954, 595, -889, 561, -402, 488,
                                              324], [158, -21, 38, -890, -644, -644, 980, 731, -810],
                                             [-190, 981, 156, -720, -235,
                                              558, -144, -786, 75], [272, 441, 374, 537, -758, -507, 174, 229, -53]]))
