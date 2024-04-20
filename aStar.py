import heapq

class State:
    def __init__(self, queens=[], cost=0):
        self.queens = queens
        self.cost = cost
    
    def heuristic(self):
        conflicts = 0
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                if self.queens[i] == self.queens[j]:
                    conflicts += 1
                elif abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    
    def __lt__(self, other):
        return self.cost + self.heuristic() < other.cost + other.heuristic()

def a_star_search():
    start_state = State()
    open_list = [(start_state.cost + start_state.heuristic(), start_state)]
    visited_states = set()
    traversed_states = []

    while open_list:
        _, current_state = heapq.heappop(open_list)
        traversed_states.append(current_state)
        visited_states.add(tuple(current_state.queens))
        if len(current_state.queens) == 4:
            return current_state.queens, traversed_states

        for i in range(4):
            if i not in current_state.queens:
                new_queens = current_state.queens + [i]
                if tuple(new_queens) not in visited_states:
                    new_state = State(new_queens, current_state.cost + 1)
                    heapq.heappush(open_list, (new_state.cost + new_state.heuristic(), new_state))
                    visited_states.add(tuple(new_queens))

def print_board(queens):
    board = [['.' for _ in range(4)] for _ in range(4)]
    for i in range(4):
        board[i][queens[i]] = 'Q'
    for row in board:
        print(' '.join(row))

queens, traversed_states = a_star_search()
for i, state in enumerate(traversed_states):
    print(f"State {i + 1}: {state.queens}")
print(f"Total number of states traversed: {len(traversed_states)}")
print("\nFinal board:")
print_board(queens)
