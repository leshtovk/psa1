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
    return (starts, grid)

def main():
    # h -- number of rows
    # w -- number of columns
    # L -- maximum amount of steps the knight is allowed to take

    # get input
    (w, h, L) = tuple(map(int, input().split()))
    grid = ["" for i in range(h)]
    for k in range(h):
        grid[k] = input()

    # print the maze
    print("\nInput maze")
    for ln in grid:
        print(ln)


    # print an example
    print("\nExample situation")

    # get starting position
    (i0, j0) = find_on_grid(grid, "V")
    print("start:", (i0, j0))

    # set the goal
    (goals, grid_marked) = find_goals(grid[:], h, w)
    G = goals[1]
    print("chosen goal:", G)

    # set the start of the final straight line
    (starts, grid_circled) = find_starts(grid[:], G, h, w)
    start = starts[0]
    print("start of final line:", start)

    # print the example maze
    example_grid = grid[:]
    example_grid[start[1][0]] = mark_tile(example_grid[start[1][0]], start[1][1], "o")
    example_grid[G[0]] = mark_tile(example_grid[G[0]], G[1], "x")
    for ln in example_grid:
        print(ln)

main()

