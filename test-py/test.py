import cv2
import os
import pytesseract
import glob
import re
import sys
import subprocess
from io import StringIO
import linecache
from subprocess import Popen, PIPE

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
root_dir = r'C:\Users\ZF\Documents\python\test-py'


# .FILE FORMAT CHANGEABLE
for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
    pattern = r"\Digital Certificate\b" or r"\Sijil Digital\b"
    keyword = {'Digital','Certificate', 'Sijil','COVID-19', 'Vaccination', 'Vaksinasi' }
    #image = r'C:\Users\ZF\Pictures\Sabah Elite percipio - Copy.png'
    #image = r'C:\Users\ZF\Documents\python\test-py\6.png'
    textImg = pytesseract.image_to_string(filename)
    text = str(textImg.strip())
    queryword = text.split()
    substring = str(text.partition("Digital"))
    #print(substring.split("Digital", "Sijil", "Certificate"))
    
    resultword = [word for word in queryword if word.lower() not in keyword]
    result = ' '.join(resultword)
    ########################################################################
    filter1 = result.replace('Digital', '')
    filter2 = filter1.replace('Certificate', '')
    filter3 = filter2.replace('Vaccination', '')
    filter4 = filter3.replace('Sijil', '')
    filter5 = filter4.replace('COVID-19', '')
    filter6 = filter5.replace('COVID-1 9', '')
    filter7 = filter6.replace('wl 4G @ ) Profile —', '')
    filter7 = filter6.replace('Cerifcate', '')
    final = filter7.replace('Vaksinasi', '')
    ########################################################################
    #                        ADD FILTER WORDS DI SINI
    ########################################################################
    print(final)
    user = final[0:23]
    #print(user)
    numbers = []
    for word in final.split():
        if word.isdigit():
            numbers.append(int(word))
            
    #print(numbers)
    #if numbers is None:
    if not numbers:
        print(user)
        os.rename(filename, user + '.png')
    else:
        ic = str(numbers[0])       
        print(ic)
        os.rename(filename, ic + '.png')

    #print(substring[55:70])
    #sys.stdout = open(root_dir + '_output_tested.txt', 'a+')
    #keyword = 'Digital Certificate'
    #stripped = text.split(keyword)
    #print(stripped) 
    #before_keyword, keyword, after_keyword = mystring.partition(pattern)
    #user = re.search('(?<=Digital Certificate)(\w+)',text)
    #name = user.group()
    #name = re.findall(pattern, text)
    #username = text.split("Digital Certificate", 1)
    #user = re.match()
    #for element in keyword:
    #while 'Digital Certificate' not in text.readline():
    #    continue
    #print(f.readline())
    #name = text.split("Digital Certificate",3)[1]
    #print(user)
    #iterator = iter(lines.splitlines())
    #content = textImg.readlines()
    #print(text[0:3])
    #print(text[39:65])
    #print(linecache.getline('test-py_outputs.txt',4))
    
    
    #proc=subprocess.Popen('Echo to stdout', shell=True, stdout=subprocess.PIPE, )
    #output = proc.communicate()
    #print(output)
    #f = open(root_dir + '_outputed.txt', 'a+')
    #sys.stdout = f
    #f.close()
    

#os.rename(image,)

    #orig_stdout = sys.stdout
    #f = open('outpur.txt', 'w')
    #sys.stdout = f

    #for i in range(2):
    #    print('i= ', i)

    #sys.stdout = orig_stdout
    #f.close()

#file = open('output.txt', 'rt')
#contents = file.read() 
#print(contents)
