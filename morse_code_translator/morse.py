# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:49:09 2020

@author: DELL
"""
 
from tkinter import *
  
# Create a GUI window  
root = Tk() 
  
# create a global variables   
variable1 = StringVar(root)  
variable2 = StringVar(root)  
    
# initialise the variables  
variable1.set("lang-code")  
variable2.set("lang-code")  
    

# Dictionary representing the morse code chart  
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',  
                    'C':'-.-.', 'D':'-..', 'E':'.',  
                    'F':'..-.', 'G':'--.', 'H':'....',  
                    'I':'..', 'J':'.---', 'K':'-.-',  
                    'L':'.-..', 'M':'--', 'N':'-.',  
                    'O':'---', 'P':'.--.', 'Q':'--.-',  
                    'R':'.-.', 'S':'...', 'T':'-',  
                    'U':'..-', 'V':'...-', 'W':'.--',  
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    'a':'.-', 'b':'-...',  
                    'c':'-.-.', 'd':'-..', 'e':'.',  
                    'f':'..-.', 'g':'--.', 'h':'....',  
                    'i':'..', 'j':'.---', 'k':'-.-',  
                    'l':'.-..', 'm':'--', 'n':'-.',  
                    'o':'---', 'p':'.--.', 'q':'--.-',  
                    'r':'.-.', 's':'...', 't':'-',  
                    'u':'..-', 'v':'...-', 'w':'.--',  
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',  
                    '4':'....-', '5':'.....', '6':'-....',  
                    '7':'--...', '8':'---..', '9':'----.',  
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',  
                    '?':'..--..', '/':'-..-.', '-':'-....-',  
                    '(':'-.--.', ')':'-.--.-'}  
  
# Function to clear both the text areas 
def clearAll() : 
    # whole content of text area  is deleted  
    language1_field.delete(1.0, END) 
    language2_field.delete(1.0, END) 
  
# Function to perform coversion form one 
# language to another 
def convert() : 
    message = language1_field.get("1.0", "end")[:-1] 
  
    if variable1.get() == "Eng" and variable2.get() == "Morse" : 
        rslt = encrypt(message) 
  
    elif variable1.get() == "Morse" and variable2.get() == "Eng" : 
        rslt = decrypt(message) 
    language2_field.insert('end -1 chars', rslt) 
      
          
# Function to encrypt the string  
# according to the morse code chart  
def encrypt(message): 
    cipher = ''  
    for letter in message:  
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:  
            cipher += ' '
    
    return cipher  
    
# Function to decrypt the string  
# from morse to english  
def decrypt(message):  
    message += ' '
    
    decipher = ''  
    citext = ''  
    for letter in message:  
        if (letter != ' '):  
            i = 0
            citext += letter  
        else:  
            i += 1
            if i == 2 :  
                decipher += ' '
            else:  
                decipher += list(MORSE_CODE_DICT.keys())[ 
                             list(MORSE_CODE_DICT .values()).index(citext)]  
                citext = ''  
    
    return decipher  
  
  
# Driver code  
if __name__ == "__main__" :  
      
    # Set the background colour of GUI window   
    root.configure(background = 'light green')   
      
    # Set the configuration of GUI window (WidthxHeight)  
    root.geometry("400x350")   
  
    # set the name of tkinter GUI window   
    root.title("Translator") 

    # Create a "One Language " label   
    label1 = Label(root, text = "One Language ",  
                 fg = 'black', bg = 'light yellow')  
    label1.grid(row = 1, column = 0)   
        
    # Create a "From Language " label   
    label2 = Label(root, text = "From Language",   
                   fg = 'black', bg = 'light yellow')   
    label2.grid(row = 2, column = 0)  
      
    # Create a "To Language " label   
    label3 = Label(root, text = "To Language ",   
                   fg = 'black', bg = 'light yellow')  
    label3.grid(row = 3, column = 0)  
    
    # Create a "Converted Language " label   
    label4 = Label(root, text = "Converted Language ",   
                   fg = 'black', bg = 'light yellow')  
    label4.grid(row = 5, column = 0)  
        
    # Create a text area box   
    # for filling or typing the information.   
    language1_field = Text(root, height = 5, width = 25,  
                                     font = "lucida 13")  
    language2_field = Text(root, height = 5, width = 25,  
                                     font = "lucida 13") 
         
    # padx keyword argument used to set paading along x-axis .   
    language1_field.grid(row = 1, column = 1, padx = 10)   
    language2_field.grid(row = 5, column = 1, padx = 10)  
    
    # list of language codes  
    languageCode_list = ["Eng", "Morse"]  
    
    # create a drop down menu using OptionMenu function  
    # which takes window name, variable and choices as  
    # an argument. use * befor the name of the list,  
    # to unpack the values  
    FromLanguage_option = OptionMenu(root, variable1, *languageCode_list)  
    ToLanguage_option = OptionMenu(root, variable2, *languageCode_list)  
        
    FromLanguage_option.grid(row = 2, column = 1, ipadx = 10)  
    ToLanguage_option.grid(row = 3, column = 1, ipadx = 10)  
        
    # Create a Convert Button and attached   
    # with convert function   
    button1 = Button(root, text = "Convert", bg = "light blue", fg = "black",  
                                command = convert)  
        
    button1.grid(row = 4, column = 1)  
    
    # Create a Clear Button and attached   
    # with clearAll function   
    button2 = Button(root, text = "Clear", bg = "light blue",   
                     fg = "black", command = clearAll) 
      
    button2.grid(row = 6, column = 1)  
      
    # Start the GUI   
    root.mainloop()   
