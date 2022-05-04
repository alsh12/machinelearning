import re

def ReadDataAadhar(text):
    res = text.split()
    name = None
    dob = None
    adhaarNo = None
    sex = str(re.findall(r"male|female", text.lower())).replace("[","").replace("'", "").replace("]", "")
    print("Sex: ",sex)
    dob = str(re.findall(r"[\d]{1,4}[/-][\d]{1,4}[/-][\d]{1,4}", text)).replace("]", "").replace("[", "").replace("'","")
    print("Date of Birth: ",dob)
    nameLine = []
    dobLine = []
    text0 =[]
    text1 =[]
    text2 =[]
    lines = text.split('\n')
    genderSearchStr = '(Female|Male|female|male|FEMALE|MALE)$'
    for wordlist in lines:
        # print(wordlist)
        wordsplit = wordlist.split()
        if[w for w in wordsplit if re.search('(Year|Birth|irth|YoB|YoB:|DOB|DOB:|Dos)$',w)]:
            dobLine = wordlist
            print("DOB line found: ",dobLine)

        elif [w for w in wordsplit if re.search(genderSearchStr,w.lower())]:
            print(wordlist)
            genderLine = wordlist
            print("Gender Line found:",genderLine)

        else:
            text1.append(wordlist)

    # for DOB
    try:
        dob = str(re.findall(r"[\d]{1,4}[/-][\d]{1,4}[/-][\d]{1,4}", dobLine)).replace("]", "").replace("[", "").replace("'", "")
        print("`DOB/Year of Birth`: ",dob)
    except Exception as e:
        print('Caught exception' ,e)
        pass

    # Gender
    try:
        sex = str(re.findall(r"male|female", genderLine.lower())).replace("[","").replace("'", "").replace("]", "")
        print("Gender: ",sex)

    except Exception as e:
        print('Caught exception: ', e)
        pass

    try:
        # Find names
        name = text0[0]
        print("Name: ",name)
    except:
        pass
    # print(text)
    # print("================")
    # print(text1)
    # print("============")
    # print("Check difference")
    # text1 = list(filter(None,text1))
    # print(text1)
    # print("============")
    # print("Check difference")




