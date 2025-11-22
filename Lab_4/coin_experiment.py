"""
Lab 4: Compound Coin Flip Experiment
CSE 107 - Probability and Statistics

This simulation models a two-stage coin flipping process:
1. Flip Coin 1 (probability p) until first head appears → N flips (Geometric)
2. Flip Coin 2 (probability q) exactly N times → Y heads (sum of N Bernoulli trials)

We compute E[Y] and Var[Y] experimentally for all combinations of p, q ∈ {0.1, 0.2, ..., 0.9}
using 10,000 trials per combination.
"""

import numpy as np


def flip_coin_until_heads(p):
    """
    Flip a coin with probability p of heads until first head appears.
    
    Parameters:
    -----------
    p : float
        Probability of heads for Coin 1
    
    Returns:
    --------
    int : Number of flips needed (N)
    """
    flips = 0
    while True:
        flips += 1
        if np.random.random() < p:  # Got heads
            return flips


def count_heads_in_n_flips(q, n):
    """
    Flip a coin n times and count the number of heads.
    
    Parameters:
    -----------
    q : float
        Probability of heads for Coin 2
    n : int
        Number of flips
    
    Returns:
    --------
    int : Number of heads (Y)
    """
    heads = 0
    for _ in range(n):
        if np.random.random() < q:  # Got heads
            heads += 1
    return heads


def simulate_compound_process(p, q, n_trials=10000):
    """
    Simulate the compound coin flip process for n_trials.
    
    Parameters:
    -----------
    p : float
        Probability of heads for Coin 1
    q : float
        Probability of heads for Coin 2
    n_trials : int
        Number of trials to run
    
    Returns:
    --------
    list : List of Y values (number of heads from Coin 2)
    """
    y_values = []
    
    for _ in range(n_trials):
        # Stage 1: Flip Coin 1 until first head
        n = flip_coin_until_heads(p)
        
        # Stage 2: Flip Coin 2 exactly n times and count heads
        y = count_heads_in_n_flips(q, n)
        
        y_values.append(y)
    
    return y_values


def compute_mean_variance(y_values):
    """
    Compute mean and variance of Y values.
    
    Returns:
    --------
    tuple : (mean, variance)
    """
    y_array = np.array(y_values)
    mean = np.mean(y_array)
    variance = np.var(y_array, ddof=0)  # Population variance
    return mean, variance


def run_full_experiment(n_trials=10000):
    """
    Run the experiment for all combinations of p, q ∈ {0.1, 0.2, ..., 0.9}.
    
    Returns:
    --------
    tuple : (mean_table, variance_table) as 9x9 numpy arrays
    """
    prob_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    
    mean_table = np.zeros((9, 9))
    variance_table = np.zeros((9, 9))
    
    for i, p in enumerate(prob_values):
        for j, q in enumerate(prob_values):
            y_values = simulate_compound_process(p, q, n_trials)
            mean, variance = compute_mean_variance(y_values)
            mean_table[i, j] = mean
            variance_table[i, j] = variance
    
    return mean_table, variance_table


def print_table(table, title, prob_values):
    """
    Print a 9×9 table formatted according to assignment specifications.
    
    Parameters:
    -----------
    table : numpy array
        9×9 table of values
    title : str
        Title of the table (e.g., "Mean")
    prob_values : list
        List of probability values
    """
    print(f"\n{title}")
    print("    q:", end="")
    for q in prob_values:
        print(f"    {q:.1f}", end="")
    print()
    print("p")
    
    for i, p in enumerate(prob_values):
        print(f"{p:.1f}", end="")
        for j in range(9):
            print(f"  {table[i, j]:6.3f}", end="")
        print()


def main():
    """Main function to run the compound coin flip experiment."""
    np.random.seed(42)
    mean_table, variance_table = run_full_experiment(n_trials=10000)
    prob_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    
    print_table(mean_table, "Mean", prob_values)
    print()
    print_table(variance_table, "Variance", prob_values)


if __name__ == "__main__":
    main()

