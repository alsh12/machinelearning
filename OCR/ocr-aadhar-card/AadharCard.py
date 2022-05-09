import re

def ReadDataAadhar(text):
    res = text.split()
    name = None
    dob = None
    adhaarNo = None
    # sex = str(re.findall(r"male|female", text.lower())).replace("[","").replace("'", "").replace("]", "")
    # print("Sex: ",sex)
    # dob = str(re.findall(r"[\d]{1,4}[/-][\d]{1,4}[/-][\d]{1,4}", text)).replace("]", "").replace("[", "").replace("'","")
    # print("Date of Birth: ", dob)
    # aadhar = str(re.findall(r"^\d{4}\s\d{4}\s\d{4}$", '3977 8800 0234')).replace("]", "").replace("[", "").replace("'","")
    # print("Aadhar: ",aadhar)
    nameLine = []
    dobLine = []
    aadharLine = []
    genderLine =[]
    text0 =[]
    text1 =[]
    text2 =[]
    lines = text.split('\n')
    line_list =[]
    index_list = []
    genderSearchStr = '(Female|Male|female|male|FEMALE|MALE)$'
    aadharNoStr = '^\d{4}\s\d{4}\s\d{4}$'
    print(type(lines))
    for i, wordlist in enumerate(lines):
        # print("Index:",i,", Word: ",wordlist)
        # print(wordlist)
        wordsplit = wordlist.split()

        if[w for w in wordsplit if re.search('(Year|Birth|irth|YoB|YoB:|DOB|DOB:|Dos)$',w)]:
            dobLine = wordlist
            line_list.append(wordlist)
            # print("Current word index: ", lines.index(wordlist))
            # previousIndex = (lines.index(wordlist) -1)
            # currenntIndex = lines.index(wordlist)
            # print("Previous word:",lines[55:57])
            # print("Index of the line", index)
            # index_list.append(index)
            print("DOB line found: ",dobLine)

        elif [w for w in wordsplit if re.search(genderSearchStr,w.lower())]:
            print(wordlist)
            genderLine = wordlist
            print("Gender Line found:",genderLine)

        elif re.search(aadharNoStr, wordlist):
            print(wordlist)
            aadharLine = wordlist
            print("Aadhar Line: ", aadharLine)
        else:
            text1.append(wordlist)

    # print required values DOB/YOB, Gender, Name a below
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
    print("printing required values DOB/YOB, Gender, Name a below ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
    # for DOB
    try:
        dob = str(re.findall(r"[\d]{1,4}[/-][\d]{1,4}[/-][\d]{1,4}|.*([1-3][0-9]{3})", dobLine)).replace("]", "").replace("[", "").replace("'", "")
        print("DOB/Year of Birth: ",dob)
    except Exception as e:
        print('Caught exception' ,e)
        pass

    # Gender
    try:
        if len(genderLine)>0:
            sex = str(re.findall(r"male|female", genderLine.lower())).replace("[","").replace("'", "").replace("]", "")
            print("Gender: ",sex)
        else:
            print("Gender not found")

    except Exception as e:
        print('Caught exception: ', e)
        pass

    try:
        # Find names
        name = text0[0]
        print("Name: ",name)
    except:
        pass
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    # print(text)
    # print("================")
    # print(text1)
    # print("============")
    # print("Check difference")
    # text1 = list(filter(None,text1))
    # print(text1)
    # print("============")
    # print("Check difference")




