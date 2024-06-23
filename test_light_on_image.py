import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import exifread

def get_exif_data(image_path):
    with open(image_path, 'rb') as image_file:
        tags = exifread.process_file(image_file)
        exposure_time = tags.get('EXIF ExposureTime', 'N/A')
        iso_speed = tags.get('EXIF ISOSpeedRatings', 'N/A')
    return exposure_time, iso_speed

def select_images():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("JPEG files", "*.jpg;*.jpeg")],
    )
    return list(file_paths)

def main():
    image_data = []

    file_paths = select_images()
    for image_path in file_paths:
        filename = os.path.basename(image_path)
        exposure_time, iso_speed = get_exif_data(image_path)
        image_data.append((filename, exposure_time, iso_speed))
    
    return image_data

# Example usage
image_details = main()

# Print the results
for image_name, exposure_time, iso_speed in image_details:
    print(f'{image_name} - Exposure Time: {exposure_time} - ISO Speed: {iso_speed}')
