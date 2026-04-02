from Round_File import Round

def menu(): 
    """ 
    Used to display the menu: 
    What would you like to do? 
    1 - Play the game 
    2 - Watch computer play 
    3 - See statistics from 1000 moves 
    4 - Exit 
    :return: (nothing) 
    """
    print("What would you like to do? (type a number 1-4)")
    print("1 - Play the game")
    print("2 - Watch computer play ")
    print("3 - See statistics from 1000 moves ")
    print("4 - Exit")
    
     
def update_statistics():  
    """
    Uses the dictionary of all rounds to make a list of the rounds the computer plays in the “make 
    1000 random moves” choice. 
    :return: nothing 
    """
    
 
 
def print_statistics(): 
    """ 
    Prints the 1000 games played, with the most amount of moves at top. 
    :return: nothing 
    """
    

def get_int_input(prompt_string): 
    """ 
    Used to get an int from the user, asks again if input is not convertible to int 
    :param prompt_string: the string explaining what to input 
    :return: the int that was asked for 
    """ 
    while True:
        try:
            num = int(input(prompt_string))
            return num
            
        except ValueError:
            print("Enter an integer")    
        
    
def get_starting_position():
    """
    Gets starting position as an input from user, with error handling
    :return: string of starting postion ("E4", )
    """
def start_player_round():
    """
    Creates object of the Round class. 
    """

    
    
     
 
def execute(choice): 
    """ 
    Used to execute the option that the user chose 
    :param choice: an int corresponding the the chosen option 
    :return: (nothing) 
    """ 


rounds_dict = {}

starting_pos = "E4"
rounds_dict[starting_pos]= Round(starting_pos)
starting_pos = "D2"
rounds_dict[starting_pos]= Round(starting_pos)


rounds_dict["D2"].print_board()

rounds_dict["D2"].make_move("F1")
rounds_dict["D2"].print_board()

rounds_dict["D2"].make_move("G3")
rounds_dict["D2"].print_board()