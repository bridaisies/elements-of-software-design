# Input: dim is a positive odd integer
# Output: function returns a 2-D list of integers arranged in a spiral

# Input: grid a 2-D list containing a spiral of numbers
#        val is a number within the range of numbers in the grid
# Output: sum_sub_grid returns the sum of the numbers (including val)
#         surrounding the parameter val in the grid
#         if val is out of bounds, returns -1

def create_spiral(dim):

    spiral_grid = []

    low_bound = 0
    high_bound = dim


    for i in range(dim):
	row = []
	for j in range(dim):
	    row.append(0)
	spiral_grid.append(row)

    counter = dim * dim;

    for i in range((dim + 1) // 2):
	for j in range(high_bound - 1, low_bound -1, -1):
	    spiral_grid[i][j] = counter
	    counter -= 1

    	for j in range(low_bound + 1, high_bound):
 	    spiral_grid[j][i] = counter
 	    counter -= 1

	for j in range(low_bound+1, high_bound):
 	    spiral_grid[dim-1-i][j] = counter
 	    counter -= 1

	for j in range(high_bound - 2, low_bound, -1):
 	    spiral_grid[j][dim -1 -i] = counter
 	    counter -= 1

 	low_bound += 1
 	high_bound -= 1

    return spiral_grid

def sum_sub_grid (grid, val):

    for i in range(len(grid)):
	for j in range(len(grid)):
 	    if grid[i][j] == val:
 		surrounding_nums = [
 		    [i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
 		    [i, j - 1], [i, j], [i, j + 1],
		    [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]

 		total = 0

 		for i, j in surrounding_nums:
 		    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid):
 			pass
 		    else:
 			total += grid[i][j]

 		return total
     return -1

def main(dim,val):
 
    if (dim % 2 == 0 ):
	dim += 1

    if (val > dim * dim):
 	print(-1)
 	return

    grid = create_spiral(dim)

    s = sum_sub_grid(grid,val)

    return s