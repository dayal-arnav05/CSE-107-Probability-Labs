import random

n = 2000 #number of trials


#function for procedure
def procedure(a, c):
    # Create the urn with all balls
    balls = ['a'] * a + ['c'] * c
    
    # Continue until only one ball remains
    while len(balls) > 1:
        # First selection has no predecessor, so always discard it
        current_ball = random.choice(balls)
        balls.remove(current_ball)
        previous_ball = current_ball
        
        # If we're down to 1 ball, we're done
        if len(balls) == 1:
            break
            
        # Keep selecting and discarding balls with the same color as previous
        while len(balls) > 1:
            current_ball = random.choice(balls)
            
            if current_ball != previous_ball:
                break
            else:
                balls.remove(current_ball)
                previous_ball = current_ball
    
    return balls[0]

#run the experiment
def run_experiment(a, c, n):
    a_wins = 0
    c_wins = 0
    for i in range(n):
        result = procedure(a, c)
        if result == 'a':
            a_wins += 1
        else:
            c_wins += 1
    return a_wins / n

# Print results in table format as specified in assignment
print("#azure\t#carmine\tproportion ending in azure")
print("------\t--------\t--------------------------")
for a in [10, 20, 30, 40, 50]:
    c = 100 - a
    proportion = run_experiment(a, c, n)
    print(f"{a}\t{c}\t\t{proportion:.4f}")
