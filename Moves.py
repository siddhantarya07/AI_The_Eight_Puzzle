# Swap the tile up and return as new node
# If possible move is not available, return None
def move_up(state,customized_puzzle_size):
    next_state = state[:]
    next_state_index = next_state.index(0)
    state_not_to_consider = []
    start =0
    while(start < customized_puzzle_size):
        state_not_to_consider.append(start)
        start = start +1
    if next_state_index not in state_not_to_consider:
        temp = next_state[next_state_index - 3]
        next_state[next_state_index - 3] = next_state[next_state_index]
        next_state[next_state_index] = temp
        return next_state
    else:
        return None

# Swap the tile down and return as new node
# If possible move is not available
def move_down(state, customized_puzzle_size):
    next_state = state[:]
    next_state_index = next_state.index(0)
    state_not_to_consider = []
    start = len(state) -customized_puzzle_size
    for i in range(0,customized_puzzle_size):
        state_not_to_consider.append(start)
        start = start +1
    # if next_state_index not in [6, 7, 8]:
    if next_state_index not in state_not_to_consider:
        temp = next_state[next_state_index + 3]
        next_state[next_state_index + 3] = next_state[next_state_index]
        next_state[next_state_index] = temp
        return next_state
    else:
        return None

        
# Moves the tile left and return as new node
# If possible move is not available, return None
def move_left(state, customized_puzzle_size):
    next_state = state[:]
    next_state_index = next_state.index(0)
    state_not_to_consider = []
    start = 0
    while(start < len(state)):
        state_not_to_consider.append(start)
        start = start + customized_puzzle_size
    # if next_state_index not in [0, 3, 6]:
    if next_state_index not in state_not_to_consider:
        temp = next_state[next_state_index - 1]
        next_state[next_state_index - 1] = next_state[next_state_index]
        next_state[next_state_index] = temp
        return next_state
    else:
        return None

# Swap the tile right and return as new node
# If possible move is not available, return None
def move_right(state, customized_puzzle_size):
    next_state = state[:]
    next_state_index = next_state.index(0)
    state_not_to_consider = []
    start = customized_puzzle_size -1
    while(start < len(state)):
        state_not_to_consider.append(start)
        start = start + customized_puzzle_size
    # if next_state_index not in [2, 5, 8]:
    if next_state_index not in state_not_to_consider:
        temp = next_state[next_state_index + 1]
        next_state[next_state_index + 1] = next_state[next_state_index]
        next_state[next_state_index] = temp
        return next_state
    else:
        return None



