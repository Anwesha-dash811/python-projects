# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:34:40 2020

@author: DELL
"""

from indic_transliteration import sanscript 
from indic_transliteration.sanscript import transliterate 
from tkinter import *
root = Tk() 
root.configure(background = 'purple1')   
root.geometry("400x350")   
root.title("English to Hindi Converter") 
# Function to clear both the text areas 
def clearAll() : 
    field1.delete(1.0, END) 
    field2.delete(1.0, END) 
  
# Function to convert into Devanagari text  
def convert() : 
    input = field1.get("1.0", "end")[:-1] 
    output = transliterate(input, sanscript.ITRANS,  
                                            sanscript.DEVANAGARI) 
    
    field2.insert('end -1 chars', output) 
label1 = Label(root, text = " Enter English Text ", fg = 'white',bg='pink3')
label1.grid(row = 1, column = 0, padx = 10, pady = 10)   
        
label2 = Label(root, text = " Devnagiri Converted Text",fg = 'white',bg='pink3')
label2.grid(row = 3, column = 0, padx = 10, pady = 10)     
field1 = Text(root, height = 5, width = 25, font = "lucida 13")
field1.grid(row = 1, column = 1, padx = 10, pady = 10) 
field2 = Text(root, height = 5, width = 25, font = "lucida 13")
field2.grid(row = 3, column = 1, padx = 10, pady = 10)  
button1 = Button(root, text = "Convert into Devnagiri text",  
                     bg = "pink3", fg = "white", command = convert)
button1.grid(row = 2, column = 1)    
button2 = Button(root, text = "Clear", bg = "pink3",   
                     fg = "white", command = clearAll)
button2.grid(row = 4, column = 1)   

root.mainloop()      

      
