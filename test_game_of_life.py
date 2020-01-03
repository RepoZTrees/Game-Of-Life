# Test file for Game of Life.

import game_of_life

def test_display_grid():

    expected_grid_value = """. * .
. * .
. * ."""
    
    grid_value = game_of_life.display_grid(grid = [[0,1,0], [0,1,0], [0,1,0]])

    assert game_of_life.display_grid([[0,0,0],[0,0,0],[0,0,0]]) == '. . .\n. . .\n. . .'

    assert game_of_life.display_grid([[0,1],[1,0]]) == '. *\n* .'
        
    assert grid_value == expected_grid_value

