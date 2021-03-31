def rec_search(grid):
    summ = helper(grid, 0, 0)
    return summ

def helper(grid, x, y):

    grid2 = grid[x][y]
    ln = len(grid)
    if (x == (ln - 1)):
        return grid2
    else:
        #call helper
        y2 = (helper(grid, (x + 1), y))
        y3 = (helper(grid, (x + 1), (y + 1)))
        return (grid2 + max(y2, y3))

def main(grid):
    #return recursive solution for the greatest path sum
    return rec_search(grid)