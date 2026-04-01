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
        self.current_position = start_position
        self.allowed_positions = []
        self.previous_positions = [start_position]
        
        self.current_row = 0
        self.current_col = 0
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
                                
                            [-1,  -1, 'A','B','C','D','E','F','G','H'   -1,-1],#10

                            [-1,  -1, -1, -1, -1, -1, -1, -1, -1, -1,   -1,-1],#11
                            # 0    1   2   3   4   5   6   7   8   9    10 11
                            ]
        
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
#

    def print_board(self):
        """
        Prints the board row by row
        """
        previous_index = 0
        allowed_index = 2
        print("-"*40)
        print("|   "  + ("-"*32) + "   |")
        for id_row, row in enumerate(self.board): #Cycles through each row
            if row[1] != -1:
                print("|" + str(row[1]), end=" ")
                
                for col in range(2,10): #Cycles through each square in one row
                    print(" | ")

                    if [id_row, col] == self.current_position:
                        print("X") #Print the knight                        

                    elif [id_row, col] in self.previous_positions:
                        print(self.previous_positions[previous_index])
                        previous_index += 1

                    elif [id_row, col] in self.allowed_positions:
                        print(str((self.board[10][allowed_index]())).lower())
                        allowed_index += 1  
                        
                    else:
                        print(" ")
                    
                    
                                                            

                            
    def get_move(self):
        """
        Ask user for move and return chosen coordinate
        """
        move = input("Choose your move: ")
        return move
    
    def update_curent_position(self, move):
        """
        Translates a move (A1 or G4...) to row index and column index and 
        """
        
        self.current_row  = 10 - int(move[1]) #move[1] is a number 1-8
        self.current_col  = self.board[10].index(move[0]) #move[0] is a letter A-H
        self.current_position = [self.current_row, self.current_col]
        
        

    def calculate_allowed_moves(self):
        """
        Calculates allowed moves and updates list
        """
        
        pass

    def make_move(self, new_position):
        """
        Moves the knight to a new position
        """
        self.current_position = new_position
        self.previous_positions.append(new_position)


