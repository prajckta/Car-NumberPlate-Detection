import cv2
import pytesseract
import re

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def extract_text(image):
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#     text = pytesseract.image_to_string(thresh, config='--psm 6')
#     return text.strip()


def extract_text(image):
    # Use pytesseract to extract text from the image
    custom_config = r'--oem 3 --psm 6'
    extracted_text = pytesseract.image_to_string(image, config=custom_config)
    
    # Define a regular expression pattern to match only letters and digits
    pattern = r'[a-zA-Z0-9]+'
    
    # Use regex to find all matches of the pattern in the extracted text
    matches = re.findall(pattern, extracted_text)
    
    # Join the matches into a single string
    cleaned_text = ''.join(matches)
    
    return cleaned_text

# License plate format: 2 letters, 2 digits, 2 letters, 4 digits
def detect_license_plate(text, image, filename):
    pattern = r'^[A-Z]{2}\s*\d{2}\s*[A-Z]{2}\s*\d{4}$'
      
    if re.match(pattern, text):
        print("License plate detected:", text)
        # Additional processing or actions can be performed here if the format matches
        # For example, you can save the image or perform further analysis
        cv2.imwrite(filename, image)
        print("Image saved:", filename)
    # else:
    #     print("License plate format not detected.")

