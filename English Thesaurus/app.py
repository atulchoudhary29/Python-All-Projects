import json
from difflib import get_close_matches # Library for find similar word.

data=json.load(open("data.json"))

def translate(w):
    l=w.lower() # Lowercase all the letters.
    c=w.capitalize() # Capitalize first letter.

    if w in data:
        return data[w] 
    elif l in data:
        return data[l]
    elif c in data:
        return data[c]

    # Checking Similar Words
    elif len(get_close_matches(w, data.keys())) > 0:
        var1= input("Did you mean %s instead? Press Y if yes, or N if no. " % get_close_matches(w, data.keys())[0])       
        if var1 == "Y" or var1 == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif var1 =="N" or var1 =="n":
            return "This word doesn't exist. Please double check it."    
        else:
            return "We didn't understand your entry."    

    elif len(get_close_matches(l, data.keys())) > 0:
        var2= input("Did you mean %s instead? Press Y if yes, or N if no. " % get_close_matches(l, data.keys())[0])
        if var2 == "Y" or var2 =="y":
            return data[get_close_matches(l, data.keys())[0]]
        elif var2 =="N" or var2 =="n":
            return "This word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."    

    elif len(get_close_matches(c, data.keys())) > 0:
        var3= input("Did you mean %s instead? Press Y if yes, or N if no. " % get_close_matches(c, data.keys())[0])
        if var3 == "Y" or var3 == "y":
            return data[get_close_matches(c, data.keys())[0]]
        elif var3 =="N" or var3 == "n":
            return "This word doesn't exist. Please double check it."    
        else:
            return "We didn't understand your entry."    

    else:
        return "This word doesn't exist. Please double check it."   

word = input("Enter Word: ")
output=translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)     
