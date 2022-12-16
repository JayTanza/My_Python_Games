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


heading = Label(root, text='CREATE AN ACCOUNT', font=("Comic Sans MS", 25, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='20')
heading.place(x=330,y=50)

emaillbl = Label(root, text='Email Address', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
emaillbl.place(x=345,y=150)

emailEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", justify='center')
emailEntry.place(x=345,y=190)

userlbl = Label(root, text='Username', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
userlbl.place(x=345,y=250)

userEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", show='', justify='center')
userEntry.place(x=345,y=290)

passlbl = Label(root, text='Password', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
passlbl.place(x=345,y=350)

passEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", show='', justify='center')
passEntry.place(x=345,y=390)

repasslbl = Label(root, text='Confirm Password', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
repasslbl.place(x=345,y=450)

repassEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", show='', justify='center')
repassEntry.place(x=345,y=490)

check = IntVar()

termandconditions = Checkbutton(root, text='I agree to the Terms & Conditions',font=("Comic Sans MS", 13, "bold"), width='35', variable=check)
termandconditions.place(x=345, y=540)

signup_btn = Button(root, text='SIGN UP', font=("Comic Sans MS", 18, "bold"), fg='white', bg='limegreen',height='1', width='25', activebackground='white',command=lambda: database())
signup_btn.place(x=345, y=585)

developby = Label(root, text='Developed by: Team Padayon', font=("Comic Sans MS", 10, "bold"), bg='limegreen',fg='white', borderwidth=1, relief="solid", width='25')
developby.place(x=10, y=685)

def database(arg=None):
    #Getting entries
    email = emailEntry.get()
    name = userEntry.get()
    password = passEntry.get()
    confirmpassword = repassEntry.get()

    #Validating Entries
    validation = []

    #Adding information to the list
    validation.append(email)
    validation.append(name)
    validation.append(password)
    validation.append(confirmpassword)

    #Boolean for Condition
    condition = True

    for ele in validation:
        if ele == '':
            condition = False
            break

    if condition:
        #Check for password match
        if password != confirmpassword:
            ms.showerror('Oops', 'Password Does Not Match!!!')
        elif (check.get() == 0):
            ms.showerror('Error', 'Please Accept Terms and Conditions!')
        else:
            #Making connection
            conn = sqlite3.connect('Database.db')

            #Creating cursor
            with conn:
                cursor = conn.cursor()
            find_user = ('SELECT * FROM users WHERE Username = ? AND Password = ?')
            cursor.execute(find_user, (name,password))
            results = cursor.fetchall()

            if results:
                ms.showerror('Oops', 'The Username has Alreay Taken!')
            else:
                #Making table if not exist
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (Email TEXT NOT NULL,Username TEXT NOT NULL,Password TEXT NOT NULL)')

                #Inserting Data into Table
                cursor.execute('INSERT INTo Users (Email,Username,Password) VALUES(?,?,?)',(email,name,password))
                conn.commit()

                #Showing success message
                ms.showinfo('Successful','Account Created Successfully!!! Now You Can Login To System!!')

                #Clearing all the entries input by user
                emailEntry.delete(0, 'end')
                userEntry.delete(0, 'end')
                passEntry.delete(0, 'end')
                repassEntry.delete(0, 'end')
    else:
        ms.showerror('Oops', 'Please Fill All The Input Fields!')
def Login_page():
    root.destroy()
    import Signin


def exit_window():
    sys.exit(root.destroy())

root.mainloop()