"""
Lab 3: Lottery Experiment Simulation
CSE 107 - Probability and Statistics

This simulation models Joe's lottery playing behavior over n weeks.
- Each week, with probability p, Joe plays the lottery (incrementing X)
- If Joe plays, with probability q, he wins (incrementing Y)
- We simulate 100,000 trials to estimate joint, marginal, and conditional PMFs
"""

import numpy as np
from collections import defaultdict


def simulate_lottery_trial(n_weeks, p_play, q_win):
    """
    Simulate one trial of n weeks of lottery play.
    
    Parameters:
    -----------
    n_weeks : int
        Number of weeks to simulate
    p_play : float
        Probability that Joe plays in a given week
    q_win : float
        Probability that Joe wins when he plays
    
    Returns:
    --------
    tuple (x, y) where:
        x = number of times Joe played
        y = number of times Joe won
    """
    x = 0  # Number of times Joe played
    y = 0  # Number of times Joe won
    
    for week in range(n_weeks):
        # Flip coin to decide if Joe plays this week
        if np.random.random() < p_play:
            x += 1
            # Joe played, now flip coin to decide if he wins
            if np.random.random() < q_win:
                y += 1
    
    return (x, y)


def run_simulation(n_weeks, p_play, q_win, n_trials=100000):
    """
    Run the lottery simulation for multiple trials.
    
    Parameters:
    -----------
    n_weeks : int
        Number of weeks per trial
    p_play : float
        Probability that Joe plays in a given week
    q_win : float
        Probability that Joe wins when he plays
    n_trials : int
        Number of trials to simulate (default: 100,000)
    
    Returns:
    --------
    dict : frequency counts for each (x, y) pair
    """
    frequency = defaultdict(int)
    
    for trial in range(n_trials):
        x, y = simulate_lottery_trial(n_weeks, p_play, q_win)
        frequency[(x, y)] += 1
        
        # Progress indicator for long simulations
        if (trial + 1) % 10000 == 0:
            print(f"Completed {trial + 1}/{n_trials} trials...")
    
    return frequency


def compute_joint_pmf(frequency, n_trials):
    """
    Compute the joint PMF from frequency counts.
    
    Returns:
    --------
    dict : joint PMF p_{X,Y}(x,y)
    """
    joint_pmf = {}
    for (x, y), count in frequency.items():
        joint_pmf[(x, y)] = count / n_trials
    return joint_pmf


def compute_marginal_pmf_x(joint_pmf):
    """
    Compute marginal PMF p_X(x) by summing over y values.
    """
    marginal_x = defaultdict(float)
    for (x, y), prob in joint_pmf.items():
        marginal_x[x] += prob
    return dict(marginal_x)


def compute_marginal_pmf_y(joint_pmf):
    """
    Compute marginal PMF p_Y(y) by summing over x values.
    """
    marginal_y = defaultdict(float)
    for (x, y), prob in joint_pmf.items():
        marginal_y[y] += prob
    return dict(marginal_y)


def compute_conditional_pmf_y_given_x(joint_pmf, marginal_x):
    """
    Compute conditional PMF p_{Y|X}(y|x) = p_{X,Y}(x,y) / p_X(x)
    """
    conditional = {}
    for (x, y), joint_prob in joint_pmf.items():
        if marginal_x[x] > 0:
            conditional[(x, y)] = joint_prob / marginal_x[x]
        else:
            conditional[(x, y)] = 0.0
    return conditional


def compute_conditional_pmf_x_given_y(joint_pmf, marginal_y):
    """
    Compute conditional PMF p_{X|Y}(x|y) = p_{X,Y}(x,y) / p_Y(y)
    """
    conditional = {}
    for (x, y), joint_prob in joint_pmf.items():
        if marginal_y[y] > 0:
            conditional[(x, y)] = joint_prob / marginal_y[y]
        else:
            conditional[(x, y)] = 0.0
    return conditional


def print_joint_pmf_table(joint_pmf):
    """Print the joint PMF in table format."""
    if not joint_pmf:
        print("No data to display")
        return
    
    x_values = sorted(set(x for x, y in joint_pmf.keys()))
    y_values = sorted(set(y for x, y in joint_pmf.keys()))
    
    print("\nJoint PMF p_{X,Y}(x,y)")
    print("x\\y" + "".join(f"{y:8d}" for y in y_values))
    print("-" * (4 + 8 * len(y_values)))
    
    for x in x_values:
        row = f"{x:2d} |"
        for y in y_values:
            prob = joint_pmf.get((x, y), 0.0)
            row += f"{prob:8.4f}"
        print(row)


def print_marginal_pmf_x(marginal_x):
    """Print the marginal PMF for X."""
    print("\nMarginal PMF p_X(x)")
    print("x: ", end="")
    for x in sorted(marginal_x.keys()):
        print(f"{x:8d}", end="")
    print()
    
    print("p: ", end="")
    for x in sorted(marginal_x.keys()):
        print(f"{marginal_x[x]:8.4f}", end="")
    print()


def print_marginal_pmf_y(marginal_y):
    """Print the marginal PMF for Y."""
    print("\nMarginal PMF p_Y(y)")
    print("y: ", end="")
    for y in sorted(marginal_y.keys()):
        print(f"{y:8d}", end="")
    print()
    
    print("p: ", end="")
    for y in sorted(marginal_y.keys()):
        print(f"{marginal_y[y]:8.4f}", end="")
    print()


def print_conditional_pmf_y_given_x(conditional, joint_pmf):
    """Print the conditional PMF p_{Y|X}(y|x) in table format."""
    if not conditional:
        print("No data to display")
        return
    
    x_values = sorted(set(x for x, y in joint_pmf.keys()))
    y_values = sorted(set(y for x, y in joint_pmf.keys()))
    
    print("\nConditional PMF of Y given X: p_{Y|X}(y|x)")
    print("y:" + "".join(f"{y:8d}" for y in y_values))
    print("x " + "-" * (8 * len(y_values)))
    
    for x in x_values:
        row = f"{x:2d} |"
        for y in y_values:
            prob = conditional.get((x, y), 0.0)
            row += f"{prob:8.4f}"
        print(row)


def print_conditional_pmf_x_given_y(conditional, joint_pmf):
    """Print the conditional PMF p_{X|Y}(x|y) in table format."""
    if not conditional:
        print("No data to display")
        return
    
    x_values = sorted(set(x for x, y in joint_pmf.keys()))
    y_values = sorted(set(y for x, y in joint_pmf.keys()))
    
    print("\nConditional PMF of X given Y: p_{X|Y}(x|y)")
    print("x:" + "".join(f"{x:8d}" for x in x_values))
    print("y " + "-" * (8 * len(x_values)))
    
    for y in y_values:
        row = f"{y:2d} |"
        for x in x_values:
            prob = conditional.get((x, y), 0.0)
            row += f"{prob:8.4f}"
        print(row)


def main():
    """Main function to run the lottery experiment."""
    print("=" * 70)
    print("Lab 3: Lottery Experiment Simulation")
    print("=" * 70)
    
    # Simulation parameters
    n_weeks = int(input("Enter the number of weeks (n): "))
    p_play = float(input("Enter the probability Joe plays each week (p): "))
    q_win = float(input("Enter the probability Joe wins when he plays (q): "))
    n_trials = 100000
    
    print(f"\nRunning simulation with:")
    print(f"  - n = {n_weeks} weeks per trial")
    print(f"  - p = {p_play} (probability of playing)")
    print(f"  - q = {q_win} (probability of winning when playing)")
    print(f"  - {n_trials} trials")
    print()
    
    # Set random seed for reproducibility (optional)
    np.random.seed(42)
    
    # Run the simulation
    frequency = run_simulation(n_weeks, p_play, q_win, n_trials)
    
    # Compute PMFs
    print("\nComputing PMFs...")
    joint_pmf = compute_joint_pmf(frequency, n_trials)
    marginal_x = compute_marginal_pmf_x(joint_pmf)
    marginal_y = compute_marginal_pmf_y(joint_pmf)
    conditional_y_given_x = compute_conditional_pmf_y_given_x(joint_pmf, marginal_x)
    conditional_x_given_y = compute_conditional_pmf_x_given_y(joint_pmf, marginal_y)
    
    # Print results
    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)
    
    print_joint_pmf_table(joint_pmf)
    print_marginal_pmf_x(marginal_x)
    print_marginal_pmf_y(marginal_y)
    print_conditional_pmf_y_given_x(conditional_y_given_x, joint_pmf)
    print_conditional_pmf_x_given_y(conditional_x_given_y, joint_pmf)
    
    print("\n" + "=" * 70)
    print("Simulation complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()

