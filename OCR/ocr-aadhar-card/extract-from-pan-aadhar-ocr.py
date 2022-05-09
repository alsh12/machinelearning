from pan_aadhar_ocr import Pan_Info_Extractor
from pan_aadhar_ocr import Aadhar_Info_Extractor

extractor = Aadhar_Info_Extractor()
extractor.info_extractor('./SampleImage/sample-9-front.jpg','./SampleImage/sample-9-back.jpg')


