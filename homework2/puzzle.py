
from __future__ import division
from __future__ import print_function

import sys
import math
import time
import queue as Q
import resource

#### SKELETON CODE ####
## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[self.n*i : self.n*(i+1)])

    def move_up(self):
        """ 
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index < self.n :
            return None

        else :
            next_state = self.config.copy()
            next_state[self.blank_index], next_state[self.blank_index - self.n] = next_state[self.blank_index - self.n], next_state[self.blank_index]
            return PuzzleState(next_state, self.n, self, "Up", self.cost + 1)
      
    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index >= self.n*self.n - self.n :
            return None

        else :
            next_state = self.config.copy()
            next_state[self.blank_index], next_state[self.blank_index + self.n] = next_state[self.blank_index + self.n], next_state[self.blank_index]
            return PuzzleState(next_state, self.n, self, "Down", self.cost + 1)
      
    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index % self.n == 0 :
            return None

        else :
            next_state = self.config.copy()
            next_state[self.blank_index], next_state[self.blank_index - 1] = next_state[self.blank_index - 1], next_state[self.blank_index]
            return PuzzleState(next_state, self.n, self, "Left", self.cost + 1)

    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index % self.n == self.n - 1 :
            return None

        else :
            next_state = self.config.copy()
            next_state[self.blank_index], next_state[self.blank_index + 1] = next_state[self.blank_index + 1], next_state[self.blank_index]
            return PuzzleState(next_state, self.n, self, "Right", self.cost + 1)
      
    def expand(self):
        """ Generate the child nodes of this node """
        
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children
        
        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]    
        return self.children

    
    def __lt__(self, other):
        this_cost = calculate_total_cost(self)
        other_cost = calculate_total_cost(other)

        if this_cost == other_cost :
            return direction_priority.index(self.action) < direction_priority.index(other.action)

        return this_cost < other_cost

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput(final_state, path, expanded, depth, maximum, time, space):
    ### Student Code Goes here
    output = open("output.txt", "a")
    output.write("path_to_goal: " + str(path))
    output.write("\ncost_of_path: %d" %final_state.cost)
    output.write("\nnodes_expanded: %d" %expanded)
    output.write("\nsearch_depth: %d" %depth)
    output.write("\nmax_search_depth: %d" %maximum)
    output.write("\nrunning_time: %.3f s" %time)
    output.write("\nmax_ram_usage: %.3f MB" %space)
    output.write("\n\n")

    #print("path_to_goal: " + str(path))
    #print("cost_of_path: %d" %final_state.cost)
    #print("nodes_expanded: %d" %expanded)
    #print("search_depth: %d" %depth)
    #print("max_search_depth: %d" %maximum)
    #print("running_time: %.3f s" %time)
    #print("max_ram_usage: %.3f MB" %space)

def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    q = Q.Queue()
    q.put(initial_state)
    visited = {(*initial_state.config,)} # converts the list into a tuple so that it can be hashed
    nodes_expanded = 0
    search_depth = 0
    max_search_depth = 0

    while not q.empty() :
        state = q.get();
        #print(str(state.cost) + " " + state.action)
        #state.display()
        #print()

        if test_goal(state) :
            search_depth = state.cost
            return [state, nodes_expanded, search_depth, max_search_depth]

        state.expand()
        nodes_expanded += 1

        if state.cost >= max_search_depth :
            max_search_depth = state.cost + 1

        for i in state.children :
            config_tuple = (*i.config,)
            if config_tuple not in visited :
                q.put(i)
                visited.add(config_tuple)

    return False

def dfs_search(initial_state):
    """DFS search"""
    ### STUDENT CODE GOES HERE ###
    q = Q.LifoQueue()
    q.put(initial_state)
    visited = {(*initial_state.config,)}
    nodes_expanded = 0
    search_depth = 0
    max_search_depth = 0

    while not q.empty() :
        state = q.get();
        #print(str(state.cost) + " " + state.action)
        #state.display()
        #print()

        if state.cost >= max_search_depth :
            max_search_depth = state.cost

        if test_goal(state) :
            search_depth = state.cost
            return [state, nodes_expanded, search_depth, max_search_depth]

        state.expand()
        nodes_expanded += 1

        state.children.reverse()
        for i in state.children :
            config_tuple = (*i.config,)
            if config_tuple not in visited :
                q.put(i)
                visited.add(config_tuple)

    return False

def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###
    q = Q.PriorityQueue()
    q.put(initial_state)
    visited = {(*initial_state.config,)}
    nodes_expanded = 0
    search_depth = 0
    max_search_depth = 0

    while not q.empty() :
        state = q.get()
        #print(str(state.cost) + " " + state.action)
        #state.display()
        #print("man: %d"%(calculate_total_cost(state) - state.cost))
        #print()

        if test_goal(state) :
            search_depth = state.cost
            return [state, nodes_expanded, search_depth, max_search_depth]

        state.expand()
        nodes_expanded += 1

        if state.cost >= max_search_depth :
            max_search_depth = state.cost + 1

        for i in state.children :
            config_tuple = (*i.config,)
            if config_tuple not in visited :
                q.put(i)
                visited.add(config_tuple)

    return False

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###
    total_cost = state.cost
    idx = 0

    for value in state.config :
        if value == 0 :
            idx += 1

        else : 
            total_cost += calculate_manhattan_dist(idx, value, state.n)
            idx += 1

    return total_cost

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###
    return abs(idx//n - value//n) + abs(idx%n - value%n)


def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### STUDENT CODE GOES HERE ###
    return puzzle_state.config == config_goal


def path(puzzle_state) :
    path = []
    while puzzle_state.cost != 0 :
        path.append(puzzle_state.action)
        puzzle_state = puzzle_state.parent

    path.reverse()
    return path

# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    
    #Global Variable for functions that are called many times.
    global config_goal
    config_goal = list(range(0,board_size*board_size))
    global direction_priority
    direction_priority = ("Up", "Down", "Left", "Right")

    final_state = None
    if   search_mode == "bfs": final_state = bfs_search(hard_state)
    elif search_mode == "dfs": final_state = dfs_search(hard_state)
    elif search_mode == "ast": final_state = A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")
        
    path_to_goal = path(final_state[0])
    space = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000000
    end_time = time.time()
    writeOutput(final_state[0], path_to_goal, final_state[1], final_state[2], final_state[3], end_time-start_time, space)
    print("Program completed in %.3f second(s)"%(end_time-start_time))

if __name__ == '__main__':
    main()

