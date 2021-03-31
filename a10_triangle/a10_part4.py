def dynamic_prog(grid):

    summ = 0 
    ln = len(grid)
    for x in range ((ln - 1), 0, -1):
        for y in range (x):
            grid2 = grid[x][y]
            if(grid2 < grid[x][y + 1]):
                grid[x - 1][y] = grid[x - 1][y] + grid[x][y + 1]
            else:
                grid[x - 1][y] = grid[x - 1][y] + grid2
    
            summ = grid[0][0]
    return summ

def main(grid):
    #return greatest path sum
    return dynamic_prog(grid)