import game_of_life

def test_initialize_grid():
    grid_actual_value = initialize_grid()
    grid_expected_value = [[0,0,0,
                   0,0,0,
                   0,0,0]]
    assert grid_actual_value == grid_expected_value
    
