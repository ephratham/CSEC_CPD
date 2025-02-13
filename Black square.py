import sys

def solve():
    # Read calorie values for squares 1, 2, 3, 4
    calories = list(map(int, sys.stdin.readline().split()))
    
    # Read the sequence of key presses
    sequence = sys.stdin.readline().strip()
    
    # Calculate total calories
    total_calories = sum(calories[int(char) - 1] for char in sequence)
    
    # Print the result
    print(total_calories)

# Execute the function
solve()
