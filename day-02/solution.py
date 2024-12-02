def is_safe(level):
    """Check if a report is safe based on the original rules."""
    if len(level) < 2:  # Single-element levels are inherently safe
        return True

    # Determine the initial direction
    direction = level[1] - level[0]
    if abs(direction) < 1 or abs(direction) > 3:  # Rule 2: Difference must be between 1 and 3
        return False

    is_increasing = direction > 0  # True if increasing, False if decreasing

    for i in range(1, len(level)):
        diff = level[i] - level[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:  # Rule 2: Difference must be between 1 and 3
            return False
        if (diff > 0) != is_increasing:  # Rule 1: Consistent direction
            return False

    return True

def is_safe_with_dampener(level):
    """Check if a report is safe with the Problem Dampener."""
    if is_safe(level):  # Already safe without removing any levels
        return True

    # Try removing each level and check if the remaining report is safe
    for i in range(len(level)):
        modified_level = level[:i] + level[i+1:]  # Remove the ith level
        if is_safe(modified_level):  # Check if the modified report is safe
            return True

    return False

# Main logic to process the input file
levels = []
safeCount = 0

# Read and parse input file
with open("input.txt") as file:
    for line in file:
        try:
            # Parse each line as a list of integers
            level = list(map(int, line.strip().split()))
            levels.append(level)
        except ValueError:
            print(f"Error parsing line: {line.strip()}")

# Count safe reports with the Problem Dampener
for level in levels:
    if is_safe_with_dampener(level):
        safeCount += 1

print(safeCount)
