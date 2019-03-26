# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by Stella Xu and Eric Martin 


import sys
from random import seed, choice
from array_queue import *

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def preferred_paths_to_corners():
    explored_pos = []
    all_paths = ArrayQueue()
    paths = {}
    dirc = {'SE':(1,1),'SW':(-1,1),'NW':(-1,-1),'NE':(1,-1),'S':(0,1),'W':(-1,0),'N':(0,-1),'E':(1,0)}
    next_dirc = {'SE':('SE','E','S'),'SW':('SW','W','S'),'NW':('NW','W','N'),'NE':('NE','E','N')}
    current_dirc = grid[3][3]
    (i,j) = (3,3)
    temp_path = [(3,3)]
    all_paths.enqueue(temp_path)
    next_pos = []
    while len(all_paths) > 0 and len(paths)<4:
        temp_path = all_paths.dequeue()
        #print(temp_path,'temppath1')
        i = temp_path[-1][0]
        j = temp_path[-1][1]
        explored_pos.append((i,j))
        #print(i,j,'ij')
        current_dirc = grid[j][i]
        #print(current_dirc)
        for temp_dirc in next_dirc[current_dirc]:
            #print(temp_dirc,'tempdirc')
            (i1,j1) = (dirc[temp_dirc][0]+i,dirc[temp_dirc][1]+j)
            #print(i1,j1,'i1j1')
            if i1 > dim-1 or i1 < 0 or j1> dim -1 or j1 < 0:
                continue
            #if (i1,j1) in next_pos:
                #continue
            if (i1,j1) in explored_pos:
                continue
            if (i1,j1) in corners:
                if (i1,j1) in paths.keys():
                    continue
                else:
                    final_path = temp_path.copy()
                    final_path.append((i1,j1))
                    paths.update({(i1,j1):final_path})
                    #print(paths)
            else:
                next_pos.append((i1,j1))

        #print(next_pos,'nextpos')

        for temp_pos in next_pos:
            #print(temp_path,'TP')
            #print(temp_pos,'TEMPPos')
            next_path = temp_path.copy()
            next_path.append(temp_pos)
            all_paths.enqueue(next_path)
            #print(next_path,'t2')
        #print(all_paths.peek_at_front())
            next_pos = []

    return paths   
	
	
try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

for i in range(dim):
    for j in range(dim):
        grid[i][j] = choice(directions)
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
