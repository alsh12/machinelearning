import re
import AadharCardV2 as ac

def ReadDataAadhar(text):

    aadharData = ac.AadharData()

    print(aadharData.InfoExtracter('./SampleImage/sample-9.jpg'))





