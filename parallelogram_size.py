# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()

#pre-deal with the grid, transform to all 1 or 0 matrix
def trans_grid():
    for i in range (dim):
        for j in range(dim):
            if grid[i][j]:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid

# first transform rows of counts of consecutive above 1s
def count_consecutive_above_1s(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1,m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = grid[i-1][j] +1
    #if only 1, we count it as 0 as we need at least 2 1s
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
    return grid

# second, compute the max_area of each row
def max_each_row(row):
    row.append(0)
    position = []
    count_neighbour = []
    max_row_area = 0
    for i in range(len(row)):
        if row[i]== 1:
            count = 0
        else:
            count = row[i]
        if len(count_neighbour)== 0 or count > count_neighbour[-1]:
            position.append(i)
            count_neighbour.append(count)
        elif count < count_neighbour[-1]:
            while len(count_neighbour) and count < count_neighbour[-1]:
                previous_position = position.pop()
                previous_count = count_neighbour.pop()
                if i-previous_position > 1:
                    current_area = previous_count*(i-previous_position)
                else:
                    current_area = 0
                max_row_area = max(max_row_area,current_area)
            position.append(previous_position)
            count_neighbour.append(count)
    while len(count_neighbour):
        previous_position = position.pop()
        previous_count = count_neighbour.pop()
        current_area = previous_count*(i-previous_position)
        max_row_area = max(max_row_area,current_area)
    return max_row_area

#Third, compute the max_area of the whole grid by iterating through each row for unshifted condition
def unshifted_max_area(grid):
    max_area = 0
    count_grid = count_consecutive_above_1s(grid)
    for i in range(len(grid)):
        max_area = max(max_area, max_each_row(count_grid[i]))
    return( max_area)

#finally, include the left direction/right direction special cases in by shifting them back to horizontal/vertical


def size_of_largest_parallelogram(grid):
    #Left direction - shift matrix
    left_matrix = [[0 for _ in range(2*dim-1)] for _ in range(dim)]

    for i in range(len(grid)):
    	for j in range(len(grid[0])):
    		left_matrix[i][j+i] = grid[i][j]
    max_left = unshifted_max_area(left_matrix)

    #right direction - shift matrix
    right_matrix = [[0 for _ in range(2*dim-1)] for _ in range(dim)]

    for i in range(len(grid)):
    	for j in range(len(grid[0])):
    		right_matrix[i][dim+j-i-1] = grid[i][j]
    max_right = unshifted_max_area(right_matrix)

    max_unshifted = unshifted_max_area(grid)

    max_overall = max(max_left,max_right,max_unshifted)
    return max_overall
                

try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

trans_grid()

size = size_of_largest_parallelogram(grid)
if size:
    print('The largest parallelogram with horizontal sides has a size of', size, end = '.\n')
else:
    print('There is no parallelogram with horizontal sides.')
            

