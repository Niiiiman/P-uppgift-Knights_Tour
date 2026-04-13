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
            starting_position = get_position_input()
            start_round(starting_position, False)
        case 2:
            letters = ['A','B','C','D','E','F','G','H']
            starting_position = letters[random.randint(0,7)] + str(random.randint(1,8))
            start_round(starting_position, True)
    #        #start rounds with random starting pos, make random moves 1000 times

    #    case 3:    
    #        #update statistics
    #        #print statistics
        case 4:
           quit_program()
    #        #main_running = False
            
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
            position = input("Enter next move: ")
            if position == "quit" or position == "exit":
                return "quit"
            position = position[0].upper() + position[1]
            if position[0] in ['A','B','C','D','E','F','G','H'] and int(position[1]) >= 1 and  int(position[1]) <= 8:

                return position
            else:
                raise ValueError 
            
        except ValueError:
            print("Use the correct format for a position - A1, E4, H8 or similar")
    
def get_position_random(round):
    print("Enter 'quit' or 'exit' to go back to main menu, or: ")
    position = input("Press enter to see next move: ")

    if position == "quit" or position == "exit":
        return "quit"
    
   # allowed_moves_translated = []
   # for move in round.allowed_positions:
   #     if move not in round.previous_positions.values():
   #         allowed_moves_translated.append()

    letters = ['A','B','C','D','E','F','G','H']
    position = letters[random.randint(0,7)] + str(random.randint(1,8))
    return position

def start_round(start, auto):
    """)
    Creates object of the Round class and adds it to the dictionary. This function is the main-game-function
    """
    rounds_dict[start] = Round(start)
    current_round = rounds_dict[start]
    playing = True
    while playing:
        current_round.print_board()
        if len(current_round.allowed_positions) > 0:
            if auto == True:
                next_move = get_position_random(current_round)
            else:
                next_move = get_position_input()
            if next_move == "quit":
                print("Quiting to main mainu...")
                playing = False
            else:
                current_round.make_move(next_move) #make the move
        else:
            print("GAME OVER!")
            print("Final score: " + len(current_round.previous_positions))
            playing = False


#def start_computer_round(start):


def main():

    while main_running:
        main_menu()
        execute_main_menu(get_int_input("Enter choice: "))
    
    """
    
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
    """


if __name__ == '__main__':
    main()