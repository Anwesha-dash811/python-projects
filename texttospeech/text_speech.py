# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:58:59 2020

@author: DELL
"""

from tkinter import *
from gtts import gTTS    
import os 
  
# create tkinter window 
root = Tk() 
root.title("text_to_speech_convertor") 
root.geometry("400x350") 

label = Label(text = "Enter the text here",font = "bold, 15") 
  
label.grid(row=2,column=2)
entry = Entry(width = 45,bd = 4, font = 14) 
  
entry.grid(row=3,column=2) 
entry.insert(0, "") 
  
# define a function which can  
# get text and convert into audio 
def play(): 
    language = "en"
    myobj = gTTS(text = entry.get(),lang = language, slow = False) 
    myobj.save("output.wav") 
    os.system("output.wav") 
  
  
btn = Button(text = "SUBMIT", 
             width = "15", pady = 10, 
             font = "bold, 15",  
             command = play, bg='grey',fg='white') 
  
btn.grid(row=5,column=2)


root.mainloop() 