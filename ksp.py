import shutil
import os
import pytesseract
from PIL import Image


# Source and destination folders


# Image file name (change it according to your file name)
def copy_file(source_folder,destination_folder,imgname):
    image_file_name = imgname

# Full path of source and destination images
    source_image_path = os.path.join(source_folder, image_file_name)
    destination_image_path = os.path.join(destination_folder, image_file_name)

    # Copy the image file
    shutil.copyfile(source_image_path, destination_image_path)
    #print("Image copied successfully!")
    
def read_text(filename):
    # Open the image file
    image_path = "static/img/"+filename
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

    

