def greedy (grid):
    summ=grid[0][0]
    leng=len(grid)
    i=1
    j=0
    while i<leng:
        if grid[i][j]>=grid[i][j+1]:
            summ+=grid[i][j]
        else:
            j+=1
            summ+=grid[i][j]
        i+=1
    return summ

def main(grid):
    return greedy(grid)