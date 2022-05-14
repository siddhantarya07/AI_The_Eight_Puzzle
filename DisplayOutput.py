
#Displays Initial state 8*8 puzzle
from Node import Result_Set


def initial_board(state):
    print("Initial State of the puzzle is:")
    print( "-------------")
    print( "| %i | %i | %i |" % (state[0], state[1], state[2]))
    print( "-------------")
    print( "| %i | %i | %i |" % (state[3], state[4], state[5]))
    print( "-------------")
    print( "| %i | %i | %i |" % (state[6], state[7], state[8]))
    print( "-------------")

# Displays initial state for four * four puzzle
def initial_board_for_four(state):
    print("Initial State of the puzzle is:")
    print( "-------------------")
    print( "| %i | %i | %i | %i |" % (state[0], state[1], state[2], state[3]))
    print( "-------------------")
    print( "| %i | %i | %i | %i |" % (state[4], state[5], state[6], state[7]))
    print( "-------------------")
    print( "| %i | %i | %i | %i |" % (state[8], state[9], state[10], state[11]))
    print( "-------------------")
    print( "| %i | %i | %i | %i |" % (state[12], state[13], state[14], state[15]))
    print( "-------------------")

#Displays each transition state of 8*8 puzzle
def display_board(path,count):
    state = path[1]
    print(f"Step {count}: {path[0]}")
    print( "-------------")
    print( "| %i | %i | %i |" % (state[0], state[1], state[2]))
    print( "-------------")
    print( "| %i | %i | %i |" % (state[3], state[4], state[5]))
    print( "-------------")
    print( "| %i | %i | %i |" % (state[6], state[7], state[8]))
    print( "-------------")

# Displays final board for four*four puzzle
def display_board_for_four(path,count):
    state = path[1]
    print(f"Step {count}: {path[0]}")
    print( "-------------------")
    print( "| %i | %i | %i | %i |" % (state[0], state[1], state[2], state[3]))
    print( "-------------------")
    print( "| %i | %i | %i | %i |" % (state[4], state[5], state[6], state[7]))
    print( "-------------------")
    print( "| %i | %i | %i | %i |" % (state[8], state[9], state[10], state[11]))
    print( "-------------------")
    print( "| %i | %i | %i | %i |" % (state[12], state[13], state[14], state[15]))
    print( "-------------------")

#Displays initial state for any n*n size puzzle
def display_board_for_any_n_matrix_initial(state):
    print("-----------------------")
    print("Initial State for the given matrix is: ")
    print(state)
    print("-----------------------")

#Displays final state for any n*n size puzzle
def display_board_for_any_n_matrix(path, count):
    state = path[1]
    print(f"Step {count}: {path[0]}")
    print(state)
    print("-----------------------")

#Displays analysis for puzzle size
def display_analysis(steps, explored_nodes,time_taken,final_depth):
    final_depth = final_depth
    print("---------Analysis----------")
    print(f"The puzzle has been solved.")
    print(f"The total number of nodes explored: {explored_nodes}")
    print(f"Solution Depth is at: {final_depth}")
    print(f"The time taken by the algorithm is: {time_taken}")

def display_analysis_for_uniform_cost_search(steps, explored_nodes,time_taken,final_depth):
    final_depth = final_depth-1
    print("---------Analysis----------")
    print(f"The puzzle has been solved with the {steps} tile movements")
    print(f"The total number of nodes explored: {explored_nodes}")
    print(f"Solution Depth is at: {final_depth}")
    print(f"The time by the algorithm is: {time_taken}")

#Displays puzzle board according to the size of the puzzle
def display_board_according_to_size(customized_puzzle_size, result_set,initial_state, time_taken):
    count =0    
    if(customized_puzzle_size ==3):
        initial_board(initial_state)
        for path in result_set.trace_list:
            count= count+1
            display_board(path,count)
    elif(customized_puzzle_size ==4):
        initial_board_for_four(initial_state)
        for path in result_set.trace_list:
            count= count+1
            display_board_for_four(path,count)
    else:
        display_board_for_any_n_matrix_initial(initial_state)
        for path in result_set.trace_list:
            count= count+1
            display_board_for_any_n_matrix(path,count)

    display_analysis(count,result_set.explored_nodes_count,time_taken,result_set.final_depth)