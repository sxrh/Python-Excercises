# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out".
#
# Written by Stella Xu and Eric Martin 


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


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s that make it with 2.
# We "colour" the second shape we find by replacing all the 1s that make it with 3.
def colour_shapes():
    k = 2
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] == 1:
                colour_current_shape(i,j,k)
                k +=1
    return (k-2)

def colour_current_shape(i,j,k):
    grid[i][j] = k
    if (j+1 < dim) and (grid[i][j+1] == 1):
        colour_current_shape(i,j+1,k)
    if (i+1 < dim) and grid[i+1][j] == 1:
        colour_current_shape(i+1,j,k)
    if (j-1 >= 0) and (grid[i][j-1] == 1):
        colour_current_shape(i,j-1,k)
    if (i-1 >= 0) and grid[i-1][j] == 1:
        colour_current_shape(i-1,j,k)

def max_number_of_spikes(nb_of_shapes):
    spike_nb = []
    for l in range(nb_of_shapes):
        spike = 0
        for i in range(dim):
            for j in range(dim):
                if grid[i][j] == l+2:
                    if is_spike(i,j,l+2):
                        spike +=1
        spike_nb.append(spike)
    return max(spike_nb)
            
def is_spike(i,j,k):
    if grid[i][j] != k:
        return False
    count_of_neighbours = 0
    if (j+1 < dim) and (grid[i][j+1] == k):
        count_of_neighbours +=1
    if (i+1 < dim) and grid[i+1][j] == k:
        count_of_neighbours +=1
    if (j-1 >= 0) and (grid[i][j-1] == k):
        count_of_neighbours +=1
    if (i-1 >= 0) and grid[i-1][j] == k:
        count_of_neighbours +=1
    if count_of_neighbours > 1:
        return False
    return True   

try:
    for_seed, n = [int(i) for i in
                        input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) != 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
nb_of_shapes = colour_shapes()
print(f'The maximum number of spikes of some shape is equal to {max_number_of_spikes(nb_of_shapes)}')
