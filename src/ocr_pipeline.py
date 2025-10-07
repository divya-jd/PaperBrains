import pytesseract
import cv2
from pdf2image import convert_from_path
import os

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        temp_path = "temp_page.jpg"
        page.save(temp_path, "JPEG")
        text += extract_text_from_image(temp_path)
        os.remove(temp_path)
    return text
