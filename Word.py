import sys

def solve():
    # Read the input word
    word = sys.stdin.readline().strip()
    
    # Count uppercase and lowercase letters
    upper_count = sum(1 for char in word if char.isupper())
    lower_count = len(word) - upper_count  # Remaining are lowercase

    # Convert the word based on the counts
    if upper_count > lower_count:
        print(word.upper())
    else:
        print(word.lower())

# Execute the function
solve()
