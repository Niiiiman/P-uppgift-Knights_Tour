class Round:
    """
    Attributes:

    allowed_positions:   A list of coordinates, where the knight is allowed to move, the first one is 
                         up to the left from the knight. The symbols will be a-h.
    previous_positions:   A sorted list of coordinates, where the first coordinate is the first   
                        move, the second is the second move... The symbols on the board will   
                        be 1, 2, 3, 4..
    board_matrix:        12x12 grid representing the board
    current_position:    current coordinate of the knight
    """

    def __init__(self, start_position):
        """
        Creates a new Round with current_position as starting position
        """
        self.board = [
                            [-1,  -1, -1, -1, -1, -1, -1, -1  -1, -1,   -1,-1],#0
                            [-1,  -1, -1, -1, -1, -1, -1, -1  -1, -1,   -1,-1],#1
    
                            [-1,   8,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],#2
                            [-1,   7,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],#3
                            [-1,   6,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],#4
                            [-1,   5,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],#5
                            [-1,   4,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],#6
                            [-1,   3,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],#7
                            [-1,   2,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],#8
                            [-1,   1,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],#9
                                
                            [-1,  -1, 'A','B','C','D','E','F','G','H',  -1,-1],#10

                            [-1,  -1, -1, -1, -1, -1, -1, -1, -1, -1,   -1,-1],#11
                            # 0    1   2   3   4   5   6   7   8   9    10 11
                            ]
        
        self.current_position = self.translate_move_for_matrix(start_position)
        self.allowed_positions = []
        self.previous_positions = {}
        
        self.previous_dict_key = 0
        self.previous_positions[self.previous_dict_key] = self.current_position
        
        """
        OBS
        self.board[row][col] will get the element on that row and col of the matrix,
        not the playable board
        
        The playable board will be accessed by the following logic:
        
        position = A1
        "1" means row = 9 and "A" means col = 2
        
        position = A1
        row = 10 - int(postion[1]) 
        col = self.board[10].index(postion[0])
        
        self.board[row][col]
        """
        

#row[col] blir värdet på den positionen, 0 eller X eller b, eller 2
#id_row är nummer i matrisen (0-11)

    def print_board(self):
        """
        Prints the board row by row
        """
        
        allowed_list_index = 2
        previous_keys_list_index = 0

        print("Come on champ! Next move:")
        print("PREV: " + str(self.previous_positions))
        print("CURR: " + str(self.current_position))

        print("-"*40)
        for id_row, row in enumerate(self.board): #Cycles through each row

            if id_row >= 2 and id_row <= 10: #We don't want to print the outlines of the matrix
                print("|   "  + ("-"*33) + "  |")
                
                if id_row != 10:
                    print("|" + str(row[1]), end=" ") #row 10 is the ['A', 'B', ...] list, we don't want to print the row[1] here (-1).
                else:
                    print("|  ", end="")
                
                for col in range(2,10): #Cycles through each square in one row
                    print(" | ", end="")

                    if [id_row, col] == self.current_position:
                        print("X", end="") #Print the knight                        

                    elif [id_row, col] in self.previous_positions.values():
                        for key, value in self.previous_positions.items():
                            if value == [id_row, col]:
                                print(key, end="")  
                                break
                                        #Prints the history of where the knight has been
                                        #This will look ugly after 9.

                    elif [id_row, col] in self.allowed_positions:
                        print(str((self.board[10][allowed_list_index]())).lower(), end="") #str.board[10] points at the list ['A', 'B', ...]
                        allowed_list_index += 1                                            #And allowed positions will be marked by 'a','b', ...
                        #allowed_index starts at 2 because that points at A in row 10 of the matrix.
                    elif id_row == 10:
                        print(row[col], end="")
                        
                    else:
                        print(" ", end="")
                print(" |  |")
        print("-"*40)
                    
                    
                                                            

            
    
    def translate_move_for_matrix(self, move):
        """
        Translates a move (A1 or G4...) to a list of row index and column index [9, 2] or [6, 8]
        :return: a list of row and col of the matrix, named "position"
        """
        
        translated_row  = 10 - int(move[1])             #move[1] is a number 1-8
        translated_col  = self.board[10].index(move[0]) #move[0] is a letter A-H
        return [translated_row, translated_col]
        
        

    def calculate_allowed_moves(self):
        """
        Calculates allowed moves and updates list
        """
        
        pass

    def make_move(self, new_position):
        """
        Moves the knight to a new position
        """
        self.current_position = self.translate_move_for_matrix(new_position)
        self.previous_dict_key += 1
        self.previous_positions[self.previous_dict_key] = self.current_position