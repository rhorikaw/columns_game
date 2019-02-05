# Name: Richmond Horikawa
# ID: 18715219

import gamestate
import methods

if __name__ == "__main__":
    row_num = input()
    col_num = input()
    content = input()
    game = gamestate.Columns_Gamestate(int(row_num), int(col_num), content)
    methods.print_game_board(game)
    while True:
        action = input()
        try:
            methods.input_handler(action, game)
        except gamestate.QuitGameError:
            break    
        except gamestate.GameOverError:
            print('GAME OVER')
            break
        
