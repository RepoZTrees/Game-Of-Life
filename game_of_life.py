# Game of life.

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

#print(display_grid())

#--------
grid = [[0,1,0],
        [0,1,0],
        [0,1,0]]

def count_live_neighbours(grid, r, c):
    def get(r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            return grid[r][c]
        else:
            return 0

    neighbors_list = [get(r-1, c-1), get(r-1, c), get(r-1, c+1),
                      get(r  , c-1),              get(r  , c+1),
                      get(r+1, c-1), get(r+1, c), get(r+1, c+1)]

    return sum(map(bool, neighbors_list))

#a = count_live_neighbours(grid,0,1)
#print(a)

