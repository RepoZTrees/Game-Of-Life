# Game of life.
from copy import deepcopy

def display_grid(grid):
    da = []
    db  = []
    for r in range(0,len(grid)):
        da = []
        for c in grid[r]:
            if c == 0:
                da.append('.')    
            else:
                da.append('*')
        gv_str = ' '.join(da)
        db.append(gv_str)
    
    return "\n".join(db)


def count_live_neighbours(grid, r, c):
    def get(r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            return grid[r][c]
        else:
            return 0

    neighbors_list = [get(r-1, c-1), get(r-1, c), get(r-1, c+1),
                      get(r  , c-1),              get(r  , c+1),
                      get(r+1, c-1), get(r+1, c), get(r+1, c+1)]

    return sum(neighbors_list)

#a = count_live_neighbours(grid,1,2)
#print(a)


def dead_or_alive(grid,r,c):
    neighbours_count = count_live_neighbours(grid,r,c)

    if grid[r][c] == 0:
        if neighbours_count == 3:
            return 1
        else:
            return 0
    else:
        if neighbours_count <2 or neighbours_count >3:
            return 0
        else:
            return 1

# b = dead_or_alive(grid,1,2)
# print(b)


def value_of_next_generation_grid(grid):
    next_gen_grid = deepcopy(grid)
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])
    
    for rows in range(0, number_of_rows):
        for columns in range(0, number_of_columns):
            next_gen_grid[rows][columns] = dead_or_alive(grid,rows,columns)
    return next_gen_grid
            
# xz = value_of_next_generation_grid(grid)
# print(xz)
#--------

def main():
    grid = [[0,0,0],
            [1,1,1],
            [0,0,0]]
    
    for i in range(5):
        print(display_grid(grid))
        print('\n')
        grid = value_of_next_generation_grid(grid)        

main()

#------

# import pdb; pdb.set_trace() #is an interactive source code debugger for Python programs.
# from copy import deepcopy:
"""
For example:

>>> x = [1,2,3]
>>> y = x
>>> print(x,y)
[1, 2, 3] [1, 2, 3]
>>> y.append(4)
>>> print(x,y)
[1, 2, 3, 4] [1, 2, 3, 4]
>>> y.append(5)
>>> print(x,y)
[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
>>> import copy
>>> y = copy.deepcopy(x)
>>> y.append(6)
>>> print(x,y)
[1, 2, 3, 4, 5] [1, 2, 3, 4, 5, 6]

"""
