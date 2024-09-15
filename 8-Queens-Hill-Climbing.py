import random

# Helper function to calculate number of conflicts (heuristic)
def calculate_conflicts(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Function to print the board as a matrix
def print_board(state):
    n = len(state)
    board = [["." for _ in range(n)] for _ in range(n)]
    
    for col, row in enumerate(state):
        board[row][col] = "Q"
    
    for row in board:
        print(" ".join(row))
    print()

# Hill Climbing with max iterations
def hill_climbing(state, max_iterations=1000):
    current_conflicts = calculate_conflicts(state)
    iterations = 0
    while iterations < max_iterations:
        neighbors = []
        for col in range(len(state)):
            for row in range(len(state)):
                if state[col] != row:
                    new_state = state[:]
                    new_state[col] = row
                    neighbors.append((new_state, calculate_conflicts(new_state)))
        
        # Find the best neighbor
        best_neighbor, best_conflicts = min(neighbors, key=lambda x: x[1])

        # If no improvement, return current state
        if best_conflicts >= current_conflicts:
            return state, iterations, current_conflicts
        
        state = best_neighbor
        current_conflicts = best_conflicts
        iterations += 1
    
    return state, iterations, current_conflicts

# First-choice Hill Climbing with max iterations
def first_choice_hill_climbing(state, max_iterations=1000):
    current_conflicts = calculate_conflicts(state)
    iterations = 0
    while iterations < max_iterations:
        for _ in range(100):  # Try random moves
            col = random.randint(0, 7)
            row = random.randint(0, 7)
            if state[col] != row:
                new_state = state[:]
                new_state[col] = row
                new_conflicts = calculate_conflicts(new_state)

                if new_conflicts < current_conflicts:
                    state = new_state
                    current_conflicts = new_conflicts
                    break
        if calculate_conflicts(state) == 0:
            return state, iterations, current_conflicts
        
        iterations += 1
    
    return state, iterations, current_conflicts

# Random Restart Hill Climbing with max restarts
def random_restart_hill_climbing(max_restarts=50):
    total_iterations = 0
    for attempt in range(max_restarts):
        state = [random.randint(0, 7) for _ in range(8)]
        solution, iterations, conflicts = hill_climbing(state)
        total_iterations += iterations

        if calculate_conflicts(solution) == 0:
            return solution, total_iterations, conflicts
    
    return None, total_iterations, -1  # Return -1 conflicts if no solution found

# Main Function
def solve_8_queens():
    print("Hill Climbing Algorithm:")
    initial_state = [random.randint(0, 7) for _ in range(8)]
    solution_hc, iterations_hc, conflicts_hc = hill_climbing(initial_state)
    print("Final Solution (Hill Climbing):")
    print_board(solution_hc)
    print(f"Iterations: {iterations_hc}, Final Conflicts (Heuristic): {conflicts_hc}\n")
    
    print("First-choice Hill Climbing Algorithm:")
    initial_state = [random.randint(0, 7) for _ in range(8)]
    solution_fchc, iterations_fchc, conflicts_fchc = first_choice_hill_climbing(initial_state)
    print("Final Solution (First-choice Hill Climbing):")
    print_board(solution_fchc)
    print(f"Iterations: {iterations_fchc}, Final Conflicts (Heuristic): {conflicts_fchc}\n")
    
    print("Random Restart Hill Climbing Algorithm:")
    solution_rrhc, total_iterations_rrhc, conflicts_rrhc = random_restart_hill_climbing()
    if solution_rrhc:
        print("Final Solution (Random Restart Hill Climbing):")
        print_board(solution_rrhc)
        print(f"Total Iterations: {total_iterations_rrhc}, Final Conflicts (Heuristic): {conflicts_rrhc}\n")
    else:
        print(f"No solution found after {total_iterations_rrhc} total iterations.")

# Run the 8-Queens Solver
solve_8_queens()


