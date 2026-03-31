class Round:
    """
    Attributes:

    allowed_positions:   list of coordinates where the knight can move
    previous_positions:  list of visited coordinates
    board_matrix:        12x12 grid representing the board
    current_position:    current coordinate of the knight
    """

    def __init__(self, current_position):
        """
        Creates a new Round with current_position as starting position
        """
        self.current_position = current_position
        self.allowed_positions = []
        self.previous_positions = [current_position]
        self.board = [
                            [-1,  -1, -1, -1, -1, -1, -1, -1  -1, -1,   -1,-1],
                            [-1,  -1, -1, -1, -1, -1, -1, -1  -1, -1,   -1,-1],
    
                            [-1,   8,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],
                            [-1,   7,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],
                            [-1,   6,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],
                            [-1,   5,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],
                            [-1,   4,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],
                            [-1,   3,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],
                            [-1,   2,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],
                            [-1,   1,  0,  0,  0,  0,  0,  0,  0,  0,   -1,-1],
                                
                            [-1,  -1, 'A','B','C','D','E','F','G','H'   -1,-1],

                            [-1,  -1, -1, -1, -1, -1, -1, -1, -1, -1,   -1,-1],
                            ]
        #self.board[row][col] will get the element on that row and col of the matrix,
        #  not the playable board



    def __str__(self):
        """
        Returns a string representation of the board
        """

        return ""

    def get_move(self):
        """
        Ask user for move and return chosen coordinate
        """
        move = input("Choose your move: ")
        return move

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


