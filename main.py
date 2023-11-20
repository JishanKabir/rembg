from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def remove_bg(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()  # Open file dialog
    if file_path:
        output_path = 'output.png'  # Output path for the processed image
        remove_bg(file_path, output_path)
        print("Background removed. Output saved as 'output.png'")

if __name__ == "__main__":
    select_image()
