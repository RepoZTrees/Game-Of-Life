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

    
def test_count_live_neighbours():
# count_live_neighbours(grid,r,c). So (0,2 is row0, column2)

    assert game_of_life.count_live_neighbours([[0,1,0],
                                               [0,1,0],
                                               [0,1,0]], (1),(0)) == 3

    assert game_of_life.count_live_neighbours([[0,1,1],
                                               [0,1,0],
                                               [0,1,1]], (1),(2)) == 5

    assert game_of_life.count_live_neighbours([[0,1],
                                               [0,1,0]], (0),(0)) == 2
                                                                                                           

def test_live_cell_no_neighbours_dies():
    assert game_of_life.dead_or_alive([[0,0,0],
                                       [0,0,0],
                                       [0,1,0]], (2),(1)) == 0


"""
#select all, alt ;

def test_live_cell_one_neighbours_dies():
    assert game_of_life.dead_or_alive([[1,1,0],
                                       [0,0,0],
                                       [0,1,0]], (0),(0)) == 0

    
def test_live_cell_two_neighbours_live():
    assert game_of_life.dead_or_alive([[1,1,0],
                                       [0,1,0],
                                       [0,1,0]],(0),(0)) == 1 

def test_live_cell_three_neighbours_live():
    assert game_of_life.dead_or_alive([[0,1,0],
                                       [1,1,0],
                                       [0,1,0]],(1),(0)) == 1


def test_live_cell_more_than_three_neighbours_dies():
    assert game_of_life.dead_or_alive([[1,1,0],
                                       [1,1,0],
                                       [0,1,0]],(1),(1)) == 0


def test_dead_cell_two_neighbours_remains_dead():
    assert game_of_life.dead_or_alive([[0,1,0],
                                       [0,1,0],
                                       [1,1,0]],(0),(0)) == 0


def test_dead_cell_three_neighbours_realive():
    assert game_of_life.dead_or_alive([[0,1,0],
                                       [0,1,0],
                                       [0,1,0]],(1),(0)) == 1


def test_dead_cell_more_than_three_neighbours_remains_dead():
    assert game_of_life.dead_or_alive([[1,1,0],
                                       [0,1,0],
                                       [1,1,0]],(1),(0)) == 0

"""

