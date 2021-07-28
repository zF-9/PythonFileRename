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
import os.path
from os import path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
root_dir = r'C:\Users\ZF\Documents\python\test-py'

file_format = ".png" #change format globally , eg: .png/.jpeg/.jpg


# .FILE FORMAT CHANGEABLE
for filename in glob.iglob(root_dir + '**/*' + file_format, recursive=True):
    pattern = r"\Digital Certificate\b" or r"\Sijil Digital\b"
    keyword = {'Digital','Certificate', 'Sijil','COVID-19', 'Vaccination', 'Vaksinasi' }
    #image = r'C:\Users\ZF\Pictures\Sabah Elite percipio - Copy.png' - test image
    #image = r'C:\Users\ZF\Documents\python\test-py\6.png' - test image
    textImg = pytesseract.image_to_string(filename)
    text = str(textImg.strip())
    queryword = text.split()
    substring = str(text.partition("Digital"))
    #print(substring.split("Digital", "Sijil", "Certificate"))
    
    resultword = [word for word in queryword if word.lower() not in keyword]
    result = ' '.join(resultword)
    
    ########################################################################
    #                        ADD FILTER WORDS DI SINI
    ########################################################################    
    filter1 = result.replace('Digital', '')
    filter2 = filter1.replace('Certificate', '')
    filter3 = filter2.replace('Vaccination', '')
    filter4 = filter3.replace('Sijil', '')
    filter5 = filter4.replace('COVID-19', '')
    filter6 = filter5.replace('COVID-1 9', '')
    filter7 = filter6.replace('wl 4G @ ) Profile —', '')
    filter8 = filter7.replace('Cerifcate', '')
    filter9 = filter8.replace('wl 4G @ ) Profile —', '')
    final = filter9.replace('Vaksinasi', '')
    ########################################################################
    #                        ADD FILTER WORDS DI SINI
    ########################################################################
    
    print(final)
    user = final[0:28]
    #print(user)
    numbers = []
    for word in final.split():
        if word.isdigit():
            numbers.append(int(word))
            
    #print(numbers)
    #if numbers is None:
    if not numbers:
        file_name = root_dir + '\\' + user + '.png'
        new_name = user + '.png'
        #print(new_name)
        if path.isfile(new_name):
            #print("ada duplicate nama")
            #print("delete lama - save yang baru")
            print(filename)
            print(user)

            if file_name == filename:
                print("ini file sama; delete yang latter") # do nothing
                #os.rename(filename, 'duplicate-' + new_name)
            else:
                print("ini diffrent file")
                os.rename(filename, 'duplicate-' + new_name)
                os.remove('duplicate-' + new_name)
                #os.remove(filename)
            #file_to_rem = pathlib.Path(new_name)
            #file_to_rem.unlink()
            #os.remove(new_name)
            #os.rename(filename, 'duplicate' + new_name )
        else:
            print("ok rename la nama dia")
            #os.remove() 
            os.rename(filename, new_name)
    else:
        ic = str(numbers[0])
        file_ic = root_dir + '\\' + ic  + '.png'
        new_ic = ic + '.png'
        #print(new_ic)
        if path.isfile(new_ic):
            print(filename)
            print(file_ic)

            if file_ic == filename:
                print("ini file sama; delete yang latter") #do nothing
                #os.rename(filename, 'duplicate-' + new_ic)
            else:
                print("ini diffrent file")
                os.rename(filename, 'duplicate-' + new_ic)
                os.remove('duplicate-' + new_ic)
                #os.remove(filename)
            #print("ada duplicate IC")
            #print("delete file yang kena tengok")
            #os.remove(filename)
            #file_to_rem = pathlib.Path(new_name)
            #file_to_rem.unlink()
            #os.remove(new_name)
            #os.rename(filename, 'duplicate' + new_ic )
        else:
            print("ok rename la ic dia")
            os.rename(filename, new_ic)

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
