from tkinter import * #Access all the module of tkinter
from PIL import ImageTk
import sys
import pygame
from tkinter import messagebox as ms
import sqlite3

#Functionality part

root = Tk()
root.resizable(0,0)
# in order to add image in window
bgImage = ImageTk.PhotoImage(file='Images/LoadingBackground.jpg')
# pass the image through label to view
bgLabel = Label(root,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH, expand=YES)

# add background music
pygame.mixer.init()
pygame.mixer.music.load("BGMusic/Helmet Heroes Soundtrack - 01 - Helmet Heroes.mp3")
pygame.mixer.music.play(loops=0)

# Calculate Starting X and Y coordinates for Window
w = 1080  # Width
h = 720  # Height
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight()  # Height of the screen
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)

exit_btn = Button(root, text='X',command=lambda: exit_window(), font=("Comic Sans MS",13, 'bold'),fg='white',bg='limegreen',height='1', width='3')
exit_btn.place(x=1038,y=2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Helmet Heroes')
root.iconbitmap(r'Images/favicon.ico')
#root.overrideredirect(1)

heading = Label(root, text='CHOOSE GAMES', font=("Comic Sans MS", 25, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='15')
heading.place(x=370,y=365)


game1_btn = Button(root, text='Typing Game', font=("Comic Sans MS", 18, "bold"),fg='white',bg='limegreen',height='1', width='20',command=lambda: Game1())
game1_btn.place(x=370,y=430)

game2_btn = Button(root, text='Shooter Game', font=("Comic Sans MS", 18, "bold"),fg='white',bg='limegreen',height='1', width='20',command=lambda: Game2())
game2_btn.place(x=370,y=500)

game3_btn = Button(root, text='Shapes Game', font=("Comic Sans MS", 18, "bold"),fg='white',bg='limegreen',height='1', width='20',command=lambda: Game3())
game3_btn.place(x=370,y=570)

developby = Label(root, text='Developed by: Team Padayon', font=("Comic Sans MS", 10, "bold"), bg='limegreen',fg='white', borderwidth=1, relief="solid", width='25')
developby.place(x=10, y=685)

def Game1():
    root.destroy()
    import TypingGame

def Game2():
    root.destroy()
    import ShooterGame

def Game3():
    root.destroy()
    import App

def exit_window():
    sys.exit(root.destroy())

root.mainloop()