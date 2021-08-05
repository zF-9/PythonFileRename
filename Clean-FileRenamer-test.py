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
root_dir = r'C:\Users\Fauzi\Documents\PythonFileRename\test-py'
#r'C:\Users\Fauzi\Desktop\un-opencv'
#r'C:\Users\Fauzi\Desktop\to_convert'
#r'C:\Users\Fauzi\Documents\PythonFileRename\test-py'

file_format = ".png" #change format globally , eg: .png/.jpeg/.jpg
ic = ' '
#numbers = []
#new_ic = ''
#file_ic = ''


#def get_ic():

        #for i in numbers:
            #print(numbers[i])
            #print(len(numbers[i]))
            #print(len(str(numbers[i])))
            #if len(str(numbers[i])) == 12:
            #    ic = str(numbers[i])
            #    return ic

def get_name():
    file_name = root_dir + '\\' + user + '.png'
    new_name = user + '.png'
    #print(new_name)
    if path.isfile(new_name):
        print("extracted-output-image: " + user)
        raw = str(filename)

        # remove characters
        bad_chars = [';', ':', '!', "*", '.png', 'C:\\Users\\ZF\\Documents\\python\\test-py\\']
        for i in bad_chars :
            raw = raw.replace(i, '')

        raw_final_filter = raw.replace('.png', '')
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

# .FILE FORMAT CHANGEABLE
for filename in glob.iglob(root_dir + '**/*' + file_format, recursive=True):
    pattern = r"\Digital Certificate\b" or r"\Sijil Digital\b"
    keyword = {'Digital','Certificate', 'Sijil','COVID-19', 'Vaccination', 'Vaksinasi' }

    while True:
        try:
            textImg = pytesseract.image_to_string(filename)
            break
        except ValueError:
            print("Oops!  file is corrupted! ")
            pass

    #textImg = pytesseract.image_to_string(filename)
    text = str(textImg.strip())
    queryword = text.split()
    substring = str(text.partition("Digital"))
    #print(substring.split("Digital", "Sijil", "Certificate"))
    
    resultword = [word for word in queryword if word.lower() not in keyword]
    result = ' '.join(resultword)
    
    ########################################################################
    #                        ADD FILTER WORDS DI SINI
    ########################################################################    
    #filter1 = result.replace('Digital', '')
    #filter2 = filter1.replace('Certificate', '')
    #filter3 = filter2.replace('Vaccination', '')
    #filter4 = filter3.replace('Sijil', '')
    #filter5 = filter4.replace('COVID-19', '')
    #filter6 = filter5.replace('COVID-1 9', '')
    #filter7 = filter6.replace('wl 4G @ ) Profile —', '')
    #filter8 = filter7.replace('Cerifcate', '')
    #filter9 = filter8.replace('wl 4G @ ) Profile —', '')
    #filter10 = filter9.replace('‘', '')
    #filter11 = filter10.replace('Vay NP Gat', '')
    #filter12 = filter11.replace('© LTE* il” 53% o™ @: emo” s as ema', '')
    #filter13 = filter12.replace('sijil','')
    #filter14 = filter13.replace('vaksin', '')
    #filter15 = filter14.replace('Check-In Maklumat Check-in Lokasi Servay Express - Kimanis Nama', '')
    #filter16 = filter15.replace('12:17PTG & ace il © 944 953%', '')
    #filter17 = filter16.replace('18:55 fas @--- Os GD', '')
    #filter18 = filter17.replace('oOo "oo" e Oo e', '')
    #final = filter18.replace('Vaksinasi', '')

    filter_chars = ['Digital','Certificate','Sijil','COVID-19','COVID-1 9',
                    'wl 4G @ ) Profile —','Cerifcate','Vaksinasi',';', ':',
                    '!', "*",'Vaccination', 'acelil|', '‘', 'Sijil', 'COVID', 'wl 4G @ ) Profile —',
                    'wl 4G @ ) Profile —', 'Cerifcate', 'vaksin', '© LTE* il” 53% o™ @: emo” s as ema'
                    'oOo "oo" e Oo e', 'Vaksinasi', 'KEKAL SELAMATEED  ,1l| <@ Profile', 'au 10 349 080 a cey il',
                    'voure oe Og ® © ¥ HH 10 33 Profil — Ini adalah kod OR untuk profil MySejahtera anda.',
                    'Sila tunjukkan ini kepada pihak berkuasa apabila diminta Negatif',
                    'Tarikh pengesahan  07/04/2021 Sumber  MKAK, KKM', '        ', 'O 6s a Profile 7',
                    ' ']
    for j in filter_chars:
        result = result.replace(j, ' ')

    print(result)
    
    ########################################################################
    #                        ADD FILTER WORDS DI SINI
    ########################################################################
    
    #print(final)
    user = result[0:28]

    numbers = []
    for word in result.split():
        if word.isdecimal():
            numbers.append(int(word))
            
    print(numbers)


    print('afer: ' + str(numbers))
    #if numbers is None:
    if not numbers:
        get_name()

    else:
        for i in numbers:
            if len(str(i)) == 12:
                ic = str(i)

            else:
                file_name = root_dir + '\\' + user + '.png'
                new_name = user + '.png'
                get_name()

        print(ic)
        #if len(numbers) == 1:
            #print(len(numbers))
            #print(numbers[0])
            #ic = str(numbers[0])
        #else:
            #if len(str(numbers[0])) == 12:
            #    ic = str(numbers[0])
            #else:
                #print(len(numbers))
                #print(numbers[1])
                #ic = str(numbers[1])
            
        #for i in numbers:
            #print(i)
            #if len(str(numbers[i])) != 12:
            #    ic = str(numbers[i])
            #    print(ic)
            #    file_ic = root_dir + '\\' + ic  + '.png'
            #    new_ic = ic + '.png'
            #else:
            #    file_name = root_dir + '\\' + user + '.png'
            #    new_name = user + '.png'                
            #    print("boleh la rename sudah")
            #    os.rename(filename, new_name)
                #goto end
        #if len(str(numbers[0])) != 12:
            #ic = str(numbers[1])
        
        #file_ic = root_dir + '\\' + ic  + '.png'
        #new_ic = ic + '.png'

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

        #label: end
        #print("successful")

    print("###############################################################################")


    
