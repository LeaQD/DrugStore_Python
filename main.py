import sys
from tkinter import *
from tkinter import ttk, Label


# import tkinter.messagebox
# import random
# import time
# import datetime


class Window1:

    def __init__(self, master):
        # title and size+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.master = master
        self.master.title("Pharmacy Management Systems")
        # self.master.config(bg='#105DC1')
        # self.master.geometry('1400x700+0+0')
        # self.frame = Frame(self.master)
        # self.frame.grid(row=0, column=0, padx=0, pady=0)
        self.frame = Frame(self.master, width=400, height=680)
        self.frame.grid(row=0, column=0, padx=10)

        self.rframe = Frame(self.master, width=980, height=680)
        self.rframe.grid(row=0, column=1, padx=10, pady=10)
        # Buttons and Frames+++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.bgf = PhotoImage(file='D:\GitHub\PharmacyManagementSystems_Python\gggg.png')
        self.label = Label(self.frame, image=self.bgf)
        self.label.grid(row=0, column=0)

        self.LabelTitle = Label(self.rframe, text="Pharmacy Management Systems", font=("Calibre", 30, 'bold'))
        self.LabelTitle.grid(row=0, column=0, pady=10)

        self.LabelTitle = Label(self.rframe, text="________OR________", font=("Calibre", 15, 'bold'))
        self.LabelTitle.grid(row=3, column=0)
        # Login information++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame1 = Frame(self.rframe, width=240, height=160, bd=10, relief='ridge')
        self.frame1.grid(row=1, column=0, pady=10)

        self.lblUsername = Label(self.frame1, text="Username", font=("Calibre", 15, 'bold'), bd=10)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.frame1, font=("Calibre", 15, 'bold'), bd=10)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.frame1, text="Password", font=("Calibre", 15, 'bold'), bd=10)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.frame1, font=("Calibre", 15, 'bold'), show="*", bd=10)
        self.txtPassword.grid(row=1, column=1, pady=10)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame2 = Frame(self.rframe, width=240, height=160, bd=10, relief='ridge')
        self.frame2.grid(row=2, column=0, pady=10)

        self.frame3 = Frame(self.rframe, width=240, height=160, bd=10, relief='ridge')
        self.frame3.grid(row=4, column=0, pady=10)

        self.frame4 = Frame(self.rframe, width=240, height=160, bd=10, relief='ridge')
        self.frame4.grid(row=5, column=0, pady=10)

        self.btnLogin = Button(self.frame2, text="Login", font=("Calibre", 18, 'bold'))
        self.btnLogin.grid(row=0, column=0)

        self.btnRegistration = Button(self.frame3, text="Registration", font=("Calibre", 18, 'bold'), command=self.registration_window)
        self.btnRegistration.grid(row=0, column=0)

        self.btnExit = Button(self.frame4, text="Exit", font=("Calibre", 15, 'bold'), command=self.quit)
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
