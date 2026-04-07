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
    
    
def execute(choice): 
    """ 
    Used to execute the option that the user chose 
    :param choice: an int corresponding the the chosen option 
    :return: (nothing) 
    """ 
    #match choice:
    #    case 1:
    #        #Get starting pos
    #        #start player round
    #    case 2:
    #        #start rounds with random starting pos, make random moves 1000 times
    #    case 3:    
    #        #update statistics
    #        #print statistics
    #    case 4:
    #        #Running = False
    #        
    #    case default:
    #        #error
            
     
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
    while True:
        try:
            starting_position = input("Enter your starting position - A1 to H8")
            if starting_position[0] in ['A','B','C','D','E','F','G','H'] and int(starting_position[1]) >= 1 and  int(starting_position[1]) <= 8:

                return starting_position
            else:
                raise ValueError 
            
        except ValueError:
            print("Use the correct format for a position - A1, E4, H8 or similar")
    

def start_player_round(starting_position):
    """
    Creates object of the Round class. 
    """
    


def start_auto_round(starting_position):
    """
    
    """
    
    
     
 


rounds_dict = {}

#starting_position= "E4"
#rounds_dict[starting_position= Round(starting_position)
starting_position= "D2"
rounds_dict[starting_position] = Round(starting_position)


rounds_dict["D2"].print_board()

rounds_dict["D2"].make_move("F1")
rounds_dict["D2"].print_board()

rounds_dict["D2"].make_move("G3")
rounds_dict["D2"].print_board()

rounds_dict["D2"].make_move("E4")
rounds_dict["D2"].print_board()

#rounds_dict["D2"].make_move("")
#rounds_dict["D2"].print_board()