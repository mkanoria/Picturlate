#Module to detect object in image and return suggestions for what is there in the image
#Returns answers to the translate function

import io
import os
from translate import translate_word
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources/wakeupcat.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

# print(labels[0].description + " " + labels[1].description)
# language = input("Enter the language to translate in: ")
# translate_word(labels[0].description, language)
