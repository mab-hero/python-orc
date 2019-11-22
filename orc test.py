from PIL import Image
import pytesseract

im = Image.open(r'C:\Users\MAB-ksa\Desktop\pytesseract-0.2.7\test.png')

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)

