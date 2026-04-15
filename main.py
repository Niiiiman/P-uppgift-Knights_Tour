from Round_File import Round

import random

main_running = True
rounds_dict = {}

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

def main_menu(): 
    """ 
    Used to display the menu: 
    What would you like to do? 
    1 - Play the game 
    2 - Watch computer play 
    3 - See statistics from 1000 moves 
    4 - Exit 
    :return: (nothing) 
    """
    print("-"*40)
    print("What would you like to do? (type a number 1-4)")
    print("1 - Play the game")
    print("2 - Watch computer play ")
    print("3 - See statistics from 1000 moves ")
    print("4 - Exit")
    print("-"*40)
    
def execute_main_menu(choice): 
    """ 
    Used to execute the option that the user chose from the main menu
    :param choice: an int corresponding the the chosen option 
    :return: (nothing) 
    """ 
    match choice:

        case 1:
            #Get starting pos
            #start player round
            empty_board = Round("A1", True)
            empty_board.print_board()

            print("Start by choosing your starting square!")
            starting_position = get_position_input()
            start_round(starting_position, False)

        case 2:
            letters = ['A','B','C','D','E','F','G','H']
            starting_position = letters[random.randint(0,7)] + str(random.randint(1,8))
            start_round(starting_position, True)
    #        #start rounds with random starting pos

    #   case 3:    
             #Let computer play 1000 moves
    #        #update statistics
    #        #print statistics
        case 4:
           quit_program()
    #      #main_running = False
            
    #        
        case default:
            print("Please enter an integer from the list (1-4)")
            
def quit_program(): 
    print("Thanks for playing! \nExiting...")
    global main_running
    main_running = False  

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
        
def get_position_input(): 
    """
    Gets position as an input from user, with error handling
    :return: string of postion ("E4", )
    
    """
    while True:
        try:
            print("Enter 'quit' or 'exit' to go back to main menu, or: ")
            print("Enter the coordinates of your next move: (Format E4, A1, H8...)")
            print("Allowed moves are marked with a - h ")
       
            position = input("Enter next move: ")
            if position == "quit" or position == "exit":
                return "quit"
            if len(position) != 2:
                raise ValueError
            position = position[0].upper() + position[1]
            if position[0] in ['A','B','C','D','E','F','G','H'] and int(position[1]) >= 1 and  int(position[1]) <= 8:

                return position
            else:
                raise ValueError 
            
        except ValueError:
            print("Use the correct format for a position - A1, E4, H8 or similar")


def get_position_random(): 
    """
    Used to allow the user to press enter to see the next random move, does not matter what they type.
    """
    print("Enter 'quit' or 'exit' to go back to main menu, or: ")
    input_random = input("Press enter to see next move: ")

    return input_random


def start_round(starting_position, auto):
    """)
    Creates object of the Round class and adds it to the dictionary. This function is the main-game-function
    """
    rounds_dict[starting_position] = Round(starting_position)
    current_round = rounds_dict[starting_position]
    playing = True
    while playing:
        current_round.print_board()
    

        if auto == True:
            next_move = get_position_random()    
        else:
            next_move = get_position_input()
            
        if next_move == "quit":
            print("Quiting to main mainu...")
            playing = False
        else:
           playing = current_round.make_move(next_move, auto) #make the move
    
    print("GAME OVER!")
    print("Final score: ", len(current_round.previous_positions))


#def start_computer_round(start):


def main():
    print("-"*200)
    print("Welcome! This is a game based on chess,")
    print("you play as a knight (which means you can")
    print("move in an L-shape), and you cannot step on")
    print("the same square twice, you lose when you cannot move.")
    print("Good luck!")
    while main_running:
        main_menu()
        execute_main_menu(get_int_input("Enter choice: "))
    

if __name__ == '__main__':
    main()