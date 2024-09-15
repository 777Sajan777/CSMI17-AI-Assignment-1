import random

# Function to calculate number of conflicts (heuristic function)
def calc_conflicts(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Function used to print the state(board) as a matrix
def print_board(state):
    n = len(state)
    board = [["." for _ in range(n)] for _ in range(n)]
    
    for col, row in enumerate(state):
        board[row][col] = "Q"
    
    for row in board:
        print(" ".join(row))
    print()

# Hill Climbing algorithm with required no. of max iterations
def hill_climbing(state, max_iterations=1000):
    current_conflicts = calc_conflicts(state)
    iter = 0
    
    while iter < max_iterations:
        neighbor_states = []
        n = len(state)
        
        # Generate neighbors by moving each queen to different positions in its column
        for col in range(n):
            for row in range(n):
                if state[col] != row:
                    new_state = state[:]
                    new_state[col] = row
                    neighbor_states.append((new_state, calc_conflicts(new_state)))
        
        if not neighbor_states:
            return state, iter, current_conflicts
        
        # Find the best neighbor with the minimum number of conflicts
        best_neighbor, best_conflicts = min(neighbor_states, key=lambda x: x[1])
        
        if best_conflicts >= current_conflicts:
            return state, iter, current_conflicts
        
        state = best_neighbor
        current_conflicts = best_conflicts
        iter += 1
    
    return state, iter, current_conflicts


# First-choice Hill Climbing with required no. of max iterations
def first_choice_hill_climbing(state, max_iterations=1000):
    current_conflicts = calc_conflicts(state)
    iter = 0
    while iter < max_iterations:
        for _ in range(100):  # Try random moves
            col = random.randint(0, 7)
            row = random.randint(0, 7)
            if state[col] != row:
                new_state = state[:]
                new_state[col] = row
                new_conflicts = calc_conflicts(new_state)

                if new_conflicts < current_conflicts:
                    state = new_state
                    current_conflicts = new_conflicts
                    break
        if calc_conflicts(state) == 0:
            return state, iter, current_conflicts
        
        
        iter += 1
    
    return state, iter, current_conflicts

# Random Restart Hill Climbing with required no. of max restarts
def random_restart_hill_climbing(max_restarts=50):
    total_iterations = 0
    for _ in range(max_restarts):
        state = [random.randint(0, 7) for _ in range(8)]
        solution, iter, conflicts = hill_climbing(state)
        total_iterations += iter

        if calc_conflicts(solution) == 0:
            return solution, total_iterations, conflicts
    
    return None, total_iterations, -1  # Returns -1 conflicts if no solution found

# Main Function to solve the problem
def solve_8_queens():
    
    print("Hill Climbing Algorithm: ")
    initial_state = [random.randint(0, 7) for _ in range(8)]
    solution_hc, iter_hc, conflicts_hc = hill_climbing(initial_state)
    
    print("Final Solution (Hill Climbing): ")
    print_board(solution_hc)
    print(f"Iterations: {iter_hc}, Final Conflicts (Heuristic): {conflicts_hc}\n")
    
    print("First-choice Hill Climbing Algorithm: ")
    initial_state = [random.randint(0, 7) for _ in range(8)]
    solution_fc_hc, iter_fc_hc, conflicts_fc_hc = first_choice_hill_climbing(initial_state) 
    
    print("Final Solution (First-choice Hill Climbing): ")
    print_board(solution_fc_hc)
    print(f"Iterations: {iter_fc_hc}, Final Conflicts (Heuristic): {conflicts_fc_hc}\n")
    
    print("Random Restart Hill Climbing Algorithm: ")
    solution_rr_hc, total_iter_rr_hc, conflicts_rr_hc = random_restart_hill_climbing()
    
    if solution_rr_hc:
        print("Final Solution (Random Restart Hill Climbing): ")
        print_board(solution_rr_hc)
        print(f"Total Iterations: {total_iter_rr_hc}, Final Conflicts (Heuristic): {conflicts_rr_hc}\n")
    else:
        print(f"No solution found after {total_iter_rr_hc} total iterations.")

# Running the 8-Queens Problem Solver
solve_8_queens()


