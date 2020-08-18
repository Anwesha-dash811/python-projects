# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:13:22 2020

@author: DELL
"""
#pip install googletrans #to install googletrans
#to know all the language that translator suports along with their short forms
#import googletrans
#print(googletrans.LANGUAGES)

from googletrans import Translator
import tkinter as tk

win=tk.Tk()
win.title("Translator")
win.geometry("300x80")
def translator():
    
    word = entry.get()
    translator=Translator(service_urls=["translate.google.com"])
    translation=translator.translate(word,dest="de") #change the short forms used in dest to get different language translations like "de" is for german
    label1=tk.Label(win,text=f'Translated word: {translation.text}',bg="cyan")
    label1.grid(row=2,column=0)
    label2=tk.Label(win,text="Translated in german",bg="cyan") #change the name of the language here
    label2.grid(row=4,column=0)


label=tk.Label(win,text="Write here")
label.grid(row=0,column=0)
entry=tk.Entry(win)
entry.grid(row=1,column=0)
btn=tk.Button(win,text="Go",command=translator)
btn.grid(row=1,column=1)
win.mainloop()

