# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:45:35 2020

@author: DELL
"""
import tkinter as tk
from tkinter import StringVar
from tkinter import END

  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
from tkinter import filedialog
  
  
# creating root object 
root = tk.Tk() 
  
# defining size of window 
root.geometry("1200x6000") 
  
# setting up the title of window 
root.title("Message Encryption and Decryption") 
Tops = tk.Frame(root, width = 1600) 
Tops.pack(side ="top") 
  
f1 =tk. Frame(root, width = 800, height = 700)
f1.pack(side = "left") 
lblInfo = tk.Label(Tops, font = ('algerian', 40, 'bold'), 
          text = "SECRET MESSAGING", 
                     fg = "Black", bd = 10, anchor='w').grid(row = 0, column = 0) 

Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 
  
# exit function 
def Exit(): 
    root.destroy() 
  
# Function to reset the window 
def Reset(): 
    #rand.set("") 
    Msg.set("") 
    key.set("") 
    mode.set("") 
    Result.set("") 

# labels 
lblMsg = tk.Label(f1, font = ('algerian', 16, 'bold'), 
         text = "TYPE MESSAGE HERE", bd = 16, anchor = "w").grid(row = 1, column = 0) 
  
txtMsg = tk.Entry(f1, font = ('algerian', 16, 'bold'), 
         textvariable = Msg, bd = 10, insertwidth = 4, 
                bg = "powder blue", justify = 'right').grid(row = 1, column = 1) 
lblkey =tk. Label(f1, font = ('algerian', 16, 'bold'), 
            text = "TYPE KEY HERE", bd = 16, anchor = "w").grid(row = 2, column = 0) 
  
txtkey =tk. Entry(f1, font = ('algerian', 16, 'bold'), 
         textvariable = key, bd = 10, insertwidth = 4, 
                bg = "powder blue", justify = 'right').grid(row = 2, column = 1) 
  
lblmode = tk.Label(f1, font = ('algerian', 16, 'bold'), 
          text = "TYPE MODE(e for encrypt, d for decrypt) HERE", 
                                bd = 16, anchor = "w").grid(row = 3, column = 0) 
  
txtmode = tk.Entry(f1, font = ('algerian', 16, 'bold'), 
          textvariable = mode, bd = 10, insertwidth = 4, 
                  bg = "powder blue", justify = 'right').grid(row = 3, column = 1) 
  
lblResult = tk.Label(f1, font = ('algerian', 16, 'bold'), 
             text = "ENCRYPTED/DECRYPTED MESSAGE", bd = 16, anchor = "w").grid(row = 4, column =0) 
  
txtResult = tk.Entry(f1, font = ('algerian', 16, 'bold'),  
             textvariable = Result, bd = 10, insertwidth = 4, 
                       bg = "powder blue", justify = 'right').grid(row = 4, column =1) 
  
# Vigenère cipher 
import base64 
  
# Function to encode 
def encode(key, clear): 
    enc = [] 
      
    for i in range(len(clear)): 
        key_c = key[i % len(key)] 
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256) 
                       
        enc.append(enc_c) 
          
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 
  
# Function to decode 
def decode(key, enc): 
    dec = [] 
      
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256) 
                             
        dec.append(dec_c) 
    return "".join(dec) 
  
  
def Ref(): 
    print("Message= ", (Msg.get())) 
  
    clear = Msg.get() 
    k = key.get() 
    m = mode.get() 
  
    if (m == 'e'): 
        Result.set(encode(k, clear)) 
    else: 
        Result.set(decode(k, clear)) 
  
# Show message button 
btnTotal = tk.Button(f1, padx = 10, pady = 5, bd = 16, fg = "black", 
                        font = ('algerian', 16, 'bold'), width = 10, 
                       text = "Show Message", bg = "light pink", 
                         command = Ref).grid(row = 7, column = 0) 
  
# Reset button 
btnReset = tk.Button(f1, padx = 10, pady = 5, bd = 16, 
                  fg = "black", font = ('algerian', 16, 'bold'), 
                    width = 10, text = "Reset", bg = "light pink", 
                   command = Reset).grid(row = 7, column = 1) 
  
# Exit button 
btnExit =tk. Button(f1, padx = 10, pady = 5, bd = 16,  
                 fg = "black", font = ('algerian', 16, 'bold'), 
                      width = 10, text = "Exit", bg = "light pink", 
                  command = Exit).grid(row = 7, column = 2) 


# keeps window alive 
root.mainloop() 