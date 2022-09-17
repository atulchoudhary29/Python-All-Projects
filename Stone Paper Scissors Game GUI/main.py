from tkinter import *
import random

# Screen Window
window=Tk()
window.title('Rock, Paper, Scissor Game')
width=690
height=600
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0,0)
window.config(bg="green")

# Load Images
blankimage=PhotoImage(file="D:\\Python_Files\\My_Projects\\5_Stone_Paper_Scissors\\Resources\\Blankimage.png")
rockplayer=PhotoImage(file="D:\\Python_Files\\My_Projects\\5_Stone_Paper_Scissors\\Resources\\Stone.png")
rockplayer_a=rockplayer.subsample(3,3)
paperplayer=PhotoImage(file="D:\\Python_Files\\My_Projects\\5_Stone_Paper_Scissors\\Resources\\Paper.png")
paperplayer_a=paperplayer.subsample(3,3)
scissorplayer=PhotoImage(file="D:\\Python_Files\\My_Projects\\5_Stone_Paper_Scissors\\Resources\\Scissors.png")
scissorplayer_a=scissorplayer.subsample(3,3)
rockcomp=PhotoImage(file="D:\\Python_Files\\My_Projects\\5_Stone_Paper_Scissors\\Resources\\Stone_Com.png")
papercomp=PhotoImage(file="D:\\Python_Files\\My_Projects\\5_Stone_Paper_Scissors\\Resources\\Paper_Com.png")
scissorcomp=PhotoImage(file="D:\\Python_Files\\My_Projects\\5_Stone_Paper_Scissors\\Resources\\Scissors_Com.png")

# Functions
def Rock():
    global player_option
    player_option=1
    image_player.configure(image=rockplayer)
    MatchProcess()

def Paper():
    global player_option
    player_option=2
    image_player.configure(image=paperplayer)
    MatchProcess()

def Scissor():
    global player_option
    player_option=3
    image_player.configure(image=scissorplayer)
    MatchProcess()

def MatchProcess():
    option_computer=random.randint(1, 3)    
    if option_computer==1:
        computer_image.configure(image=rockcomp)
        Rockcom()
    elif option_computer==2:
        computer_image.configure(image=papercomp)    
        Papercom()
    elif option_computer==3:
        computer_image.configure(image=scissorcomp)    
        Scissorcom()

def Rockcom():
      if player_option==1:
          label_status.config(text="Game Tie")      
      elif player_option==2:
          label_status.config(text="Player Win")
      elif player_option==3:
          label_status.config(text="Computer Win")    

def Papercom():
      if player_option==1:
          label_status.config(text="Game Tie")      
      elif player_option==2:
          label_status.config(text="Player Win")
      elif player_option==3:
          label_status.config(text="Computer Win")

def Scissorcom():
      if player_option==1:
          label_status.config(text="Game Tie")      
      elif player_option==2:
          label_status.config(text="Player Win")
      elif player_option==3:
          label_status.config(text="Computer Win")

def Exit():
    window.destroy()
    exit()

# ***********************Widgets************************
# 1. Labels
image_player= Label(window, image=blankimage)
image_player.grid(row=2, column=1, padx=30, pady=20)
computer_image=Label(window, image=blankimage)  
computer_image.grid(row=2, column=3, pady=20)  
player_label=Label(window, text="Player")
player_label.grid(row=1, column=1)
player_label.config(bg="blue", fg="white", font=("Arial", 12, "bold"))
computer_label=Label(window, text="Computer")
computer_label.grid(row=1, column=3)
computer_label.config(bg="blue", fg="white", font=("Arial", 12, "bold"))
label_status=Label(window, text="", font=("Arial", 12))
label_status.grid(row=3, column=2)
label_status.config(bg="green", fg="red", font=("Arial", 20, "bold"))

# 2. Buttons
rock=Button(window, image=rockplayer_a, command=Rock)
rock.grid(row=4, column=1, pady=30)
paper=Button(window, image=paperplayer_a, command=Paper)
paper.grid(row=4, column=2, pady=30)
scissor=Button(window, image=scissorplayer_a, command=Scissor)
scissor.grid(row=4, column=3, pady=30)
button_exit=Button(window, text="Quit", bg="Blue", fg="white", font=("Arial", 18, "bold"), command=Exit)
button_exit.grid(row=5, column=2)

window.mainloop()