from collections import Counter

leftIds = []
rightIds = []
distance = 0
similarityScore = 0

# Read and parse input file
with open("input.txt") as file:
    for line in file:
        locationIds = line.strip().split()  # Handles arbitrary whitespace
        try:
            leftIds.append(int(locationIds[0]))
            rightIds.append(int(locationIds[1]))
        except (ValueError, IndexError):
            print(f"Skipping invalid line: {line}")

# Check for mismatched lengths
if len(leftIds) != len(rightIds):
    raise ValueError("Mismatch in number of IDs between left and right.")

print("---- Part One ----")

# Sort for distance calculation
leftIds_sorted = sorted(leftIds)
rightIds_sorted = sorted(rightIds)

# Calculate distance
for x in range(len(leftIds_sorted)):
    distance += abs(leftIds_sorted[x] - rightIds_sorted[x])

print(f"Distance: {distance}")

print("---- Part Two ----")

# Calculate similarity score
counter = Counter(rightIds)
for id in leftIds:
    frequency = counter.get(id, 0)
    similarityScore += id * frequency

print(f"Similarity Score: {similarityScore}")