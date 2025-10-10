# Lab Assignment 1 — CSE 107

[Assignment PDF](https://people.ucsc.edu/~ptantalo/cse107/Fall25/lab1.pdf)

## Problem Description

In this assignment you will simulate the experiment described in Problem 27 on page 59 of the textbook, which says:

> Alice and Bob have **2n+1** coins, each with probability of a head equal to **1/2**.  
> Bob tosses **n+1** coins, while Alice tosses the remaining **n** coins.  
> Assuming independent coin tosses, show that the probability that after all the coins have been tossed, Bob will have gotten more heads than Alice, is **1/2**.

## Part 1: Fair Coins

Write a program, in any language, that simulates this experiment with **n = 300**. Perform **1000 trials** of this experiment, and compute the relative frequency of Bob tossing more heads than Alice:

```
relative frequency = (number of trials in which Bob tossed more heads) / (total number of trials)
```

**Note:** This relative frequency is an approximation to P(Bob tosses more heads than Alice). Verify that your relative frequency is very close to 1/2.

## Part 2: Loaded Coins

Now suppose we do another sequence of 1000 trials with **2n+1** loaded coins (again **n = 300**). In particular:

1. Run all 1000 trials of the experiment, but now with the probability of heads equal to **p**.
2. Do this for each **p ∈ {0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8}**.

This should be possible by editing just a few lines of code (replacing 1/2 by a variable `p` which you initialize at the beginning of the program).

### Questions to Answer

- Does the probability that Bob tosses more heads than Alice now seem to depend on **p**, or is it still 1/2?
- Form a conjecture regarding that probability, and whether it depends (strongly, weakly, or not at all) on **p**.

### Required Table

Create a table containing, for each value of p, the relative frequency with which Bob throws more heads than Alice. Again you are running each experiment with **n = 300** and doing **1000 trials** for each value of p.

Your table should be formatted as:

| p   | relative frequency |
|-----|--------------------|
| 0.2 | 0.000              |
| 0.3 | 0.000              |
| 0.4 | 0.000              |
| 0.5 | 0.000              |
| 0.6 | 0.000              |
| 0.7 | 0.000              |
| 0.8 | 0.000              |

*(Replace 0.000 with your actual relative frequencies, rounded to 3 decimal places.)*

## Deliverable

Once your table is constructed, state your conjecture as to the probability that Bob tosses more heads, and how (strongly, weakly, or not at all) that probability depends on **p**.

Submit your answers in a PDF file (called `lab1.pdf`) to Gradescope before the due date.
