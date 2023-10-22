import pytesseract
from PIL import Image

# Path to the Tesseract executable (change this to the path on your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Replace 'image.png' with the path to your image file
image_path = 'path/to/your/image.png'

# Load the image from the specified path
img = Image.open(image_path)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)
