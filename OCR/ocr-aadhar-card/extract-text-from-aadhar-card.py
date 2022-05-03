import cv2
import numpy as np
import pytesseract
import re
#import spacy


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img3 = cv2.imread('./SampleImage/sample-3.jpg')   #any picture
print(img3.shape)

rgb_planes = cv2.split(img3)
result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((10, 10), np.uint8))        #change the value of (10,10) to see different results
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = cv2.normalize(diff_img, None, alpha=0, beta=250, norm_type=cv2.NORM_MINMAX,
                                                 dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

result = cv2.merge(result_planes)
result_norm = cv2.merge(result_norm_planes)
dst = cv2.fastNlMeansDenoisingColored(result_norm, None, 10, 10, 7, 11)             # removing noise from image

text = pytesseract.image_to_string(dst).upper()
0
print("Full Text")
print('=====')
print(text)
print('=====')

#Option 1. Get the date , number and sex details using regex function
date = str(re.findall(r"[\d]{1,4}[/-][\d]{1,4}[/-][\d]{1,4}", text)).replace("]", "").replace("[","").replace("'", "")
print(date)
number = str(re.findall(r"[0-9]{11,12}", text)).replace("]", "").replace("[","").replace("'", "")
print(number)
sex = str(re.findall(r"MALE|FEMALE", text)).replace("[","").replace("'", "").replace("]", "")
print(sex)


#Option 2: Get the detail based on NLP
# nlp = spacy.load("en_core_web_sm")
#
# doc = nlp(text)
#
# from spacy import displacy
# print(displacy.render(nlp(doc.text),style='ent',jupyter=True))




