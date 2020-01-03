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
