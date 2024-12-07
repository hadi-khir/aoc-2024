import re

total_sum = 0

with open("input.txt", "r") as file:
    content = file.read()

print("----Part One----");

mulArr = re.findall(r"mul\(\d+,\d+\)", content)

for value in mulArr:
    nums = re.findall(r"\d+", value)
    x, y = map(int, nums)
    total_sum += x * y 

print(f"Part One: {total_sum}")

print("----Part Two----")

total_sum = 0

instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", content)

isEnabled = True # initially set to true

for value in instructions:
    if (value == 'do()'):
        isEnabled = True
        continue
    elif (value == "don't()"):
        isEnabled = False
        continue
    
    if (isEnabled):
        nums = re.findall(r"\d+", value)
        x, y = map(int, nums)
        total_sum += x * y 


print(f"Part Two: {total_sum}")