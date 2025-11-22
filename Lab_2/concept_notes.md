# The Azure-Carmine Urn Problem: Why Restarts Create 50/50 Odds

## The Problem

An urn contains `a` azure balls and `c` carmine balls, where `a + c = n` total balls.

**Procedure:**
1. Select a ball at random and discard it (first ball has no predecessor)
2. Keep selecting balls randomly:
   - If same color as predecessor → discard it
   - If different color → **DO NOT discard**, **RESTART** the procedure
3. Continue until only 1 ball remains

**Claim:** P(last ball is azure) = P(last ball is carmine) = 1/2, **regardless of initial values of a and c**

---

## Why This is Counterintuitive

You'd naturally think:
- If you start with 10 azure and 90 carmine, carmine should win ~90% of the time
- If you start with 50 azure and 50 carmine, each should win ~50% of the time

**But that's wrong!** The probability is **always 50/50**, no matter the starting ratio.

---

## The Key Insight: What "Restart" Really Means

When you encounter a ball of a different color:
1. That ball is **not discarded** (it stays in the urn)
2. The procedure **restarts** (next ball selected has no predecessor, so is always discarded)

This creates an asymmetry in how balls get removed:
- **Same-colored balls** get removed in "runs" (discard, discard, discard...)
- **The different-colored ball** that breaks the run **survives** and triggers a restart

---

## Intuition: The Minority Color Gets "Extra Lives"

Consider the extreme case: **1 azure, 99 carmine**

### Without Restarts (naive approach):
- Probability azure is last = 1/100 = **1%**

### With Restarts:
1. First selection likely gets carmine (99% chance) → discard
2. Keep getting carmine (same color) → discard, discard, discard...
3. Eventually hit the azure ball (different color!) → **azure SURVIVES, restart**
4. Now say 1 azure, 30 carmine remain
5. Likely get carmine again → discard
6. Keep getting carmine → discard, discard...
7. Hit azure again → **azure SURVIVES again!**

The rare azure ball gets to "survive" multiple times by triggering restarts, while carmine balls keep getting eliminated in long runs of same-colored selections.

**This balancing effect makes it 50/50!**

---

## Why Shuffle-Once Doesn't Work

### Approach 1: Shuffle once, process sequentially ❌

```python
balls = ['a'] * a + ['c'] * c
random.shuffle(balls)  # Shuffle ONCE at the start

# Then always check balls[0], remove from front
while len(balls) > 1:
    # ... process balls[0] ...
    balls.pop(0)
```

**Problem:** Once shuffled, the list is **fixed**. You're just removing from the front until you reach the last element.
- The last ball in the shuffled list will always win
- P(last ball is azure) = a/(a+c) ❌

### Approach 2: Random selection each time ✓

```python
balls = ['a'] * a + ['c'] * c
# NO shuffle needed!

while len(balls) > 1:
    current = random.choice(balls)  # Random choice from REMAINING balls
    balls.remove(current)
```

**Key difference:** Each `random.choice()` is selecting from the **current** remaining balls, not from a fixed pre-shuffled sequence.
- The probabilities change dynamically as balls are removed
- The restart mechanism creates the 50/50 symmetry
- P(last ball is azure) = 1/2 ✓

---

## The Mathematical Magic

The procedure creates a **symmetric** process with respect to colors:
- Both colors have equal "power" to survive via triggering restarts
- The minority color benefits from staying alive when encountered (triggers restart)
- The majority color gets eliminated faster in same-color runs
- These effects perfectly balance out to 50/50

This is similar to the concept of a **fair game** in probability theory, where no player has an inherent advantage despite starting from asymmetric positions.

---

## Key Takeaways

1. **Shuffling once ≠ Random selection each time**
   - Shuffle-once creates a fixed sequence (last element wins with probability a/(a+c))
   - Random selection each time creates dynamic probabilities (always 50/50)

2. **Restart mechanism is crucial**
   - Without restarts: probability depends on initial ratio
   - With restarts: creates symmetry → always 50/50

3. **Rare colors get "extra lives"**
   - Minority color survives by triggering restarts
   - Majority color gets eliminated in same-color runs
   - This perfectly balances the odds

4. **Experimental verification**
   - Run 2000 trials for a = 10, 20, 30, 40, 50
   - All should show ~0.5000 proportion ending in azure
   - Demonstrates the probability is independent of initial values

---

## Real-World Analogy

Think of it like a survival game where:
- Being in the **minority** gives you a "shield" (restart protection)
- Being in the **majority** makes you vulnerable (eliminated in groups)
- These two effects perfectly cancel out!

It's like a weighted coin that adjusts its weights after each flip to stay perfectly fair.

---

## Further Reading

This problem comes from *Probability and Random Processes* by Grimmett and Stirzaker, and demonstrates how **dynamic random processes** can behave very differently from **static random arrangements**.

It's a great example of how **the mechanism of randomness matters**, not just the randomness itself!

