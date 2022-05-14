from Algorithms import *
from DisplayOutput import *
import time


#User choices for puzzle type
def input_user_choice():
    size_of_matrix= 0
    print("Press 1 for default 8*8 puzzle")
    print("Press 2 for customized N*N puzzle")
    puzzle_type = input()
    if(puzzle_type == '1'):
        print("\nYou have selected to solve default 8*8 puzzle\n")
        print("Please enter space to seperate the numbers.")
        print("Please enter 0 for the blank tile.")
        size_of_matrix = 3
    elif(puzzle_type == '2'):
        print("\nYou have selected to solve N*N puzzle\n")
        print("Please enter space to seperate the numbers.")
        print("Please enter 0 for the blank tile.")
        print("Enter the size of the matrix puzzle:")
        size_of_matrix = int(input())
    else:
        print("Invalid output\n")
    #User Input for puzzle data
    array_data =[]
    user_input_count =1
    while( user_input_count <= size_of_matrix):
        print(f"Enter data for Row {user_input_count}:")
        matrix_row_input_data= input()
        matrix_row_input_data_array = matrix_row_input_data.split(" ")
        matrix_aray_user_data = [int(numeric_string) for numeric_string in matrix_row_input_data_array]
        array_data.append(matrix_aray_user_data)
        user_input_count = user_input_count +1
    return array_data,size_of_matrix

# Select Puzzle type
def puzzle_type_selection():
    print("Please select type of algorithm to solve the puzzle:")
    print("Type 1 for Uniform Cost Search")
    print("Type 2 for A* with Misplaced Tile Heuristic")
    print("Type 3 for A* with Manhattan Distance Heuristic")
    algorithm_type_input= input()
    algorithm_type = int(algorithm_type_input)
    return algorithm_type


# Main Method
# Starting point of the application
def main():
    result = input_user_choice()
    input_puzzle_data = result[0]
    customized_puzzle_size = result[1]
    algorithm_selection = puzzle_type_selection()
    #Defines goal state
    goal_state = []
    state = 1
    while( state < customized_puzzle_size*customized_puzzle_size):
        goal_state.append(state)
        state = state+1
    goal_state.append(0)
    # Flattens puzzle data    
    puzzle_array_data = np.array(input_puzzle_data)
    initial_state_array = puzzle_array_data.flatten()
    initial_state = initial_state_array.tolist()
    result_set = None
    if algorithm_selection == 1:
        start = time.time()
        result_set = uniform_cost_search(initial_state, goal_state,customized_puzzle_size)
        end = time.time()
        time_taken= end- start
    elif algorithm_selection == 2:
        start = time.time()
        result_set = a_star_misplaced_tile_heuristic(initial_state, goal_state, customized_puzzle_size)
        end = time.time()
        time_taken= end- start
    elif algorithm_selection == 3:
        start = time.time()
        result_set = a_star_manhattan_distance_heuristic(initial_state, goal_state, customized_puzzle_size)
        end = time.time()
        time_taken= end- start
    else:
        print("Invalid Selection")

    display_board_according_to_size(customized_puzzle_size,result_set, initial_state,time_taken)
   


if __name__ == "__main__":
    main()

