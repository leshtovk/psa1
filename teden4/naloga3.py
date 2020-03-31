def find_on_grid(grid, mark):
    for k in range(len(grid)):
        ln = grid[k]
        if ln.find(mark) != -1:
            return (k, ln.find(mark))


def mark_tile(ln, j, mark):
    return ln[:j] + mark + ln[j+1:]


def find_goals(grid, h, w):
    (k0, l0) = find_on_grid(grid, "Z")
    goals = []

    # check up:
    if k0 > 0:
        if grid[k0 - 1][l0] == ".":
            grid[k0 - 1] = mark_tile(grid[k0 - 1], l0, "x")
            goals.append((k0 - 1, l0))

    # check down:
    if k0 < h-1:
        if grid[k0 + 1][l0] == ".":
            grid[k0 + 1] = mark_tile(grid[k0 - 1], l0, "x")
            goals.append((k0 + 1, l0))

    # check left:
    if l0 > 0:
        if grid[k0][l0 - 1] == ".":
            grid[k0] = mark_tile(grid[k0], l0 - 1, "x")
            goals.append((k0, l0 - 1))

    # check down:
    if l0 < w-1:
        if grid[k0][l0 + 1] == ".":
            grid[k0] = mark_tile(grid[k0], l0 + 1, "x")
            goals.append((k0, l0 + 1))

    return (goals, grid)


def find_starts(grid, goal, h, w):
    starts = []
    (i0, j0) = (goal[0], goal[1])

    # find possibilities in the column -- {grid[i][j0] for i in range(h)}
    i = i0
    while(i >= 0 and (grid[i][j0] not in ["#", "Z"])):
        grid[i] = mark_tile(grid[i], j0, "o")
        starts.append((abs(i0 - i), (i, j0)))
        i = i - 1

    i = i0
    while(i < h and (grid[i][j0] not in ["#", "Z"])):
        grid[i] = mark_tile(grid[i], j0, "o")
        starts.append((abs(i0 - i), (i, j0)))
        i = i + 1

    # find possibilities in the row -- {grid[i0][j] for j in range(w)}
    j = j0
    while (j >= 0 and (grid[i0][j] not in ["#", "Z"])):
        grid[i0] = mark_tile(grid[i0], j, "o")
        starts.append((abs(j0 - j), (i0, j)))
        j = j - 1

    j = j0
    while (j < h and (grid[i0][j] not in ["#", "Z"])):
        grid[i0] = mark_tile(grid[i0], j, "o")
        starts.append((abs(j0 - j), (i0, j)))
        j = j + 1

    starts.sort(reverse = True)
    starts = starts[:-3]
    return (starts, grid)


def bfs(grid, grid_distance, h, w, initial):
    visited = []
    queue = [initial]
    grid_distance[initial[0]][initial[1]] = 0

    while queue != []:

        node = queue.pop(0)
        if node not in visited:

            visited.append(node)
            level = grid_distance[node[0]][node[1]] + 1

            # check up:
            if node[0] > 0:
                if grid[node[0] - 1][node[1]] == "." and (node[0] - 1, node[1]) not in visited:
                    queue.append((node[0] - 1, node[1]))
                    grid_distance[node[0] - 1][node[1]] = level

            # check down:
            if node[0] < h-1:
                if grid[node[0] + 1][node[1]] == "." and (node[0] + 1, node[1]) not in visited:
                    queue.append((node[0] + 1, node[1]))
                    grid_distance[node[0] + 1][node[1]] = level

            # check left:
            if node[1] > 0:
                if grid[node[0]][node[1] - 1] == "." and (node[0], node[1] - 1) not in visited:
                    queue.append((node[0], node[1] - 1))
                    grid_distance[node[0]][node[1] - 1] = level

            # check down:
            if node[1] < w-1:
                if grid[node[0]][node[1] + 1] == "." and (node[0], node[1] + 1) not in visited:
                    queue.append((node[0], node[1] + 1))
                    grid_distance[node[0]][node[1] + 1] = level

    return grid_distance


def get_answer(grid_distance, start, L):
    if grid_distance[start[1][0]][start[1][1]] + start[0] <= L:
        return(start[0] + 1)
    else:
        return(0)


def main():
    # h -- number of rows
    # w -- number of columns
    # L -- maximum amount of steps the knight is allowed to take

    # get input
    (w, h, L) = tuple(map(int, input().split()))
    grid = ["" for i in range(h)]
    for k in range(h):
        grid[k] = input()

    # set the initial distances
    grid_distance = [[1111 for j in range(w)] for i in range(h)]

    # print the maze
    for ln in grid:
        print(ln)

    # get initial position
    initial = find_on_grid(grid, "V")
    print("\nInitial position:", initial)

    # get the shortest distances from the initial position
    shortest_distances = bfs(grid, grid_distance, h, w, initial)
    print("\nBFS")
    for ln in shortest_distances:
        print(ln)

    # find the positions the knight has to reach
    (goals, grid_marked) = find_goals(grid[:], h, w)
    print("\nGoals:", goals)
    for ln in grid_marked:
        print(ln)

    # obtain solution
    print("Solution process:")

    answers = []
    for G in goals:
        (starts, grid_circled) = find_starts(grid[:], G, h, w)
        for start in starts:
            print("goal:", G, "start:", start)
            answer = get_answer(shortest_distances, start, L)
            if answer != 0:
                answers.append(answer)
                print("added:", answer)
                break
            else:
                answers.append(0)
                print("added 0")

    print(max(answers))

main()

