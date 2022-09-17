from translate import Translator
from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Language Translator")
root.maxsize(500,500)

# New window for Abbrevations
def ab_win():
    new_win=Tk()
    new_win.title("Abbrevations")
    new_win.maxsize(400,300)
    new_win.minsize(400,300)
    newcanvas = Canvas(new_win, height = 400, width = 300)
    newcanvas.pack()
    newframe = Frame(new_win, bg ="yellow")
    newframe.place(relwidth = 1, relheight = 1)
    newtext=Text(newframe, font = ("Comic Sans MS", 11, "bold"), fg ="#001a4d")
    newtext.insert(END, "Abbrevation:\nAfrikaans = af\nAlbanian = sq\nAmharic = am\nArabic = ar\nArmenian = hy\nAzerbaijani = az\nBasque = eu\nBelarusian = be\nBengali = bn\nBosnian = bs\nBulgarian = bg\nCatalan = ca\nCebuano = ceb\nChinese (Simplified) = zh-CN or zh (BCP-47)\nChinese (Traditional) = zh-TW (BCP-47)\nCorsican = co\nCroatian = hr\nCzech = cs\nDanish = da\nDutch = nl\nEnglish = en\nEsperanto = eo\nEstonian = et\nFinnish = fi\nFrench = fr\nFrisian = fy\nGalician = gl\nGeorgian = ka\nGerman = de\nGreek = el\nGujarati = gu\nHaitian Creole = ht\nHausa = ha\nHawaiian = haw\nHebrew = he or iw\nHindi = hi\nHmong = hmn\nHungarian = hu\nIcelandic = is\nIgbo = ig\nIndonesian = id\nIrish = ga\nItalian = it\nJapanese = ja\nJavanese = jv\nKannada = kn\nKazakh = kk\nKhmer = km\nKinyarwanda = rw\nKorean =ko\nKurdish = ku\nKyrgyz = ky\nLao = lo\nLatvian = lv\nLithuanian = lt\nLuxembourgish = lb\nMacedonian = mk\nMalagasy = mg\nMalay = ms\nMalayalam = ml\nMaltese = mt\nMaori = mi\nMarathi = mr\nMongolian = mn\nMyanmar (Burmese) = my\nNepali = ne\nNorwegian = no\nNyanja (Chichewa) = ny\nOdia (Oriya) = or\nPashto = ps\nPersian = fa\nPolish = pl\nPortuguese (Portugal, Brazil) = pt\nPunjabi = pa\nRomanian = ro\nRussian = ru\nSamoan = sm\nScots Gaelic = gd\nSerbian = sr\nSesotho = st\nShona = sn\nSindhi = sd\nSinhala (Sinhalese) = si\nSlovak = sk\nSlovenian = sl\nSomali = so\nSpanish = es\nSundanese = su\nSwahili = sw\nSwedish = sv\nTagalog (Filipino) = tl\nTajik = tg\nTamil = ta\nTatar = tt\nTelugu = te\nThai = th\nTurkish = tr\nTurkmen = tk\nUkrainian = uk\nUrdu = ur\nUyghur = ug\nUzbek = uz\nVietnamese = vi\nWelsh = cy\nXhosa = xh\nYiddish = yi\nYoruba = yo\nZulu = zu")
    newbutton = Button(newframe, text = "Back",font = ("Comic Sans MS", 11, "bold"),  bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black", command = lambda:new_win.destroy())
    newbutton.place(relx = 0.76, rely = 0.82, relwidth = 0.14, relheight = 0.11)
    newtext.place(relx = 0.05, rely = 0.05,relwidth = 0.90, relheight = 0.90)
    v = Scrollbar(newtext)
    v.pack(side = RIGHT, fill = Y)
    v.config(command=newtext.yview)
    newtext.config(yscrollcommand = v.set)
    new_win.mainloop()

# Input Text Function    
def input_text():
    global inp
    inp=entry1.get(1.0, "end-1c")
    translator = Translator(to_lang=lan)
    Translation = translator.translate(inp)
    entry2.delete(1.0,END) #deletes previous text
    entry2.insert(1.0,Translation)
# Input Language Function
def input_lang():
    global lan
    lan=entry3.get(1.0, "end-1c")

# Title Label 
lab1=Label(root, text="Language Translator", )
lab1.grid(row=0, column=0, columnspan=3)
lab1.config(font=("Courier", 25))

# Select Language
lab2=Button(root, text="Enter Langauge and Press", command=input_lang)
lab2.grid(row=4, column=0)

# Select Language Entry
entry3=Text(root, wrap=WORD, height=1, width=10)
entry3.grid(row=4,column=1)

# Abbrevation of Languages
btn = Button(root,text ="Abbrevation",command = ab_win)
btn.grid(row=4, column=2)

# Translate Button
button1=Button(root, text="Translate",command=input_text)
button1.grid(row=7, column=1)

# Enter Text
entry1=Text(root, wrap=WORD, height=15, width=20)
entry1.grid(row=7,column=0, padx=20, pady=10)
lab3=Label(root, text="Enter Text")
lab3.grid(row=6, column=0)

# Output
entry2=Text(root, wrap=WORD, height=15, width=18)
entry2.grid(row=7,column=2, padx=20)
lab4=Label(root, text="Output")
lab4.grid(row=6, column=2)

# Exit
exit_btn=Button(root, text="Close", command=root.destroy)
exit_btn.grid(row=8, column=2)

# Empty
lab7=Label(root, text=" ")
lab7.grid(row=1, column=0, columnspan=3)
lab6=Label(root, text=" ")
lab6.grid(row=3, column=0, columnspan=3)
lab8=Label(root, text=" ")
lab8.grid(row=5, column=0, columnspan=3)

# Instruction
lab5=Label(root, text="Instruction:- You need to input 'Language Code' first then press button to load desired langauge and then use translator.", wraplength=410)
lab5.grid(row=2, column=0, columnspan=3)


root.mainloop()