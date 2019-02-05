# Name: Richmond Horikawa
# ID: 18715219

class Faller:
    def __init__(self, faller_info: list) -> None:
        'Creates a new faller object'
        self._row_num = 0
        self._col_num = int(faller_info[1])-1
        self._block = [faller_info[4],faller_info[3],faller_info[2]]
        self._landed = False

    def get_row_num(self) -> int:
        'Returns the current row number'
        return self._row_num

    def get_col_num(self) -> int:
        'Returns the current column number'
        return self._col_num

    def get_block(self) -> list:
        'Returns the contents of the block'
        return self._block

    def get_condition(self) -> bool:
        'Returns True if the block has landed on a floor or block'
        return self._landed

    def move_left(self) -> None:
        'Shifts the block one space to the left'
        self._col_num = self._col_num - 1

    def move_right(self) -> None:
        'Shifts the block one space to the right'
        self._col_num = self._col_num + 1

    def fall(self) -> None:
        'Shifts the block one space to the bottom'
        self._row_num = self._row_num + 1

    def rotate(self) -> None:
        'Rotates the block as defined in the project guide'
        self._block.append(self._block[0])
        self._block.remove(self._block[0])

    def land(self) -> None:
        'Lands the block to the bottom'
        self._landed = True
    

class Columns_Gamestate:
    def __init__(self, row: int, col: int, contents: str) -> None:
        'Creates/ Starts a new game'
        self._rows = row
        self._cols = col
        self._board = []
        self._faller = None
        self._clearble = False
        self.initialize_empty_board(row,col)
        if contents == 'CONTENTS':
            self.initialize_board(row,col)

    def initialize_empty_board(self, row: int, col: int) -> None:
        'Creates an empty board'
        for r in range(row):
            self._board.append([])
            for c in range(col):
                self._board[-1].append(' ')

    
    def initialize_board(self, row: int, col: int) -> None:
        'Creates a board filled with specified contents'
        for r in range(row):
            line = input()
            for c in range(col):
                if line != '':
                    if line[c] == ' ':
                        self._board[r][c] == ' '
                    else:
                        self._board[r][c] = '<' + line[c] + '>'
                else:
                    self._board[r][c] = ' '

    def create_faller(self, faller_info: str) -> None:
        'Creates a new faller'
        info_list = faller_info.split()
        self._faller = Faller(info_list)

    def check_top(self) -> int:
        'Returns the amount of blocks that are still not shown'
        return 2 - self._faller.get_row_num()

    def is_at_bottom(self) -> bool:
        'Checks if thte block has reached the bottom'
        if self._faller.get_row_num() == self._rows - 1:
            return True
        elif self._board[self._faller.get_row_num()+1][self._faller.get_col_num()] != ' ':
            return True
        else:
            return False

    def check_right(self) -> bool:
        'Checks whether the faller can move to the right'
        row = self._faller.get_row_num()
        if self._faller.get_condition():
            return False
        adjacent_col = self._faller.get_col_num() + 1
        if adjacent_col >= len(self._board[0]):
            return False
        if self.check_top() == 2:
            return self._check_right_first_block(row,adjacent_col)
        if self.check_top() == 1:
            return self._check_right_first_second_blocks(row,adjacent_col)       
        else:
            return self._check_right_all_blocks(row,adjacent_col)

    def _check_right_first_block(self,row: int,adjacent_col: int) -> bool:
        'Checks if the space to the left of the first faller block is open'
        if  self._board[row][adjacent_col] == ' ':
                return True
        else:
            return False

    def _check_right_first_second_blocks(self,row: int,adjacent_col: int) -> bool:
        'Checks if the space to the left of the first and second faller block is open'
        if  self._check_left_first_block(row,adjacent_col):
            if self._board[row - 1][adjacent_col] == ' ':
                return True
        else:
            return False

    def _check_right_all_blocks(self, row: int, adjacent_col: int) -> bool:
        'Checks if all of the spaces to the left of the faller block is open'
        if self._check_left_first_second_blocks(row,adjacent_col):
            if self._board[row - 2][adjacent_col] == ' ':
                return True
        else:
            return False

    def check_left(self) -> bool:
        'Checks whether the faller can move to the left'
        row = self._faller.get_row_num()
        if self._faller.get_condition():
            return False
        adjacent_col = self._faller.get_col_num() - 1
        if adjacent_col < 0:
           return False 
        if self.check_top() == 2:
            return self._check_left_first_block(row,adjacent_col)
        if self.check_top() == 1:
            return self._check_left_first_second_blocks(row,adjacent_col)        
        else:
            return self._check_left_all_blocks(row,adjacent_col)

    def _check_left_first_block(self,row: int,adjacent_col: int) -> bool:
        'Checks if the space to the left of the first faller block is open'
        if  self._board[row][adjacent_col] == ' ':
                return True
        else:
            return False

    def _check_left_first_second_blocks(self,row: int,adjacent_col: int) -> bool:
        'Checks if the space to the left of the first and second faller block is open'
        if  self._check_left_first_block(row,adjacent_col):
            if self._board[row-1][adjacent_col] == ' ':
                return True
        else:
            return False

    def _check_left_all_blocks(self, row: int, adjacent_col: int) -> bool:
        'Checks if all of the spaces to the left of the faller block is open'
        if self._check_left_first_second_blocks(row,adjacent_col):
            if self._board[row-2][adjacent_col] == ' ':
                return True
        else:
            return False
        
    def clear_current_position(self) -> None:
        'Clears the board of your current position'
        if not self._faller == None:
            row = self._faller.get_row_num()
            col = self._faller.get_col_num()
            if self.check_top() == 2:    
                self._board[row][col] = ' '
            elif self.check_top() == 1:
                self._board[row][col] = ' '
                self._board[row-1][col] = ' '
            else:
                self._board[row][col] = ' '
                self._board[row-1][col] = ' '
                self._board[row-2][col] = ' '

    def convert_landed(self) -> None:
        'Changes frozen blocks into features on the board'
        self.add_block_to_board()
        self._faller = None
        
    def add_block_to_board(self) -> None:
        'Adds the falling block to the board'
        row = self._faller.get_row_num()
        col = self._faller.get_col_num()
        if self.check_top() == 2:    
            self._board[row][col] = self._faller.get_block()[0]
        elif self.check_top() == 1:
            self._board[row][col] = self._faller.get_block()[0]
            self._board[row-1][col] = self._faller.get_block()[1]
        else:
            self._board[row][col] = self._faller.get_block()[0]
            self._board[row-1][col] = self._faller.get_block()[1]
            self._board[row-2][col] = self._faller.get_block()[2]

    def _handle_one_block(self, row_num: int, col_num: int, row: int, col: int) -> str:
        'Returns appropriate string for the appropiate cell when one cell of the faller is in play'
        if row == row_num and col == col_num:
            return self._return_one_block(row_num,col_num,row,col)
        else:
            return self.special_contents(self._board[row][col])

    def _handle_two_blocks(self, row_num: int, col_num: int, row: int, col: int) -> str:
        'Returns appropriate string for the appropiate cell when two cells of the faller is in play'
        if row == row_num - 1 and col == col_num:
            return self._return_second_block(row_num,col_num,row,col)
        else:
            return self._handle_one_block(row_num,col_num,row,col)

    def _handle_three_blocks(self, row_num: int, col_num: int, row: int, col: int) -> str:
        'Returns appropriate string for the appropiate cell when teh whole faller is in play'
        if row == row_num - 2 and col == col_num:
            return self._return_third_block(row_num,col_num,row,col)
        else:
            return self._handle_two_blocks(row_num,col_num,row,col) 
        

    def _return_one_block(self, faller_row: int, faller_col: int, row: int, col: int) -> str:
        'Return the first block of the faller as a string'
        if self._faller.get_condition():
            return '|' + self._board[faller_row][faller_col] + '|'
        else:
            return '[' + self._board[faller_row][faller_col] + ']'

    def _return_second_block(self, faller_row: int, faller_col: int, row: int, col: int) -> str:
        'Return the second block of the faller as a string'
        return self._return_one_block(faller_row - 1,faller_col,row,col)

    def _return_third_block(self, faller_row: int, faller_col: int, row: int, col: int) -> str:
        'Return the third block of the faller as a string'
        return self._return_one_block(faller_row - 2,faller_col,row,col)

    def special_contents(self, cell: str) -> str:
        'Converts cells into strings that are suitable for being printed out'
        if cell.startswith('*'):
            return cell
        elif cell.startswith('<'):
            return ' ' + cell[1] + ' '
        else:
            return ' ' + cell + ' '

    def _read_value_of_cell(self, cell: str) -> str:
        'Reads the value of cells'
        if cell.startswith('*') or cell.startswith('<'):
            return cell[1]
        else:
            return cell

    def _contains_non_init_cell(self, list_of_cells: list) -> bool:
        'Returns True if the list contains a cell that was not initilialized with the board'
        for element in list_of_cells:
            if not element.startswith('<'):
                return True
        return False
        
    
    def _connect_three(self, row: int, col: int, row_change: int, col_change: int) -> bool:
        'Returns true if there are any blocks that can be cleared'
        list_of_cells = [self._board[row][col]]
        start = self._read_value_of_cell(self._board[row][col])
        if start == ' ':
            return False
        else:
            for count in range(1,3):
                if 0 <= col+col_change*count < self._cols and 0 <= row+row_change*count < self._rows:
                    value = self._read_value_of_cell(self._board[row + row_change * count][col + col_change * count])
                    if value != start:
                        return False
                    else:
                        list_of_cells.append(self._board[row + row_change * count][col + col_change * count])
                else:
                    return False
            return self._contains_non_init_cell(list_of_cells)
            

    def _is_clearable(self) -> bool:
        'Checks if there are any clearable blocks at the current gamestate'
        for row in range(self._rows):
            for col in range(self._cols):
                if not self._three_starts_at(row,col) == []:
                    return True
        return False

    def check_clearable_blocks(self) -> None:
        'If there are three or more blocks in a row, it changes those blocks to have "*" surrounding them'
        if self._is_clearable():
            for row in range(0,self._rows):
                for col in range(0,self._cols):
                    for direction in self._three_starts_at(row,col):
                        value = self._read_value_of_cell(self._board[row][col])
                        compare = value
                        count = 0
                        while 0 <= col+direction[1]*count < self._cols and 0 <= row+direction[0]*count < self._rows and compare == value:
                            self._board[row + direction[0] * count][col + direction[1] * count] = '*' + compare + '*'
                            count += 1
                            try:
                                compare = self._read_value_of_cell(self._board[row+direction[0]*count][col+direction[1]*count])
                            except:
                                pass
                                
    def _three_starts_at(self, row: int, col: int) -> list:
        'Returns all the directions where blocks can be cleared'
        list_of_directions = []
        if self._connect_three(row,col,0,1):
            list_of_directions.append([0,1])
        if self._connect_three(row,col,1,1):
            list_of_directions.append([1,1])
        if self._connect_three(row,col,1,0):
            list_of_directions.append([1,0])
        if self._connect_three(row,col,0,-1):
            list_of_directions.append([0,-1])
        if self._connect_three(row,col,1,-1):
            list_of_directions.append([1,-1])
        if self._connect_three(row,col,-1,-1):
            list_of_directions.append([-1,-1])
        if self._connect_three(row,col,-1,0):
            list_of_directions.append([-1,0])
        if self._connect_three(row,col,-1, 1):
            list_of_directions.append([-1,1])
        return list_of_directions

                        
    def clear_blocks(self) -> None:
        'Clears the board of the same blocks placed three in a row'
        for row in range(0,self._rows):
            for col in range(0, self._cols):
                if self._board[row][col].startswith('*'):
                    self._board[row][col] = ' '

    def is_empty_cell(self, row: int, col: int) -> bool:
        'Returns True if there is an empty cell'
        if self._board[row][col] == ' ':
               return True
        else:
            return False

    def is_initialized_cell(self,row:int,col:int) -> bool:
        'Returns True if it is an initialized cell'
        if self._board[row][col].startswith('<'):
            return True
        else:
            return False
                        
    def bring_blocks_down(self, row: int, col: int) -> None:
        'Brings the blocks above the given coordinates down'
        contains_frozen = False
        if row != 0:
            for r in range(row, 0 , -1):
                if self._board[r-1][col].startswith('<'):
                    contains_frozen = True
                    break
                else:
                    self._board[r][col] = self._board[r - 1][col]
            if not contains_frozen:
                self._board[0][col] = ' '
        
class QuitGameError(Exception):
    pass

class GameOverError(Exception):
    pass




