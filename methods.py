# Name: Richmond Horikawa
# ID: 18715219

import gamestate

def input_handler(user_input: str, game: gamestate.Columns_Gamestate) -> None:
    'Reads the user input and does an action according to the input'
    if user_input.startswith('F'):
        _handle_F_key(game, user_input)
    elif user_input == 'R':
        _handle_R_key(game)
    elif user_input == '<':
        _handle_left_key(game)
    elif user_input == '>':
        _handle_right_key(game)
    elif user_input == 'Q':
        _handle_Q_key(game)
    elif user_input == '':
        _handle_enter_key(game)
    else:
        pass

def _handle_F_key(game: gamestate.Columns_Gamestate, user_input: str) -> None:
    'Creates the faller in the game'
    game.create_faller(user_input)
    print_game_board(game)

def _handle_R_key(game: gamestate.Columns_Gamestate) -> None:
    'Rotates the faller in the game'
    game._faller.rotate()
    print_game_board(game)

def _handle_left_key(game: gamestate.Columns_Gamestate) -> None:
    'Moves the faller to the left in the game'
    game.clear_current_position()
    if game.check_left():
        game._faller.move_left() 
    print_game_board(game)
    
def _handle_right_key(game: gamestate.Columns_Gamestate) -> None:
    'Moves the faller to the right in the game'
    game.clear_current_position()
    if game.check_right():
        game._faller.move_right()
    print_game_board(game)

def _handle_Q_key(game: gamestate.Columns_Gamestate) -> None:
    'Quits the game immediately'
    raise gamestate.QuitGameError()

def _handle_enter_key(game: gamestate.Columns_Gamestate) -> None:
    'Deals with several scenarios when the enter key is pressed'
    if game._faller != None:
        if not game.is_at_bottom():
            _bring_faller_down(game)
        else:
            if not game._faller.get_condition():
                _land_faller(game)
            else:
                _clear_blocks_after_land(game)
        print_game_board(game)
    else:
        _update_board(game)

def _bring_faller_down(game: gamestate.Columns_Gamestate) -> None:
    'Brings the faller down in the game'
    game.clear_current_position()
    game._faller.fall()

def _land_faller(game: gamestate.Columns_Gamestate) -> None:
    'Lands the faller so that it cannot move. Also checks if the game is over'
    game._faller.land()
    if game.check_top() > 0:
        print_game_board(game)
        raise gamestate.GameOverError()

def _clear_blocks_after_land(game: gamestate.Columns_Gamestate) -> None:
    'Clears all of the removable blocks in the game'
    game.convert_landed()
    game.check_clearable_blocks()

def _update_board(game: gamestate.Columns_Gamestate) -> None:
    'Updates the game/gameboard if needed'
    game.clear_blocks()
    for row in range(0, game._rows):
        for col in range(0, game._cols):
            if game.is_empty_cell(row,col):
                game.bring_blocks_down(row,col)
    game.check_clearable_blocks()
    print_game_board(game)

def print_game_board(game: gamestate.Columns_Gamestate) -> None:
    'Prints the current board'
    row_num = -1
    col_num = -1
    if not game._faller == None:
        game.add_block_to_board()
        row_num = game._faller.get_row_num()
        col_num = game._faller.get_col_num()
    for row in range(game._rows):
        line = '|'
        for col in range(game._cols):
            if not game._faller == None:
                if game.check_top() == 2:
                    line += game._handle_one_block(row_num,col_num,row,col)
                elif game.check_top() == 1:
                    line += game._handle_two_blocks(row_num,col_num,row,col)
                else:
                    line += game._handle_three_blocks(row_num,col_num,row,col)
            else:
                line += game.special_contents(game._board[row][col])
        print(line + '|')
    print(' ' + '-' * 3 * game._cols + ' ')



















    
