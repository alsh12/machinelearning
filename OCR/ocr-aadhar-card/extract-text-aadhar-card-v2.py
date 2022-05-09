# import required libraries
import pytesseract
import numpy
import cv2
import ftfy
import AadharCard
import AadharCardV2 as aadharCard


aadhar = aadharCard.AadharData()
print(aadhar.InfoExtracter('./SampleImage/sample-9-front.jpg','./SampleImage/sample-9-back.jpg'))
#
# # extract image and convert to grayscale for better readability
#
#
# img = cv2.imread('./SampleImage/sample-9.jpg')
# img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
#
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # cv2.imshow('Resize Image', img)
# # cv2.waitKey(0)
#
# # validate image blur or not
# # var = cv2.Laplacian(img,cv2.CV_64F).var()
# #print(var)
#
# # if var < 50:
# #     print('Image is too blurry...')
# #     exit(input('Enter any key to exit...'))
#
#
# # pytesseract cmd
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# # read the text from image
# text = pytesseract.image_to_string(img,lang='eng')
#
# # write the data in output text file
# text_output = open('output.txt','w',encoding='utf-8')
# text_output.write(text)
# text_output.close()
#
# # fix the text
# text = ftfy.fix_text(text)
# text = ftfy.fix_encoding(text)
# # print(text)
# print("Original Text end here...")
# print(AadharCard.ReadDataAadhar(text))