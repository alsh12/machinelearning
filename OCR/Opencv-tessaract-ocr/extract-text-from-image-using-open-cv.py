import cv2
import pytesseract
import numpy as np

# 1. pytesseract cmd
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 2. load image
img = cv2.imread("./Images/sample-4.jpg")

# 3. pytesseract only accept RGB value, OpenCV images are in BGR so convert image to RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

rgb_planes = cv2.split(img)
result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((10, 10), np.uint8))        #change the value of (10,10) to see different results
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = cv2.normalize(diff_img, None, alpha=0, beta=250, norm_type=cv2.NORM_MINMAX,dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

result = cv2.merge(result_planes)
result_norm = cv2.merge(result_norm_planes)

dstFromMainImg = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 11)
dstFromNormalizedImg = cv2.fastNlMeansDenoisingColored(result_norm, None, 10, 10, 7, 11)

# cv2.imshow("Result" , result)
# cv2.imshow("Result Norm" , result_norm)
# cv2.waitKey(0)

# Get the all the texts from the images
# print(pytesseract.image_to_string(dstFromNormalizedImg))

# ### Detect the characters
# hImage,wImage,_ = img.shape
# config = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(dstFromNormalizedImg,config=config)
# for b in boxes.splitlines():
#     # print(b)
#     b = b.split(' ')
#     print(b)
#     #Get the x,y,width and height and convert the value string to int
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(dstFromNormalizedImg,(x,hImage-y),(w,hImage-h),(0,0,255),2)
#     cv2.putText(dstFromNormalizedImg,b[0],(x,hImage-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255,),1)


# ### Detect the words
# hImage,wImage,_ = img.shape
# config = r'--oem 3 --psm 1 outputbase words'
# boxes = pytesseract.image_to_data(dstFromNormalizedImg,config=config)
# # print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     if x!= 0:
#         b = b.split()
#         # print(b)
#         # print(len(b))
#         if len(b)==12:
#             print('printing length',len(b))
#             print(b)
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(dstFromNormalizedImg,(x,y),(w+x,h+y),(0,0,255),2)
#             cv2.putText(dstFromNormalizedImg,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255,),1)

### Detect the digits
aadharcardNo =0
dateOfBirth = 0
hImage,wImage,_ = img.shape
config = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(dstFromNormalizedImg,config=config)
# print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x!= 0:
        b = b.split()
        print(b)
        # print(len(b))
        if len(b)==12:
            print('printing length',len(b))
            if len(b[11])==4:
                dateOfBirth = b[11]
            if len(b[11])==8:
                dateOfBirth = b[11]
            if len(b[11]) == 12:
                aadharcardNo = b[11]
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(dstFromNormalizedImg,(x,y),(w+x,h+y),(0,0,255),2)
            cv2.putText(dstFromNormalizedImg,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255,),1)


print("DOB: ",dateOfBirth)
print("Aadhar Card No: ",aadharcardNo)
cv2.imshow("Result",dstFromNormalizedImg)
cv2.waitKey(0)

