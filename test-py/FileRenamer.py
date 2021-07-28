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
    filter10 = filter9.replace('‘', '')
    final = filter10.replace('Vaksinasi', '')

    #filter_chars = ['Digital','Certificate','Sijil','COVID-19','COVID-1 9',
    #                'wl 4G @ ) Profile —','Cerifcate','Vaksinasi',';', ':',
    #                '!', "*",'Vaccination']
    #for j in filter_chars:
    #    final = result.replace(j, ' ') 
    
    ########################################################################
    #                        ADD FILTER WORDS DI SINI
    ########################################################################
    
    print(final)
    user = final[0:28]

    numbers = []
    for word in final.split():
        if word.isdecimal():
            numbers.append(int(word))
            
    print(numbers)
    #if numbers is None:
    if not numbers:
        file_name = root_dir + '\\' + user + '.png'
        new_name = user + '.png'
        #print(new_name)
        if path.isfile(new_name):
            print("extracted-output-image: " + user)
            raw = str(filename)

            # remove characters
            bad_chars = [';', ':', '!', "*", '.png', 'C:\\Users\\ZF\\Documents\\python\\test-py\\']
            for i in bad_chars :
                raw_filter = raw.replace(i, '')

            raw_final_filter = raw_filter.replace('.png', '')
            print("read_file: " + filename)
            print("target_file_to: " + file_name)

            # check if same file
            if file_name == filename:
                print("it's the same file; everthing's fine")
                #do nothing
            else:
                #if digits != 12; then dia bukan IC
                print("(Nama): different file")
                #raw_final_check = int(raw_final_filter)
                digits = str(len(str(raw_final_filter)))
                digit = int(digits)

                # check if filename is already IC
                if raw_final_filter.isdigit() and digit == 12:
                    print("digit: " + digits)
                    print("IC la ni: " + str(raw_final_filter))
                    #do nothing
                    #skip if file already renamed in IC
                else:
                    print("digit: " + digits)
                    print("bukan IC: " + str(raw_final_filter))
                    if path.isfile(file_name):
                        print("file existed!")
                        os.remove(file_name)
                        os.rename(filename, new_name)
                    else:
                        print("boleh la rename sudah")
                        os.rename(filename, new_name)
        else:
            print("ok rename la nama dia") 
            os.rename(filename, new_name)
    else:
        ic = str(numbers[0])
        file_ic = root_dir + '\\' + ic  + '.png'
        new_ic = ic + '.png'
        print("extracted-output-image: " + ic)
        if path.isfile(new_ic):
            print("read_file: " + filename)
            print("target_file: " + file_ic)

            if file_ic == filename:
                print("it's the same file; everthing's fine")
                #do nothing
            else:
                print("(IC): different files")
                os.rename(filename, 'duplicate-' + new_ic)
                os.remove('duplicate-' + new_ic)

        else:
            print("ok rename la IC dia")
            os.rename(filename, new_ic)

    print("###############################################################################")

