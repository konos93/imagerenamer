import pytesseract
import tkinter as tk
from tkinter import filedialog
import time
from PIL import Image

# Set up Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set number of OCR iterations per image
num_iterations = 5

# Create Tkinter window for selecting image files
root = tk.Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames(title="Select Image Files", filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])

# Perform OCR on each selected image file multiple times and store the most likely result
ocr_results = []
start_time = time.time()
for file_path in file_paths:
    best_result = ""
    best_confidence = -1
    img = Image.open(file_path)
    for i in range(num_iterations):
        try:
            ocr_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT ,config='--psm 6 tessedit_char_whitelist=0123456789')
            for j in range(len(ocr_data["text"])):
                if ocr_data["text"][j] and int(ocr_data["conf"][j]) > best_confidence:
                    best_result = ocr_data["text"][j]
                    best_confidence = int(ocr_data["conf"][j])
        except pytesseract.TesseractError:
            continue
    file_name = file_path.split("/")[-1]
    ocr_results.append(f"{file_name}:\{best_result.zfill(4)}\n")

# Save OCR results to a single text file
file_name = "ocr_results.txt"
with open(file_name, "w", encoding="utf-8") as f:
    f.writelines(ocr_results)

end_time = time.time()
print(f"Program runtime: {end_time - start_time:.2f} seconds")
