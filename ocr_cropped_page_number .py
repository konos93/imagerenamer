from tkinter import filedialog
from tkinter import Tk
from PIL import Image
import pytesseract
import concurrent.futures
import os


# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_numbers(image_path, angle):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Rotate the entire image without cropping
    rotated_image = image.rotate(angle, expand=True)

    # Get the dimensions of the rotated image
    width, height = rotated_image.size

    # Use pytesseract to recognize all text in the rotated image
    all_text = pytesseract.image_to_string(rotated_image, config='--psm 6')

    # Filter and extract numbers between 10 and 999 from the rotated image
    recognized_numbers = [f"{int(word):04d}" for word in all_text.split() if word.isdigit() and 10 <= int(word) <= 1299]

    return recognized_numbers, angle


def recognize_numbers_concurrent(image_path):
    # Get the filename from the path
    filename = os.path.basename(image_path)

    # Initialize lists to store recognized numbers and corresponding angles
    all_recognized_numbers = []
    all_angles = []

    # Use concurrent.futures.ThreadPoolExecutor for concurrent execution
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Rotate the image from angle -5 to angle +5 in steps of 1 degrees
        angles = range(-5, 5, 1)

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

    # Filter recognized numbers based on the absolute value of the filename with a tolerance of ±10
    abs_filename = abs(int(filename.split('.')[0]))
    min_value = abs_filename - 50
    max_value = abs_filename + 50
    filtered_numbers = [num for num in all_recognized_numbers if min_value <= int(num) <= max_value]

    return filename, filtered_numbers, all_angles

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

def write_to_file(output_filename, results):
    with open(output_filename, 'w') as file:
        for filename, numbers, angles in results:
            file.write(f"Filename: {filename}, Filtered Recognized Numbers between 10 and 1299: {numbers}\n")
            # Uncomment the line below if you want to include all angles for each recognition attempt
            # file.write("All Angles for Recognition Attempts: {}\n".format(angles))
            #file.write("\n")

# Let the user choose multiple image files
image_paths = choose_images()

# Store results for each image in a list
all_results = []

for image_path in image_paths:
    result_filename, result_numbers, result_angles = recognize_numbers_concurrent(image_path)
    all_results.append((result_filename, result_numbers, result_angles))

    # Print the final result and corresponding angles
    print(f"Filename: {result_filename}, Filtered Recognized Numbers between 10 and 1299: {result_numbers}")

# Write the results to the input.txt file
write_to_file('input.txt', all_results)

