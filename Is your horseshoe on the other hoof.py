import sys

def solve():
    # Read 4 space-separated integers (horseshoe colors)
    horseshoes = list(map(int, sys.stdin.readline().split()))
    
    # Use a set to count unique colors
    unique_colors = len(set(horseshoes))
    
    # Calculate how many need to be replaced
    replacements = 4 - unique_colors
    
    # Print the result
    print(replacements)

# Execute the function
solve()
