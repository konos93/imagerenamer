import re
from collections import Counter

# Read the input text file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Dictionary to store the most common number for each filename
filename_most_common = {}

# Iterate through the lines and extract the most common number
for line in lines:
    match = re.search(r'Filename: (\d+).JPG, Filtered Recognized Numbers between 10 and 1299: (\[.*\])', line)
    if match:
        filename = match.group(1).zfill(4) + '.jpg'
        numbers = eval(match.group(2))
        
        if not numbers:  # If the list is empty, set '0000'
            most_common_number = '0000'
        else:
            most_common_number = Counter(numbers).most_common(1)[0][0]
            
        filename_most_common[filename] = most_common_number

# Write the output to a new text file
with open('output.txt', 'w') as output_file:
    for filename, most_common_number in sorted(filename_most_common.items()):
        output_file.write(f"{filename}:{str(most_common_number).zfill(4)}\n")
