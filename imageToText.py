# importing the libraries
import pytesseract
from PIL import Image
import pyttsx3
from googletrans import Translator

# open image
img = Image.open(r'C:\Users\user\PycharmProjects\imageToText\images\test.png')

# prints image format
print(img)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

result = pytesseract.image_to_string(img)

result = result.replace("\n", " ")

print(result)

# audio of image text

engine = pyttsx3.init()

# setting the voice to female voice 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say(result)
engine.runAndWait()
