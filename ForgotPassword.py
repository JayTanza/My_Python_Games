#Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
from PIL import ImageTk
import pygame
import sys
import sqlite3

root = Tk()
root.resizable(0,0)
root.iconbitmap("Images/favicon.ico")
# in order to add image in window
bgImage = ImageTk.PhotoImage(file='Images/bg1.jpg')
# pass the image through label to view
bgLabel = Label(root,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH, expand=YES)

# add background music
pygame.mixer.init()
pygame.mixer.music.load("BGMusic/Helmet Heroes Soundtrack - 02 - Heaths Training Ground.mp3")
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

back_btn = Button(root, text='<',font=("Comic Sans MS",13, 'bold'),fg='white',bg='limegreen',height='1', width='3',command=lambda: Login_page())
back_btn.place(x=2,y=2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Helmet Heroes')
root.iconbitmap(r'Images/favicon.ico')
#root.overrideredirect(1)


heading = Label(root, text='FORGOT PASSWORD', font=("Comic Sans MS", 25, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='20')
heading.place(x=330,y=70)

emaillbl = Label(root, text='Email Address', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
emaillbl.place(x=345,y=170)

emailEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", justify='center')
emailEntry.place(x=345,y=210)

userlbl = Label(root, text='New Password', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
userlbl.place(x=345,y=270)

userEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", show='', justify='center')
userEntry.place(x=345,y=310)

passlbl = Label(root, text='Confirm New Password', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
passlbl.place(x=345,y=370)

passEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", show='', justify='center')
passEntry.place(x=345,y=410)

signup_btn = Button(root, text='UPDATE PASSWORD', font=("Comic Sans MS", 18, "bold"), fg='white', bg='limegreen',height='1', width='25', activebackground='white',command=lambda: forgotpassword())
signup_btn.place(x=345, y=500)

developby = Label(root, text='Developed by: Team Padayon', font=("Comic Sans MS", 10, "bold"), bg='limegreen',fg='white', borderwidth=1, relief="solid", width='25')
developby.place(x=10, y=685)

def forgotpassword():
    if(emailEntry.get() == "" or userEntry.get() == "" or passEntry.get() == ""):
        ms.showerror("Error","All Fields Are Required!")
    elif(userEntry.get() != passEntry.get()):
        ms.showerror('Oops', 'Password Does Not Match!!!')
    else:
        db = sqlite3.connect("Database.db")
        cursor = db.cursor()
        query = 'SELECT * FROM users WHERE Email=?'
        cursor.execute(query, [(emailEntry.get())])
        row = cursor.fetchone()
        if row == None :
            ms.showerror("Error","Email Does not Exist!")
        else:
            query = '''update users set Password=? where Email=?'''
            cursor.execute(query,[userEntry.get(),emailEntry.get(),])
            db.commit()
            db.close()
            ms.showinfo("Success!","Password Updated Successfully!")
            emailEntry.delete(0, 'end')
            userEntry.delete(0, 'end')
            passEntry.delete(0,'end')

def Login_page():
    root.destroy()
    import Signin


def exit_window():
    sys.exit(root.destroy())

root.mainloop()