import json 
from difflib import get_close_matches 
  
# Loading data from json file 
# in python dictionary 
data = json.load(open("data.json")) 
  
def translate(w): 
    # converts to lower case 
    w = w.lower() 
  
    if w in data: 
        return data[w] 
    # for getting close matches of word 
    elif len(get_close_matches(w, data.keys())) > 0:              
        yn = input("Did you mean % s instead? Enter y if yes, or n if no: " % get_close_matches(w, data.keys())[0]) 
        yn = yn.lower() 
        if yn == "y": 
            return data[get_close_matches(w, data.keys())[0]] 
        elif yn == "n": 
            return "Please recheck."
        else: 
            return "Entry not found"
    else: 
        return "Word not exist"
word = input("Enter word: ") 
output = translate(word) 
  
if type(output) == list: 
    for item in output: 
        print(item) 
else: 
    print(output) 
input('Press ENTER to exit')  