import numpy as np
import pandas as pd


def preprocess_data(data):
    data = pd.DataFrame(data)
    data = data[0].str.split(" ", expand=True)
    data[3] = data[3].astype(int)
    data[3] = np.where(data[2] == "lose", data[3] * -1, data[3])
    data[10] = data[10].str.replace(".", "").str.replace("\n", "")
    data = data.drop([1, 2, 4, 5, 6, 7, 8, 9], axis=1)
    data.columns = ["Guest A", "Score A", "Guest B"]
    return data


def maximize_seating_score(df: pd.DataFrame):
    """
    Finds the optimal circular seating arrangement for guests to maximize total score.
    
    Parameters:
    - df: pandas DataFrame with columns ['Guest A', 'Score A', 'Guest B']
    
    Returns:
    - optimal_arrangement: List of guests in order around the circular table
    - max_score: Total combined score of the optimal arrangement
    """
    # 1. Build an undirected score matrix (Guest A sitting next to Guest B)
    # The total satisfaction of a pair sitting together is Score(A->B) + Score(B->A)
    guests = sorted(list(set(df['Guest A']).union(set(df['Guest B']))))
    n = len(guests)
    
    guest_to_idx = {g: i for i, g in enumerate(guests)}
    idx_to_guest = {i: g for i, g in enumerate(guests)}
    
    # Initialize affinity matrix with 0
    adj = [[0] * n for _ in range(n)]
    
    for _, row in df.iterrows():
        u = guest_to_idx[row['Guest A']]
        v = guest_to_idx[row['Guest B']]
        score = row['Score A']
        # Add mutual scores since seating adjacent benefits/affects both
        adj[u][v] += score
        adj[v][u] += score

    # 2. Branch and Bound DFS to find max weight Hamiltonian cycle
    best_score = float('-inf')
    best_path = []

    # Fix guest 0 at position 0 to break rotational symmetry
    start_guest = 0
    
    def dfs(current_guest, visited, path, current_score):
        nonlocal best_score, best_path
        
        # If all guests are seated, close the loop back to start_guest
        if len(path) == n:
            final_score = current_score + adj[current_guest][start_guest]
            if final_score > best_score:
                best_score = final_score
                best_path = path[:]
            return

        for next_guest in range(n):
            if not visited[next_guest]:
                # Optimization: Prune early if it's impossible to beat the best score
                # (Simple branch-and-bound optimization)
                visited[next_guest] = True
                path.append(next_guest)
                
                dfs(next_guest, visited, path, current_score +
                     adj[current_guest][next_guest])
                
                path.pop()
                visited[next_guest] = False

    # Break reflection symmetry by forcing guest 0's first neighbor index to be 
    # smaller than the last neighbor
    # (Optional micro-optimization: fixes 0 as starting node)
    visited = [False] * n
    visited[start_guest] = True
    dfs(start_guest, visited, [start_guest], 0)

    # Convert indices back to original guest names
    optimal_arrangement = [idx_to_guest[idx] for idx in best_path]
    
    return optimal_arrangement, best_score


def add_neutral_guest(df: pd.DataFrame, new_guest_name: str) -> pd.DataFrame:
    """
    Adds a new guest to the dataframe with 0 score toward everyone,
    and 0 score received from everyone.
    
    Parameters:
    - df: existing pandas DataFrame with columns ['Guest A', 'Score A', 'Guest B']
    - new_guest_name: Name of the new guest to add
    
    Returns:
    - Updated pandas DataFrame including the new guest
    """
    # Find all unique existing guests
    existing_guests = set(df['Guest A']).union(set(df['Guest B']))
    
    new_rows = []
    for guest in existing_guests:
        # Score from New Guest to existing guest
        new_rows.append({'Guest A': new_guest_name, 'Score A': 0, 'Guest B': guest})
        # Score from existing guest to New Guest
        new_rows.append({'Guest A': guest, 'Score A': 0, 'Guest B': new_guest_name})
    
    # Append the new rows to the DataFrame
    updated_df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
    
    return updated_df

if __name__ == "__main__":
    # DATA
    with open("./data/data_13.txt",) as file:
        data = file.read().splitlines()

    data = preprocess_data(data)
    order = maximize_seating_score(data)
    print(f"Part 1: {order[-1]}")

    data2 = add_neutral_guest(data, "Me")
    order2 = maximize_seating_score(data2)
    print(f"Part 2: {order2[-1]}")
