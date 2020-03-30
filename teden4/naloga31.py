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
            # grid[k0 - 1] = mark_goal(grid[k0 - 1], l0, "x")
            goals.append((k0 - 1, l0))

    # check down:
    if k0 < h-1:
        if grid[k0 + 1][l0] == ".":
            # grid[k0 + 1] = mark_goal(grid[k0 - 1], l0, "x")
            goals.append((k0 + 1, l0))

    # check left:
    if l0 > 0:
        if grid[k0][l0 - 1] == ".":
            # grid[k0] = mark_goal(grid[k0], l0 - 1, "x")
            goals.append((k0, l0 - 1))

    # check down:
    if l0 < w-1:
        if grid[k0][l0 + 1] == ".":
            # grid[k0] = mark_goal(grid[k0], l0 + 1, "x")
            goals.append((k0, l0 + 1))

    return goals

def find_path(grid, w, h, i, j, goal):

    # went out of the grid
    i_in_bounds = i >= 0 and i <= h - 1
    j_in_bounds = j >= 0 and j <= w - 1
    if not (i_in_bounds and j_in_bounds):
        return False

    # on an illegal tile
    if grid[i][j] not in [".", "V"]:
        return False

    # mark the tile
    grid[i] = mark_tile(grid[i], j, "#")

    # base case
    if (i, j) == goal:
        return True

    # can we get to `goal`
    if find_path(grid, w, h, i - 1, j, goal) == True:
        print("passed:", (i - 1, j))
        return True
    elif find_path(grid, w, h, i + 1, j, goal) == True:
        print("passed:", (i + 1, j))
        return True
    elif find_path(grid, w, h, i, j - 1, goal) == True:
        print("passed:", (i, j - 1))
        return True
    elif find_path(grid, w, h, i, j + 1, goal) == True:
        print("passed:", (i, j + 1))
        return True

    # couldn't get to `goal`
    return False


def main():
    # h -- number of rows
    # w -- number of columns
    # L -- maximum amount of steps the knight is allowed to take

    # get input
    (w, h, L) = tuple(map(int, input().split()))
    grid = ["" for i in range(h)]
    for k in range(h):
        grid[k] = input()

    # set goal
    goals = find_goals(grid, h, w)
    G = goals[0]
    print("goal:", G)

    # get starting position
    (i0, j0) = find_on_grid(grid, "V")
    print("start:", i0, j0)

    # print the maze
    for ln in grid:
        print(ln)


main()

