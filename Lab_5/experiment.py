"""
Lab 5: Sum of Exponentials CDF Simulation
CSE 107 - Probability and Statistics

This simulation constructs the CDF of Z = Y1 + Y2, where Y1 and Y2 are
independent exponential random variables with parameter λ = 1.

We use the inverse transform method to generate exponential random variables:
- Generate U ~ Uniform(0, 1)
- Transform to Y = -ln(1 - U) ~ Exponential(1)

The resulting distribution of Z is called the Erlang distribution.
"""

import random
import math


def generate_exponential():
    """
    Generate a single exponential random variable with λ = 1.
    
    Uses the inverse transform method:
    - Generate U ~ Uniform(0, 1)
    - Return Y = -ln(1 - U)
    
    Returns:
    --------
    float : exponential random variable
    """
    u = random.random()
    return -math.log(1 - u)


def simulate_sum_of_exponentials(n_trials=20000):
    """
    Simulate n_trials samples of Z = Y1 + Y2, where Y1 and Y2 are
    independent exponential random variables.
    
    Parameters:
    -----------
    n_trials : int
        Number of trials to simulate (default: 20,000)
    
    Returns:
    --------
    list : samples of Z
    """
    z_samples = []
    
    for trial in range(n_trials):
        # Generate two independent exponential random variables
        y1 = generate_exponential()
        y2 = generate_exponential()
        
        # Compute their sum
        z = y1 + y2
        z_samples.append(z)
        
        # Progress indicator
        if (trial + 1) % 5000 == 0:
            print(f"Completed {trial + 1}/{n_trials} trials...")
    
    return z_samples


def compute_cdf(z_samples):
    """
    Compute the empirical CDF F_Z(z) = P(Z ≤ z) for z in [0.0, 9.9]
    at intervals of 0.1.
    
    Parameters:
    -----------
    z_samples : list
        List of Z samples
    
    Returns:
    --------
    dict : CDF values with keys (row, col) corresponding to z = row + col/10
    """
    n_trials = len(z_samples)
    cdf = {}
    
    # Compute CDF for z from 0.0 to 9.9 in increments of 0.1
    for row in range(10):  # 0.0, 1.0, 2.0, ..., 9.0
        for col in range(10):  # .0, .1, .2, ..., .9
            z_value = row + col / 10.0
            
            # Count how many samples are ≤ z_value
            count = sum(1 for z in z_samples if z <= z_value)
            
            # Compute relative frequency
            cdf[(row, col)] = count / n_trials
    
    return cdf


def print_cdf_table(cdf):
    """
    Print the CDF in table format matching the standard normal table layout.
    
    The table has rows for 0.0, 1.0, 2.0, ..., 9.0 and columns for 
    .0, .1, .2, ..., .9
    """
    print("\nSum of Exponentials CDF: F_Z(z) = P(Z ≤ z)")
    print("=" * 90)
    print("\nz    | ", end="")
    for col in range(10):
        print(f"    .{col}", end="")
    print()
    print("-" * 90)
    
    for row in range(10):
        print(f"{row}.0  | ", end="")
        for col in range(10):
            value = cdf[(row, col)]
            print(f" {value:.4f}", end="")
        print()
    
    print()
    print("Note: To find F_Z(4.7), look at row 4.0 and column .7")


def verify_distribution(z_samples):
    """
    Print some statistics to verify the distribution.
    
    For Z = Y1 + Y2 where Y1, Y2 ~ Exp(1):
    - E[Z] = E[Y1] + E[Y2] = 1 + 1 = 2
    - Var[Z] = Var[Y1] + Var[Y2] = 1 + 1 = 2
    """
    n = len(z_samples)
    mean = sum(z_samples) / n
    variance = sum((z - mean) ** 2 for z in z_samples) / n
    
    print("\nDistribution Statistics:")
    print("-" * 40)
    print(f"Sample mean:     {mean:.4f}  (Expected: 2.0)")
    print(f"Sample variance: {variance:.4f}  (Expected: 2.0)")
    print(f"Sample std dev:  {math.sqrt(variance):.4f}  (Expected: {math.sqrt(2):.4f})")


def main():
    """Main function to run the experiment."""
    print("=" * 90)
    print("Lab 5: Sum of Exponentials CDF Simulation")
    print("=" * 90)
    print("\nThis experiment simulates Z = Y1 + Y2 where Y1, Y2 ~ Exponential(1)")
    print("using the inverse transform method: Y = -ln(1 - U) for U ~ Uniform(0,1)")
    print()
    
    # Set random seed for reproducibility (optional - comment out for random results)
    random.seed(42)
    
    # Run simulation
    n_trials = 20000
    print(f"Running {n_trials} trials...\n")
    z_samples = simulate_sum_of_exponentials(n_trials)
    
    # Compute CDF
    print("\nComputing CDF...")
    cdf = compute_cdf(z_samples)
    
    # Print results
    print("\n" + "=" * 90)
    print("RESULTS")
    print("=" * 90)
    
    print_cdf_table(cdf)
    verify_distribution(z_samples)
    
    print("\n" + "=" * 90)
    print("Simulation complete!")
    print("=" * 90)


if __name__ == "__main__":
    main()

