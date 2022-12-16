from tkinter import * #Access all the module of tkinter
from PIL import ImageTk
import sys
import pygame
from tkinter import messagebox as ms
import sqlite3

#Functionality part

def createacc_page():
    root.destroy()
    import Signup

def Forgotpass_page():
    root.destroy()
    import ForgotPassword

def play_page():
    root.destroy()

def user_enter(event):
    if(userEntry.get()=='Enter Username'):
        userEntry.delete(0,END)

def pass_enter(event):
    if(passEntry.get()=='Enter Password'):
        passEntry.delete(0,END)

def hide():
    openeye.config(file='Images/closeye.png')
    passEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='Images/openeye.png')
    passEntry.config(show='')
    eyeButton.config(command=hide)

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

heading = Label(root, text='SIGN-IN', font=("Comic Sans MS", 25, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='15')
heading.place(x=370,y=365)

userEntry=Entry(root, width=20, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", justify='center')
userEntry.place(x=370,y=440)
userEntry.insert(0,'Enter Username')
userEntry.bind('<FocusIn>', user_enter)

passEntry=Entry(root, width=20, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", justify='center')
passEntry.place(x=370,y=500)
passEntry.insert(0,'Enter Password')
passEntry.bind('<FocusIn>', pass_enter)

openeye=PhotoImage(file='Images/openeye.png')
eyeButton=Button(root,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=642,y=509)

frgt_btn = Button(root, text='FORGOT PASSWORD', font=("Comic Sans MS", 9, "bold"),fg='white',bg='dodger blue',height='1', width='20', command=lambda: Forgotpass_page())
frgt_btn.place(x=370,y=563)

signup_btn = Button(root, text='CREATE ACCOUNT', font=("Comic Sans MS", 9, "bold"),fg='white',bg='gold',height='1', width='20',command=lambda: createacc_page())
signup_btn.place(x=530,y=563)

start_btn = Button(root, text='PLAY', font=("Comic Sans MS", 18, "bold"),fg='white',bg='limegreen',height='1', width='20',command=lambda: Search())
start_btn.place(x=370,y=610)

developby = Label(root, text='Developed by: Team Padayon', font=("Comic Sans MS", 10, "bold"), bg='limegreen',fg='white', borderwidth=1, relief="solid", width='25')
developby.place(x=10, y=685)


def Search(arg=None):
    if userEntry.get() == '':
        ms.showerror('Oops', 'Enter Username !!')

    elif passEntry.get() == '':
        ms.showerror('Oops', 'Enter Password !!')

    else:
        global username
        username = userEntry.get()
        global password
        password = passEntry.get()

        # Making connection
        conn = sqlite3.connect('Database.db')

        # Creating cursor
        with conn:
            cursor = conn.cursor()

        # Searching for users
        find_user = ('SELECT * FROM users WHERE Username = ? AND Password = ?')
        cursor.execute(find_user, (username, password))
        results = cursor.fetchall()

        # if user then new window
        if results:
            root.destroy()
            import Main
        # if user do not exist
        else:
            ms.showerror('Oops', 'User Not Found !! Check Username and Password Again !!')

def exit_window():
    sys.exit(root.destroy())

root.mainloop()