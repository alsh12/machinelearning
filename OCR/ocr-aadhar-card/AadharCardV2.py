import re
import pytesseract
import cv2


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
            print("Working for Address")
        except Exception as e:
            print("There is exception to finding Address:", e)

    def InfoExtracter(self,frontPageImage,backPageImage):

        # pytesseract cmd
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # front image
        frontPageImageToExtract = cv2.imread(self.frontPageImage)
        # OCR_text = self.reader.readtext(img, detail=0,width_ths=0.9)
        frontPageText = pytesseract.image_to_string(frontPageImageToExtract)
        return "Work in Progress...."

