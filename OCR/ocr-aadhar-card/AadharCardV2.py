import re
import pytesseract
import cv2
import json
import ftfy

class AadharData:
    def __init__(self):
        self.extractedData = {}

    def FindAadharNumber(self, inputText):
        """
        This function is used to find the aadhar number

        Args:
            inputText: provide text from extracted ocr data

        Returns:
            str: 12 digit aadhar number
        """
        try:
            aadharNumberPattern = '[0-9]{4}\s[0-9]{4}\s[0-9]{4}'
            match = re.search(aadharNumberPattern, inputText)
            if match:
                return match.group()
        except Exception as e:
            print("There is exception to find aadhar card number: ", e)
            pass

    def FindName(self,inputText):
        try:
            aadharNamePattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\s[A-Z][a-z]+$'
            splittedText = inputText.split('\n')

            for ele in splittedText:
                if not "Aadmi Ka Adhikaar" in ele:
                    match = re.search(aadharNamePattern, ele)
                    if match:
                        return match.group()
        except Exception as e:
            print("There is exception in finding name for aadhar: ",e)
            pass

    def FindDateOfBirth(self,inputText):
        try:
            dobOrYOBPattern = '(Year|Birth|birth|YoB|YoB:|DOB|DOB:|Dos)$'
            dateOfBirthPattern = '[\d]{1,4}[/-][\d]{1,4}[/-][\d]{1,4}|.*([1-3][0-9]{3})'
            splittedText = inputText.split('\n')
            for wordList in splittedText:
                wordsplit = wordList.split()
                if [w for w in wordsplit if re.search(dobOrYOBPattern, w)]:
                    match = re.findall(dateOfBirthPattern,wordList)
                    if len(match) >0:
                        return match[0]
        except Exception as e:
            print("There is exception in finding DOB: ",e)
            pass

    def FindGender(self,inputText):
        try:
            genderSearchPattern = r'(Female|Male|female|male|FEMALE|MALE)$'
            splittedText = inputText.split('\n')

            for ele in splittedText:
                match = re.search(genderSearchPattern, ele)
                if match:
                    return match.group()

        except Exception as e:
            print("There is exception to finding Gender:",e)
            pass

    def FindAddress(self,inputText):
        try:
            pass
        except Exception as e:
            # print("Working for Address")
            print("There is exception to finding Address:", e)

    def InfoExtracter(self,frontPageImage,backPageImage = None):
        """To extract information from the aadhaar card front and back image

                Args:
                frontPageImage(ImagePath): Provide front Page Image for the aadhar card,
                backPageImage(ImagePath): Provide back Page Image for the aadhar card

                Returns:
                json: Data extracted from Aadhar Card
        """
        # pytesseract cmd
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        self.fimage = frontPageImage
        self.bimage = backPageImage

        self.frontPageText = ''
        self.backPageText = ''

        self.Name = ''
        self.Gender = ''
        self.DoBOrYoB = ''
        self.AadharNo = ''
        self.Address = ''

        # front image
        if(self.fimage != None):
            frontPageImageToExtract = cv2.imread(self.fimage)
            frontPageImageToExtract = cv2.resize(frontPageImageToExtract, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            frontPageImageToExtract = cv2.cvtColor(frontPageImageToExtract, cv2.COLOR_BGR2GRAY)

            # #Check image blur or not
            # var = cv2.Laplacian(frontPageImageToExtract, cv2.CV_64F).var()
            # print("Front image laplacian:",var)
            # if(var < 40):
            #     return "Image is too blury. Provide another front image."

            # cv2.imshow("Front Page: ",frontPageImageToExtract)
            # cv2.waitKey(0)
            frontPageText = pytesseract.image_to_string(frontPageImageToExtract,config=f'-l eng --psm 6 --oem 3 ')
            # print("Front page :",frontPageText)

            # write the data in output text file
            frontPageOutput = open('FrontPageOutput.txt', 'w', encoding='utf-8')
            frontPageOutput.write(frontPageText)
            frontPageOutput.close()

        self.AadharNo = self.FindAadharNumber(frontPageText)
        self.Name = self.FindName(frontPageText)
        self.DoBOrYoB = self.FindDateOfBirth(frontPageText)
        self.Gender = self.FindGender(frontPageText)

        # Back image
        if(self.bimage != None):

            backPageImageToExtract = cv2.imread(self.bimage)
            backPageImageToExtract = cv2.resize(backPageImageToExtract, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            backPageImageToExtract = cv2.cvtColor(backPageImageToExtract, cv2.COLOR_BGR2GRAY)

            # Check image blur or not
            var = cv2.Laplacian(backPageImageToExtract, cv2.CV_64F).var()
            print(var)
            if (var < 40):
                return "Image is too blurry. Provide another front image."

            global backPageText
            backPageText = pytesseract.image_to_string(backPageImageToExtract,config=f'-l eng --psm 6 --oem 3 ')
            # print("Back Page TExt: ",backPageText)
            backPageText = ftfy.fix_text(backPageText)
            backPageText = ftfy.fix_encoding(backPageText)

            # write the data in output text file
            backPageOutput = open('BackPageOutput.txt', 'w', encoding='utf-8')
            backPageOutput.write(backPageText)
            backPageOutput.close()

            self.Address = self.FindAddress(backPageText)

        self.extractedData ={
            'Aadhar_number': self.AadharNo,
            'Name': self.Name,
            'Gender': self.Gender,
            'DOB/Year of Birth': self.DoBOrYoB,
            'Address': self.Address
        }

        return json.dumps(self.extractedData)

