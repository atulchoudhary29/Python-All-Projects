import random
from tkinter import *

window=Tk()
window.title('Dice Roll Simulator')

def dicesim():
    number=random.randint(1,6)
    l2=Label(window, text=str(number), font=("Arial", 25))
    l2.place(relx=0.5, rely=0.65)

l1=Label(window, text="Roll the Dice", font=("Arial", 40))
l1.place(relx=0.5, rely=0.3, anchor='center')

b1=Button(window, text="Press me to get number", font=("Times New Roman", 15), command=(dicesim))
b1.place(relx=0.5, rely=0.5, anchor='center')

exit=Button(window, text="Exit" , font=("Times New Roman", 12), command=window.destroy)
exit.place(relx=1.0, rely=0.0, anchor='ne')

window.geometry("400x400")
window.minsize(400, 400)

window.mainloop()