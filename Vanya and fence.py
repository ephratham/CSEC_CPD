# Read input values
n, h = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate the required width
width = sum(2 if height > h else 1 for height in heights)

# Print the result
print(width)
