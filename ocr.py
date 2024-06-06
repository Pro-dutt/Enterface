import pytesseract
from urllib.parse import urlparse
import cv2
import global_file as gb
import numpy as np
import re

def domain_name(url):
    url = (url.replace('https://',"").
           replace('www.',"").replace('.com',''))
    parsed_url = urlparse('//' + url)
    website_name = parsed_url.netloc.split('/')[0]
    website_name = re.sub(r'[^a-zA-Z0-9\-]', ' ', website_name)
    
    gb.Url = website_name

def ocr(img_file):
    # Convert the PIL image to a NumPy array
    img_array = np.array(img_file)
    if img_array.shape[2] == 3:
        pass
    elif img_array.shape[2] == 4:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2BGR)
    else:
        raise ValueError("Unsupported image format")
    
    grey = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    ocr_result = pytesseract.image_to_string(grey)
    domain_name(ocr_result)


