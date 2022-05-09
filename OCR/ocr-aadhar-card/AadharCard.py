import re
import AadharCardV2 as ac

def ReadDataAadhar(text):

    aadharData = ac.AadharData()
    print("Aadhar Card No : ",aadharData.FindAadharNumber(text))
    print("Name of Aadhar : ",aadharData.FindName(text))
    print("Gender : ", aadharData.FindGender(text))
    print("DOB/Year of Birth : ", aadharData.FindDateOfBirth(text))

    #
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # print("@@@@@ Do Not Consider Below Data @@@@@@@@@@@@@@@@@@@@")
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # for i, wordlist in enumerate(lines):
    #     # print("Index:",i,", Word: ",wordlist)
    #     # print(wordlist)
    #     wordsplit = wordlist.split()
    #     aadharData = ac.AadharData()
    #     # print(aadharData.FindAadharNumber(lines))
    #
    #     if[w for w in wordsplit if re.search('(Year|Birth|irth|YoB|YoB:|DOB|DOB:|Dos)$',w)]:
    #         dobLine = wordlist
    #         line_list.append(wordlist)
    #         # print("Current word index: ", lines.index(wordlist))
    #         # previousIndex = (lines.index(wordlist) -1)
    #         # currenntIndex = lines.index(wordlist)
    #         # print("Previous word:",lines[55:57])
    #         # print("Index of the line", index)
    #         # index_list.append(index)
    #         print("DOB line found: ",dobLine)
    #
    #     elif [w for w in wordsplit if re.search(genderSearchStr,w.lower())]:
    #         print(wordlist)
    #         genderLine = wordlist
    #         print("Gender Line found:",genderLine)
    #
    #     elif re.search(aadharNoStr, wordlist):
    #         # print(wordlist)
    #         aadharLine = wordlist
    #         print("Aadhar Line: ", aadharLine)
    #     else:
    #         text1.append(wordlist)
    #
    # # print required values DOB/YOB, Gender, Name a below
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
    # print("printing required values DOB/YOB, Gender, Name a below ")
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
    # # for DOB
    # try:
    #     dob = str(re.findall(r"[\d]{1,4}[/-][\d]{1,4}[/-][\d]{1,4}|.*([1-3][0-9]{3})", dobLine)).replace("]", "").replace("[", "").replace("'", "")
    #     print("DOB/Year of Birth: ",dob)
    # except Exception as e:
    #     print('Caught exception' ,e)
    #     pass
    #
    # # Gender
    # try:
    #     if len(genderLine)>0:
    #         sex = str(re.findall(genderSearchStr, genderLine.lower())).replace("[","").replace("'", "").replace("]", "")
    #         print("Gender: ",sex)
    #     else:
    #         print("Gender not found")
    #
    # except Exception as e:
    #     print('Caught exception: ', e)
    #     pass
    #
    # try:
    #     if(len(aadharLine)) > 0:
    #         adhaarNo = str(re.findall(aadharNoStr, aadharLine)).replace("[","").replace("'", "").replace("]", "")
    #         print("Aadhar No: ", adhaarNo)
    # except:
    #     pass
    # try:
    #     # Find names
    #     name = text0[0]
    #     print("Name: ",name)
    # except:
    #     pass
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    # # print(text)
    # # print("================")
    # # print(text1)
    # # print("============")
    # # print("Check difference")
    # # text1 = list(filter(None,text1))
    # # print(text1)
    # # print("============")
    # # print("Check difference")




