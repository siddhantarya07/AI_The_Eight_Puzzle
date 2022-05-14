from inspect import trace
from Moves import *
# Class to initialize a method
class Node:
    def __init__(self,initial_state,parent,operation,depth,cost):
        self.state = initial_state
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost
        self.heuristic = None
    
#Create Node
def create_node(initial_state, parent_node, operation, depth, cost):
    return Node(initial_state, parent_node, operation,depth,cost)

#Applies all the operations and explore all the possible moves    
def explored_moves(working_node, customized_puzzle_size):
    explored_set =[]
    upward_move = create_node(move_up(working_node.state, customized_puzzle_size),working_node,"Move Up",working_node.depth+1,0)
    explored_set.append(upward_move)

    downward_move = create_node(move_down(working_node.state,customized_puzzle_size),working_node,"Move Down",working_node.depth+1,0)
    explored_set.append(downward_move)

    left_move = create_node(move_left(working_node.state, customized_puzzle_size),working_node,"Move Left",working_node.depth+1,0)
    explored_set.append(left_move)

    right_move = create_node(move_right(working_node.state, customized_puzzle_size),working_node,"Move Right",working_node.depth+1,0)
    explored_set.append(right_move)

    # Returns only the valid nodes
    explored_set = [working_node for working_node in explored_set if working_node.state != None]
    return explored_set

class Result_Set:
    def __init__(self,trace_list, explored_nodes_count,final_depth):
        self.trace_list =trace_list
        self.explored_nodes_count =explored_nodes_count
        self.final_depth =final_depth
