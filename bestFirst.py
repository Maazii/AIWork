class State:
    def __init__(self, queenLocations=[]):
        self.queenLocations = queenLocations

    # A note on the queenLocations array.
    # The queenLocations array can be explained well by unpacking an example of it.
    # Let queenLocations = [3, 0, 1, 1] and this can hold at minimum nothing, and at maximum 4 elements.
    # Now the above example translates to the following:
    # Index 0 (first row) has a queen at the third index (fourth column).
    # Index 1 (second row) has a queen at the zero index (first column).
    # Index 2 (third row) has a queen at the first index (second column).
    # Index 3 (fourth row) has a queen at the first index (second column).
    # Since each index of the queenLocations array acts as a row, this automatically means that once this array is implemented on a board,
    # every row will at most have one queen.
    
    def heuristicCalculation(self):
        captures = 0
        for i in range(len(self.queenLocations)):
            for j in range(i + 1, len(self.queenLocations)):


                if self.queenLocations[i] == self.queenLocations[j]: # This portion raises a capture warning as soon as there are two queens
                    captures += 1                                    # in the same column.


                elif abs(self.queenLocations[i] - self.queenLocations[j]) == abs(i - j): # This portion checks for
                    captures += 1                                                        # any capture violations diagonally.
        return captures
    
    def __lt__(self, other):
        return self.heuristicCalculation() < other.heuristicCalculation() # This is a function defined for the less than property of
                                                                          # a state instance. A comparison is carried out
                                                                          # in terms of what their heuristics result in using the
                                                                          # heuristicCalculation function.

def GBFS():
    initialState = State()
    # print_board(initialState)
    open_list = [initialState]
    # print_board(open_list)
    visitedStates = set()
    stateCounter = 0

    while open_list:
        current_state = open_list.pop(0)
        print_board(current_state.queenLocations)
        print()
        print("   |")
        print("   |")
        print("  \|/")
        print()
        stateCounter = stateCounter + 1
        visitedStates.add(tuple(current_state.queenLocations))  # Store the state as a tuple for efficient lookup
        if len(current_state.queenLocations) == 4:
            return current_state.queenLocations, stateCounter

        for i in range(4):
            if i not in current_state.queenLocations:
                new_queenLocations = current_state.queenLocations + [i]
                if tuple(new_queenLocations) not in visitedStates:  # Check if the state has been visited before
                    open_list.append(State(new_queenLocations))
                    visitedStates.add(tuple(new_queenLocations))

        open_list.sort()

def print_board(queenLocations):
    board = [['_' for _ in range(4)] for _ in range(4)]
    for i in range(len(queenLocations)):
        board[i][queenLocations[i]] = 'Q'
    for row in board:
        print(' '.join(row))

queenLocations, counter = GBFS()
print("Final board:")
print_board(queenLocations)
print()
print(f"Total number of states traversed: {counter}")
