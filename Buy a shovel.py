import sys

def solve():
    # Read input values
    k, r = map(int, sys.stdin.readline().split())
    
    # Find the minimum number of shovels
    n = 1
    while True:
        cost = k * n
        if cost % 10 == 0 or cost % 10 == r:
            print(n)
            return
        n += 1

# Execute the function
solve()
