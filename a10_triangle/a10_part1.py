def exhaustive_search (grid):
    empty=[]
    helper(grid,grid[0][0],1,0,empty)
    return max(empty)

def helper(grid,csum,idx,idx2,alls):
    ln=len(grid)
    if idx==ln:
        alls.append(csum)
        return
    else:
        csum2=csum
        csum+=grid[idx][idx2]
        csum2+=grid[idx][idx2+1]
        helper(grid,csum,idx+1,idx2,alls)
        helper(grid,csum2,idx+1,idx2+1,alls)

def main(grid):
    return exhaustive_search(grid)