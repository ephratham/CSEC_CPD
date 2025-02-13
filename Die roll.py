import sys
import math

def solve():
    # Read input values
    Y, W = map(int, sys.stdin.readline().split())
    
    # The highest number rolled
    highest = max(Y, W)

    # Favorable outcomes (rolling at least `highest`)
    favorable = 6 - highest + 1  

    # Simplify the fraction
    gcd = math.gcd(favorable, 6)
    numerator = favorable // gcd
    denominator = 6 // gcd

    # Print the result as a fraction
    print(f"{numerator}/{denominator}")

# Execute the function
solve()
