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

                                                                            
                if self.queenLocations[i] == self.queenLocations[j]:    # This portion raises a capture warning as soon as there are two queens
                                                                        # in the same column.
                    captures += 1

                elif abs(self.queenLocations[i] - self.queenLocations[j]) == abs(i - j):    # This portion checks for
                                                                                            # any capture violations diagonally.
                    captures += 1
        return captures

    def __lt__(self, other):
        return self.heuristicCalculation() < other.heuristicCalculation()   # This is a function overrde defined for the less than property of
                                                                            # a state instance. A comparison is carried out
                                                                            # in terms of what their heuristics result in using the
                                                                            # heuristicCalculation function.

def showBoard(queenLocations):
    board = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append('_')
        board.append(row)

    for i in range(len(queenLocations)):
        board[i][queenLocations[i]] = 'Q'
    for row in board:
        print(row)


def GBFS():
    initialState = State()
    # showBoard(initialState)
    container = [initialState]
    # showBoard(container)
    stateCounter = 0
    visitedStates = []

    while container:
        currentState = container.pop(0) # Get the first state in the list.
        showBoard(currentState.queenLocations)
        print()
        print("   |")
        print("   |")
        print("  \|/")
        print()
        stateCounter = stateCounter + 1 # Maintain a counter for the number of states encountered.
        visitedStates.append(list(currentState.queenLocations))
        if len(currentState.queenLocations) == 4:                   # This portion is the stopping condition for the execution
            return currentState.queenLocations, stateCounter        # when all 4 queens have been placed on the board satisfying the
                                                                    # capture conditions.

        for i in range(4):
            if i not in currentState.queenLocations:
                addedLocations = currentState.queenLocations + [i]  # This portion cycles through all possible numbers in queenLocations array
                if list(addedLocations) not in visitedStates:       # and adds them to the array as elements. These are then verified for presence
                    container.append(State(addedLocations))         # in the visited states list for prevention of revisitation, successfully generating
                    visitedStates.append(list(addedLocations))      # and cycling through new states.

        container.sort() # This is where the function override for the less than property is used.
                         # When all the states in the list are being sorted their heuristics are calculated
                         # using the heuristicCalculation function in the less than override and compared.


queenLocations, counter = GBFS()
print("Solution reached:")
showBoard(queenLocations)
print()
print(f"Number of states traversed is: {counter}")
