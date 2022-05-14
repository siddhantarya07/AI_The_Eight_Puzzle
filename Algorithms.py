from distutils.command.install_egg_info import to_filename
from Node import *
from numpy import *
import numpy as np

#Uniform cost search algorithm
def uniform_cost_search(initial_state, goal_state, customized_puzzle_size):
    initial_node= create_node(initial_state, None, None,0,0)
    trace_list = []
    frontier_queue =[]
    expanded_nodes_count = 0
    working_node = initial_node
    final_depth= 0
    orignal_queue = [] # To prevent expansion of repeated nodes 
    while(working_node.state != goal_state):
        tempMoves = explored_moves(working_node,customized_puzzle_size)
        for moves in tempMoves:
            if moves.state not in orignal_queue:
                moves.depth = working_node.depth + 1
                orignal_queue.append(moves.state)
                frontier_queue.append(moves)
                expanded_nodes_count = expanded_nodes_count +1
                final_depth = moves.depth
        frontier_queue.sort(key =lambda x: x.depth)
        working_node = frontier_queue.pop(0)
    while(working_node.parent != None):
        trace_list.append([working_node.operation,working_node.state])
        working_node = working_node.parent
    
    trace_list.reverse()
    return Result_Set(trace_list, expanded_nodes_count,final_depth)


#Calculates the misplaced heuristic value for A* algorithm
#Counts measures the amount of misplaced tile by comparing initial state to goal state
def find_misplaced_tile_heuristic(current_state, goal_state):
    count = 0 #amount of misplaced tile number
    for i in range(0,9):
        if current_state.state[i] != 0 and current_state.state[i] != goal_state[i]:
            count = count +1
    current_state.heuristic = count


# A Star algorithm with Misplaced tile heuristic
def a_star_misplaced_tile_heuristic(initial_state,goal_state,customized_puzzle_size):
    initial_node= create_node(initial_state, None, None,0,0)
    trace_list = []
    frontier_queue =[]
    expanded_nodes_count = 0
    working_node = initial_node
    final_depth= 0
    orignal_queue = [] # To prevent expansion of repeated nodes 
    while(working_node.state != goal_state):
        tempMoves= explored_moves(working_node,customized_puzzle_size)
        for moves in tempMoves:
            find_misplaced_tile_heuristic(moves, goal_state)
            if moves.state not in orignal_queue:
                moves.depth = working_node.depth + 1
                orignal_queue.append(moves.state)
                frontier_queue.append(moves)
                expanded_nodes_count = expanded_nodes_count +1
                final_depth= moves.depth
        frontier_queue.sort(key =lambda x: x.heuristic + x.depth)
        working_node = frontier_queue.pop(0)
    while(working_node.parent != None):
        trace_list.append([working_node.operation,working_node.state])
        working_node = working_node.parent
    # traverse the list
    trace_list.reverse()
    return Result_Set(trace_list, expanded_nodes_count,final_depth)


#Calculates the manhattan heuristic value for A* algorithm
def calculate_manhattan_distance_heuristic(node, goal_state,customized_puzzle_size):
    current_state = node.state
    total_manhattan = 0
    # for manhattan distance, convert a 1d array to N-D array
    initial_array =np.array(current_state)
    goal_array = np.array(goal_state)
    n_d_current_array = initial_array.reshape(customized_puzzle_size,customized_puzzle_size)
    n_d_goal_state = goal_array.reshape(customized_puzzle_size,customized_puzzle_size)
    for i in range(0,customized_puzzle_size):
        for j in range(0,customized_puzzle_size):
            if (n_d_current_array[i][j] != n_d_goal_state[i][j]) and n_d_current_array[i][j] != 0:
                current_item_index_in_goal= np.where(n_d_goal_state == n_d_current_array[i][j])
                current_tile_index_in_goal = list(zip(current_item_index_in_goal[0], current_item_index_in_goal[1]))
                current_item_index_in_initial= np.where(n_d_current_array == n_d_current_array[i][j])
                current_tile_index_in_initial = list(zip(current_item_index_in_initial[0], current_item_index_in_initial[1]))
                current_move_required= abs(current_tile_index_in_goal[0][0] -current_tile_index_in_initial[0][0]) + abs(current_tile_index_in_goal[0][1] -current_tile_index_in_initial[0][1])
                total_manhattan = total_manhattan + current_move_required
    node.heuristic= total_manhattan

# A Star algorithm with Manhattan distance heuristic
def a_star_manhattan_distance_heuristic(initial_state,goal_state,customized_puzzle_size):
    initial_node= create_node(initial_state, None, None,0,0)
    trace_list = []
    frontier_queue =[]
    orignal_queue = [] # To prevent expansion of repeated nodes 
    expanded_nodes_count = 0
    final_depth =0
    working_node = initial_node
    while(working_node.state != goal_state):
        tempMoves= explored_moves(working_node,customized_puzzle_size)
        for moves in tempMoves:
             calculate_manhattan_distance_heuristic(moves, goal_state,customized_puzzle_size)
             if moves.state not in orignal_queue:
                moves.depth = working_node.depth + 1
                orignal_queue.append(moves.state)
                frontier_queue.append(moves)
                expanded_nodes_count = expanded_nodes_count +1
                final_depth = moves.depth
        frontier_queue.sort(key =lambda x: x.heuristic  + x.depth)
        working_node = frontier_queue.pop(0)
    while(working_node.parent != None):
        trace_list.append([working_node.operation,working_node.state])
        working_node = working_node.parent
    # traverse the list
    trace_list.reverse()
    return Result_Set(trace_list, expanded_nodes_count,final_depth)
