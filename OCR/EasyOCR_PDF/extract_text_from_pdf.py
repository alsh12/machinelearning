from pdf2image import convert_from_path
import easyocr
import numpy as np
import PIL
from PIL import ImageDraw
import spacy
import os
import cv2

reader = easyocr.Reader(['en'])

images = convert_from_path('./SamplePDF/w2 2014 form.pdf',poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin')

from IPython.display import display, Image
print("Display image text")
print(display(images[0]))

bounds = reader.readtext(np.array(images[0]))
print('Bounding box')
print(bounds)

def drawBoxes(image,bounds,color='green',width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0,p1,p2,p3 = bound[0]
        draw.line([*p0,*p1,*p2,*p3,*p0],fill=color,width=width)
    return image

im = drawBoxes(images[0],bounds)
print(bounds[1][1])
ImageDraw.getdraw()
img = cv2.imread('./Images/w2 2015.png')
cv2.startWindowThread()
cv2.namedWindow("preview")
cv2.imshow("preview", img)

cv2.waitKey(0)



print('Done')
