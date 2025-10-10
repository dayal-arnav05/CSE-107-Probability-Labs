import random
import pandas as pd

trials = 1000
n = 300

#function to flip bob's coins 
def flip_bob(n, p):
    return sum(random.random() < p for _ in range(n+1))

#function to flip alice's coins 
def flip_alice(n, p):
    return sum(random.random() < p for _ in range(n))

# Part 1: Fair coins (p = 0.5)
bob_wins = 0
for trial_index in range(trials):
    bob_heads = flip_bob(n, 0.5)
    alice_heads = flip_alice(n, 0.5)
    #compare the number of heads
    if bob_heads > alice_heads:
        bob_wins += 1

#print the relative frequency
print("Part 1: Fair Coins (p = 0.5)")
print(f"Relative frequency of Bob winning: {bob_wins / trials:.3f}\n")

# Part 2: Loaded coins with different probabilities
print("Part 2: Loaded Coins")
p_values = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
results = []

for p in p_values:
    bob_wins = 0
    for trial_index in range(trials):
        bob_heads = flip_bob(n, p)
        alice_heads = flip_alice(n, p)
        #compare the number of heads
        if bob_heads > alice_heads:
            bob_wins += 1
    
    relative_freq = bob_wins / trials
    results.append({'p': p, 'relative frequency': relative_freq})

df = pd.DataFrame(results)
print(df.to_string(index=False))



