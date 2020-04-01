# Naloga3: Vitez in zmaj
# Kosta Leštov, 27171179
# matematika, 3. letnik

def find_on_grid(grid, mark):
    for k in range(len(grid)):
        ln = grid[k]
        if ln.find(mark) != -1:
            return (k, ln.find(mark))


def find_goals(grid, h, w):
    (k0, l0) = find_on_grid(grid, "Z")
    goals = []

    # check up:
    if k0 > 0:
        if grid[k0 - 1][l0] == ".":
            goals.append((k0 - 1, l0))

    # check down:
    if k0 < h-1:
        if grid[k0 + 1][l0] == ".":
            goals.append((k0 + 1, l0))

    # check left:
    if l0 > 0:
        if grid[k0][l0 - 1] == ".":
            goals.append((k0, l0 - 1))

    # check down:
    if l0 < w-1:
        if grid[k0][l0 + 1] == ".":
            goals.append((k0, l0 + 1))

    return goals


def find_starts(grid, goal, h, w):
    starts = []
    (i0, j0) = (goal[0], goal[1])

    # find possibilities in the column -- {grid[i][j0] for i in range(h)}
    i = i0
    while(i >= 0 and (grid[i][j0] not in ["#", "Z"])):
        starts.append((abs(i0 - i), (i, j0)))
        i = i - 1

    i = i0
    while(i < h and (grid[i][j0] not in ["#", "Z"])):
        starts.append((abs(i0 - i), (i, j0)))
        i = i + 1

    # find possibilities in the row -- {grid[i0][j] for j in range(w)}
    j = j0
    while (j >= 0 and (grid[i0][j] not in ["#", "Z"])):
        starts.append((abs(j0 - j), (i0, j)))
        j = j - 1

    j = j0
    while (j < w and (grid[i0][j] not in ["#", "Z"])):
        starts.append((abs(j0 - j), (i0, j)))
        j = j + 1

    starts.sort(reverse = True)
    starts = starts[:-3]
    return starts


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


def slay(grid, shortest_distances, goals, h, w, L):
    answers = []
    for G in goals:
        starts = find_starts(grid[:], G, h, w)
        for start in starts:
            answer = get_answer(shortest_distances, start, L)
            if answer != 0:
                answers.append(answer)
                break
            else:
                answers.append(0)

    print(max(answers))


def solve_maze():
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

    # get initial position
    initial = find_on_grid(grid, "V")

    # get the shortest distances from the initial position
    shortest_distances = bfs(grid, grid_distance, h, w, initial)

    # find the positions the knight has to reach
    goals = find_goals(grid[:], h, w)

    # obtain solution
    slay(grid, shortest_distances, goals, h, w, L)


def main():
    Z = int(input())
    for n in range(Z):
        catch_empty = input()
        solve_maze()

main()

