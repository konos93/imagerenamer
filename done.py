from tkinter import filedialog
from tkinter import Tk
from PIL import Image, ImageOps
import pytesseract
import concurrent.futures
import os
import sys

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_numbers(image_path, angle):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Rotate the entire image without cropping
    rotated_image = image.rotate(angle, expand=True)

    # Get the dimensions of the rotated image
    width, height = rotated_image.size

    # Crop the top half of the rotated image
    top_half = rotated_image.crop((0, 0, width, height // 4))
    

    # Display the rotated and cropped image before OCR
    #rotated_image.show()
    # top_half.show()    

    # Use pytesseract to recognize all text in the top half
    all_text = pytesseract.image_to_string(top_half, config='--psm 6')

    # Filter and extract numbers between 10 and 999 from the top half
    recognized_numbers = [f"{int(word):04d}" for word in all_text.split() if word.isdigit() and 10 <= int(word) <= 999]

    return recognized_numbers, angle

def recognize_numbers_concurrent(image_path):
    # Get the filename from the path
    filename = os.path.basename(image_path)

    # Initialize lists to store recognized numbers and corresponding angles
    all_recognized_numbers = []
    all_angles = []

    # Use concurrent.futures.ThreadPoolExecutor for concurrent execution
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Rotate the image from angle -30 to angle +30 in steps of 5 degrees
        angles = range(-30, 31, 1)
        
        # Adjust angles based on the filename
        if int(filename.split('.')[0]) % 2 == 0:
            angles = [angle + 90 for angle in angles]
        else:
            angles = [angle - 90 for angle in angles]
        
        # Map the recognize_numbers function to each adjusted angle
        results = list(executor.map(lambda angle: recognize_numbers(image_path, angle), angles))

    # Extract the recognized numbers and angles from the results
    for result, angle in results:
        all_recognized_numbers.extend(result)
        all_angles.append(angle)
        
        # Print the results for the current angle
       # print(f"\nAngle: {angle}")
       # print("Recognized Numbers between 10 and 999:", result)

    return filename, all_recognized_numbers, all_angles

def choose_images():
    # Create the Tkinter root window (it won't be shown)
    root = Tk()
    root.withdraw()  # Hide the main window

    # Open a file dialog to choose multiple image files
    file_paths = filedialog.askopenfilenames(
        title="Choose Image Files",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")],
    )

    return file_paths

# Let the user choose multiple image files
image_paths = choose_images()

# Redirect output to a file
with open("output.txt", "w") as f:
    sys.stdout = f  # Change the standard output to the file

    # Process each selected image
    for image_path in image_paths:
        result_filename, result_numbers, result_angles = recognize_numbers_concurrent(image_path)

        # Print the final result and corresponding angles
        print(f"\nFilename: {result_filename}","Overall Recognized Numbers between 10 and 999:", result_numbers) 
       # print("Overall Recognized Numbers between 10 and 999:", result_numbers)
       # print("All Angles for Recognition Attempts:", result_angles)
        #print("--------------------------------------------------------------------")

    sys.stdout = sys.__stdout__  # Reset standard output to the console
