# imagerenamer

this is a project on progress


this is for diybookscanner community

This Python script uses the Tesseract OCR engine to perform OCR on multiple cropped image files. The script utilizes the pytesseract library to interact with the Tesseract OCR engine, and the tkinter library to create a GUI window for selecting image files.
Prerequisites

    Python 3.x
    Tesseract OCR engine installed on your system
    Python libraries: pytesseract, tkinter, Pillow (PIL)

How to use

    Install the Tesseract OCR engine on your system. The script assumes that Tesseract is installed in C:\Program Files\Tesseract-OCR\tesseract.exe, but you can modify the tesseract_cmd variable in the script to match the installation path on your system.

    Install the required Python libraries. You can use pip to install them:

    python

pip install pytesseract tkinter Pillow

Clone or download the script to your local machine.

Open a command prompt or terminal window and navigate to the directory where the script is saved.

Run the script:

python

    python ocr_script.py

    A GUI window will appear allowing you to select one or more image files to process.

    After selecting the images, the script will perform OCR on each image multiple times (as specified by the num_iterations variable) and store the most likely result. The results are saved to a text file called ocr_results.txt in the same directory as the script.

    The script will print the total runtime to the console.

Notes

    The script is set up to process .jpg, .png, and .bmp image files. You can modify the filetypes in the filetypes variable as needed.

    The OCR engine is configured to recognize only digits (0-9) in the images. You can modify the config parameter in the image_to_data function to change the OCR settings.

    The OCR results are saved to a text file with each line formatted as follows: filename:ocr_result.

    The script is designed to handle errors gracefully. If the OCR engine encounters an error while processing an image, the script will simply skip that image and move on to the next one.

License

This script is released under the MIT License. Feel free to modify and use it however you like.
