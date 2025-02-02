class Puzzle:
    def __init__(self, board, goal, blank=(0, 0)):
        self.board = board
        self.goal = goal
        self.blank = blank

    # Function to display the board
    def display(self):
        for row in self.board:
            print(row)
        print()

    # Find the position of the blank (0) tile
    def find_blank(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return i, j

    # Check if the current state is the goal state
    def is_goal(self):
        return self.board == self.goal

    # Generate possible moves from the current state
    def possible_moves(self):
        moves = []
        i, j = self.blank
        directions = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}
        for direction, (di, dj) in directions.items():
            ni, nj = i + di, j + dj
            if 0 <= ni < len(self.board) and 0 <= nj < len(self.board[0]):
                moves.append((direction, ni, nj))
        return moves

    # Move the blank tile in the given direction
    def move(self, new_blank):
        i, j = self.blank
        ni, nj = new_blank
        new_board = [row[:] for row in self.board]
        new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
        return Puzzle(new_board, self.goal, blank=(ni, nj))

    # Calculate Manhattan distance (heuristic)
    def heuristic(self):
        distance = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                value = self.board[i][j]
                if value != 0:  # Ignore the blank tile
                    for x in range(len(self.goal)):
                        for y in range(len(self.goal[x])):
                            if self.goal[x][y] == value:
                                distance += abs(x - i) + abs(y - j)
        return distance

    # A* Search Algorithm
    def solve(self):
        open_set = [(self, 0)]  # (current state, g value)
        visited = []

        while open_set:
            # Sort open_set by f = g + h
            open_set.sort(key=lambda x: x[1] + x[0].heuristic())
            current, g = open_set.pop(0)

            # Check if goal is reached
            if current.is_goal():
                print("Solution found:")
                current.display()
                return True

            # Mark current state as visited
            visited.append(current.board)

            # Generate possible moves
            for direction, ni, nj in current.possible_moves():
                next_state = current.move((ni, nj))
                if next_state.board not in visited:
                    open_set.append((next_state, g + 1))

        print("No solution found.")
        return False


# Define initial and goal states
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Initialize and solve the puzzle
puzzle = Puzzle(initial_state, goal_state)
print("Initial State:")
puzzle.display()
puzzle.solve()
