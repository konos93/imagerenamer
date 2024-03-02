import cv2
import numpy as np
import os
from tkinter import filedialog
from tkinter import Tk
import concurrent.futures


# Function to process a single image
def process_image(input_path, output_folder):
    # Load the cropped image in grayscale
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Apply Otsu's thresholding to convert to black and white
    _, bw_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Get the height and width of the image
    h, w = bw_image.shape

    # Define the number of rows and columns of the grid
    rows = 75
    cols = 100

    # Calculate the size of each square in pixels
    square_h = h // rows
    square_w = w // cols

    # Create an empty array to store the grid values
    grid = np.empty((rows, cols), dtype=str)

    # Loop over the rows and columns of the grid
    for i in range(rows):
        for j in range(cols):
            # Get the coordinates of the top left corner of the square
            x = j * square_w
            y = i * square_h

            # Get the sub-image corresponding to the square
            square = bw_image[y:y+square_h, x:x+square_w]

            # Check if the square contains any black pixel 
            # to have a clearer image from black dots  > the number of ignored black pixels 
            if np.sum(square == 0) > 30:
                # Set the grid value to '#'
                grid[i, j] = '#'
            else:
                # Set the grid value to '0'
                grid[i, j] = '0'

    # Write the result to output.txt
    output_path = os.path.join(output_folder, f'{os.path.splitext(os.path.basename(input_path))[0]}_output.txt')
    with open(output_path, 'w') as file:
        for i in range(rows):
            for j in range(cols):
                file.write(grid[i, j])
            file.write('\n')

    # Define the  patterns ,lets play tetris like a page number detector.
    pattern1 = ['000000',
				'00##00', 
				'00##00', 
				'00##00', 
				'000000']
    pattern2 = ['000000',
				'000000', 
				'000##0', 
				'000##0',
				'000000', 
				'000000']
    pattern3 =['000000',
				'000000',
				'0##000',
				'0##000',
				'000000',
				'000000',
				'000000']                
    pattern4 = ['000000',
				'00#000', 
				'00##00', 
				'00##00',
				'000000', 
				'000000', 
				'000000']
    pattern5 = ['000000',
				'000000',
				'00##00',
				'00##00',
				'000000',
				'000000',
				'000000']
    pattern6 = ['000000',
				'00##00', 
				'00##00', 
				'000#00',
				'000000', 
				'000000', 
				'000000']
    pattern7 = ['000000',
				'00##00', 
				'00#000', 
				'00#000',
				'000000', 
				'000000']
    pattern8 = ['000000',
				'000#00', 
				'000#00', 
				'00##00',
				'000000', 
				'000000']
    pattern9 = ['000000',
				'00#000', 
				'00##00', 
				'00##00', 
				'000000']
    pattern10 = ['000000',
				'000#00', 
				'000##0', 
				'000#00',
				'000000', 
				'000000']
    pattern11= ['000000',
				'00##00', 
				'00##00', 
				'00#000', 
				'000000',
				'000000']
    pattern12= ['000000',
				'000000', 
				'000#00', 
				'00##00',
				'000000', 
				'000000', 
				'000000']
    pattern13= ['000000',
				'000#00', 
				'00##00', 
				'00#000',
				'000000', 
				'000000', 
				'000000']
    pattern14 =['000000',
				'00#000', 
				'00##00', 
				'000#00',
				'000000', 
				'000000']
    pattern15= ['000000',
				'000000', 
				'000000', 
				'00##00',
				'000#00', 
				'000000',
				'000000']				
    pattern16 =['000000',
				'000#00', 
				'00##00', 
				'00##00', 
				'000000',
				'000000']
    pattern17 =['000000',
				'0000#0', 
				'0000#0', 
				'000##0',
				'000000', 
				'000000']
    pattern18 =['000000',
				'000000', 
				'000000', 
				'00##00',
				'00#000', 
				'000000', 
				'000000']
    pattern19 =['000000',
				'000000', 
				'000#00', 
				'00##00',
				'000#00', 
				'000000', 
				'000000']
    pattern20 =['000000',
				'000#00', 
				'000#00', 
				'000#00',
				'000000', 
				'000000', 
				'000000']				
    pattern21 =['000000',
				'00##00', 
				'000#00', 
				'00##00',
				'000000', 
				'000000']
    pattern22 =['000000',
				'00##00', 
				'00#000', 
				'00##00',
				'000000', 
				'000000']	
    pattern23 =['000000',
				'00##00', 
				'00#000', 
				'00#000',
				'000000', 
				'000000']
    pattern24 =['000000',
				'000000', 
				'000000', 
				'000000',
				'000##0', 
				'000000',
				'000000']
    pattern25 =['000000',
				'000000', 
				'00#000', 
				'00#000',
				'000000', 
				'000000', 
				'000000']
    pattern26 =['000000',
				'00#000', 
				'00##00',
				'000000',
				'000000',				
				'000000']
    pattern27 =['000000',
				'000#00', 
				'000#00', 
				'000000',
				'000000', 
				'000000', 
				'000000']
    pattern28 =['000000',
				'00#000', 
				'00#000', 
				'00#000',
				'000000', 
				'000000']
    pattern29 =['000000',
				'000000', 
				'000000', 
				'00##00',
				'000000', 
				'000000']  
    pattern30 =['000000',
				'000000', 
				'00#000', 
				'0##000',
				'000000', 
				'000000']   
    pattern31 =['000000',
				'000000', 
				'00#000', 
				'0##000',
				'00#000', 
				'000000']                 
    pattern32 = ['00000', '00000', '00000', '00000', '00000']

    # Pattern matching
    patterns = [pattern1 , pattern2 , pattern3 , pattern4 , pattern5 , pattern6 , 
	            pattern7 , pattern8 , pattern9 , pattern10, pattern11, pattern12, 
				pattern13, pattern14, pattern15, pattern16, pattern17, pattern18, 
				pattern19, pattern20, pattern21, pattern22, pattern23, pattern24,
                pattern25, pattern26, pattern27, pattern28, pattern29, pattern30]

    with open(output_path, "r") as file:
        content = file.read()

    lines = content.split('\n')

    # Variables to keep track of the matched pattern
    matched_pattern = None
    matched_i = None
    matched_j = None

    # Iterate through patterns
    for pattern_id, pattern in enumerate(patterns, start=1):
        for i in range(len(lines) - len(pattern) + 1):
            for j in range(len(lines[i]) - len(pattern[0]) + 1):
                match = True
                for k in range(len(pattern)):
                    if lines[i + k][j:j+len(pattern[0])] != pattern[k]:
                        match = False
                        break
                if match:
                    # Store the first matched pattern and break the loops
                    matched_pattern = pattern
                    matched_i = i
                    matched_j = j
                    break
            if match:
                break
        if match:
            break

    # Crop the image based on the first matched pattern
    if matched_pattern:
        x_start = matched_j * square_w
        y_start = matched_i * square_h
        x_end = (matched_j + len(matched_pattern[0])) * square_w
        y_end = (matched_i + len(matched_pattern)) * square_h

        # Crop the image
        cropped_image = bw_image[y_start:y_end, x_start:x_end]

        # Save the cropped image with the same filename
        cropped_image_path = os.path.join(output_folder, f'{os.path.splitext(os.path.basename(input_path))[0]}_cropped.jpg')
        cv2.imwrite(cropped_image_path, cropped_image)

# Function to process multiple images in parallel
def process_images_parallel(file_paths, output_folder):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_image, path, output_folder): path for path in file_paths}

        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                future.result()
              #  print(f"Processing complete for {path}")
            except Exception as e:
                print(f"Error processing {path}: {e}")

# Create a Tkinter root window (it won't be shown)
root = Tk()
root.withdraw()

# Ask the user to select individual image files
file_paths = filedialog.askopenfilenames(title="Select Image Files", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

# Check if files are selected
if file_paths:
    # Create an output folder
    output_folder = "output_folder"
    os.makedirs(output_folder, exist_ok=True)

    # Process images in parallel
    process_images_parallel(file_paths, output_folder)

    print("All processing complete. Output files are saved in the 'output_folder'.")
else:
    print("No files selected.")

#for file_name in os.listdir(output_folder):
#	if file_name.endswith("_output.txt"):
#		os.remove(file_path)	