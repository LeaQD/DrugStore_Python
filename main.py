from fileinput import close
from logging import root
from tkinter import *
from tkinter import Label
import sys

# import tkinter.messagebox
# import random
# import time
# import datetime


class Window1:

    def __init__(self, master):
        # title and size+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.master = master
        self.master.title("Drug Store Management System")
        self.master.geometry('1400x700+0+0')
        self.frame = Frame(self.master)
        self.frame.grid()

        # Buttons and Frames+++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # self.bg = PhotoImage(file='D:/New folder/bgggg.png')
        # self.label = Label(master, image=self.bg)
        # self.label.place(x=0, y=0)

        self.LabelTitle = Label(self.frame, text="Drug Store Management System",bg="Blue", font=("Calibre", 40, 'bold'))
        self.LabelTitle.grid(row=0, column=0, pady=0)

        self.LabelTitle = Label(self.frame, text="________OR________", font=("Calibre", 20, 'bold'))
        self.LabelTitle.grid(row=3, column=0, padx=600, pady=0)
        # Login information++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame1 = Frame(self.frame, width=600, height=200, bd=10, relief='ridge')
        self.frame1.grid(row=1, column=0, padx=400, pady=10)

        self.lblUsername = Label(self.frame1, text="Username", font=("Calibre", 15, 'bold'), bd=10)
        self.lblUsername.grid(row=0, column=0, pady=10)
        self.txtUsername = Entry(self.frame1, font=("Calibre", 15, 'bold'), bd=10,
                                 )
        self.txtUsername.grid(row=0, column=1, pady=10)

        self.lblPassword = Label(self.frame1, text="Password", font=("Calibre", 15, 'bold'), bd=10)
        self.lblPassword.grid(row=1, column=0, pady=10)
        self.txtPassword = Entry(self.frame1, font=("Calibre", 15, 'bold'), bd=10, show="*")
        self.txtPassword.grid(row=1, column=1, pady=10)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame2 = Frame(self.frame, width=600, height=200, bd=10, relief='ridge')
        self.frame2.grid(row=2, column=0, padx=650, pady=10)

        self.frame3 = Frame(self.frame, width=600, height=200, bd=10, relief='ridge')
        self.frame3.grid(row=4, column=0, padx=650, pady=10)

        self.frame4 = Frame(self.frame, width=600, height=200, bd=10, relief='ridge')
        self.frame4.grid(row=5, column=0, padx=650, pady=10)

        self.btnLogin = Button(self.frame2, text="Login", font=("Calibre", 20, 'bold'))
        self.btnLogin.grid(row=0, column=0)

        self.btnRegistration = Button(self.frame3, text="Registration", font=("Calibre", 20, 'bold'), command=self.registration_window)
        self.btnRegistration.grid(row=0, column=0)

        self.btnExit = Button(self.frame4, text="Exit", font=("Calibre", 20, 'bold'),command=self.quit)
        self.btnExit.grid(row=1, column=0)
    # registration windown
    def quit(self) :
        sys.exit()
    def registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowR()


class WindowR:
    def __int__(self, master):
        self.master = master
        self.master.title("Registration Systems")
        self.master.geometry('1400x700+0+0')
        self.frame = Frame(self.master)
        self.frame.grid()




class WindowL:
    def __int__(self, master):
        self.master = master
        self.master.title("Login Systems")
        self.master.geometry('1400x700+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


def main():
    root = Tk()
    app = Window1(root)


if __name__ == '__main__':
    main()
    mainloop()
