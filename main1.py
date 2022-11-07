import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import Label
import sys


import tkinter.messagebox
# import random
# import time
# import datetime


class Window1:

    def __init__(self, master):
        # title and size++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.master = master
        self.master.title("Pharmacy Management Systems")
        # self.master.config(bg='#105DC1')
        # self.master.geometry('1600x800+0+0')
        # self.frame = Frame(self.master)
        # self.frame.grid(row=0, column=0, padx=0, pady=0)
        self.frame = Frame(self.master, width=400, height=680)
        self.frame.grid(row=0, column=0, padx=10)

        self.rframe = Frame(self.master, width=980, height=680)
        self.rframe.grid(row=0, column=1, padx=10, pady=10)
        # Buttons and Frames+++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.bgf = PhotoImage(file='background.png')
        self.label = Label(self.frame, image=self.bgf)
        self.label.grid(row=0, column=0)

        self.LabelTitle = Label(self.rframe, text="Pharmacy Management Systems", font=("Calibre", 30, 'bold'))
        self.LabelTitle.grid(row=0, column=0, pady=10)

        self.LabelTitle = Label(self.rframe, text="________OR________", font=("Calibre", 15, 'bold'))
        self.LabelTitle.grid(row=3, column=0)
        # Login information++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame1 = Frame(self.rframe, width=240, height=160, bd=10, relief='ridge')
        self.frame1.grid(row=1, column=0, pady=10)

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblUsername = Label(self.frame1, text="Username", font=("Calibre", 15, 'bold'), bd=10)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.frame1, font=("Calibre", 15, 'bold'), bd=10, textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.frame1, text="Password", font=("Calibre", 15, 'bold'), bd=10)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.frame1, font=("Calibre", 15, 'bold'), show="*", bd=10,
                                 textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1, pady=10)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame2 = Frame(self.rframe, width=240, height=160, bd=10, relief='ridge')
        self.frame2.grid(row=2, column=0, pady=10)

        self.frame3 = Frame(self.rframe, width=240, height=160, bd=10, relief='ridge')
        self.frame3.grid(row=4, column=0, pady=10)

        self.frame4 = Frame(self.rframe, width=240, height=160, bd=10, relief='ridge')
        self.frame4.grid(row=5, column=0, pady=10)

        self.btnLogin = Button(self.frame2, text="Login", font=("Calibre", 18, 'bold'),
                               command=self.Login_Sys)
        self.btnLogin.grid(row=0, column=0)

        self.btnRegistration = Button(self.frame3, text="Registration", font=("Calibre", 18, 'bold'),
                                      command=self.registration_window)
        self.btnRegistration.grid(row=0, column=0)

        self.btnExit = Button(self.frame4, text="Exit", font=("Calibre", 15, 'bold'), command=self.quit)
        self.btnExit.grid(row=1, column=0)

    # quit++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def quit(self):
        sys.exit()

    # registration window++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowR(self.newWindow)

    # Login++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Login_Sys(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        f = open('Acc.txt', 'r')
        lines = f.readline()
        for row in lines:
            if row.find(user) == -1:
                self.Login_Sys = tkinter.messagebox.showwarning("Warning!", "Account don't exist!")
            else:
                row_in = lines.index(lines)
                p = open('Pass.txt', 'r')
                passline = p.readline(row_in+1)
                pas1 = passline[row_in]
                if pas == pas1:
                    self.app = WindowR(self.master)
                else:
                    self.Login_Sys = tkinter.messagebox.showwarning("Warning!", "Incorrect password!")


class WindowR:
    def __init__(self, master):
        # title and size++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.master = master
        self.master.title("Registration Systems")
        # master.geometry('1000x800+0+0')
        # Label++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame_label = Frame(self.master, height=200, width=800)
        self.frame_label.grid(row=0, column=0, )

        self.LabelTitle = Label(self.frame_label, text="Registration Systems", font=("Calibre", 30, 'bold'))
        self.LabelTitle.grid(row=0, column=0, )
        # Button++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame1 = Frame(self.master, height=600, width=800, bd=10, relief='ridge')
        self.frame1.grid(row=1, column=0, padx=10, pady=10)

        self.Username = StringVar()
        self.Password1 = StringVar()
        self.Password2 = StringVar()

        self.lblUsername = Label(self.frame1, text="Username", font=("Calibre", 15, 'bold'), bd=10)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.frame1, font=("Calibre", 15, 'bold'), bd=10,
                                 textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1, pady=10)

        self.lblPassword1 = Label(self.frame1, text="Password", font=("Calibre", 15, 'bold'), bd=10)
        self.lblPassword1.grid(row=1, column=0)
        self.txtPassword1 = Entry(self.frame1, font=("Calibre", 15, 'bold'), show="*", bd=10,
                                  textvariable=self.Password1)
        self.txtPassword1.grid(row=1, column=1, pady=10)

        self.lblPassword2 = Label(self.frame1, text="ReEnter", font=("Calibre", 15, 'bold'), bd=10)
        self.lblPassword2.grid(row=2, column=0)
        self.txtPassword2 = Entry(self.frame1, font=("Calibre", 15, 'bold'), show="*", bd=10,
                                  textvariable=self.Password2)
        self.txtPassword2.grid(row=2, column=1, pady=10)

        # Confirm++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame2 = Frame(self.master, height=200, width=800, bd=10, relief='ridge')
        self.frame2.grid(row=3, column=0)
        self.btnConfirm = Button(self.frame2, text="Confirm", font=("Calibre", 15, 'bold'),
                                 command=self.check_ResN)
        self.btnConfirm.grid(row=0, column=0, )

    # Confirm Res++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Check name++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def check_ResN(self):
        usen = (self.Username.get())
        f = open('Acc.txt', 'r')
        lines = f.readline()
        has = 0
        for row in lines:
            if row == usen:
                has = 1
                break
        if has == 1:
            self.check_ResN = tkinter.messagebox.showwarning("Warning!", "This user name has exist!")
            self.Username.set("")
            self.Password1.set("")
            self.Password2.set("")
        else:
            f.close()
            self.check_ResP()

    # Check pass++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def check_ResP(self):
        usen = (self.Username.get())
        pas1 = (self.Password1.get())
        pas2 = (self.Password2.get())
        if pas1 == pas2:
            self.check_ResPa = tkinter.messagebox.showinfo("Registration Systems", "Congratulation")
            f = open('Acc.txt', 'a')
            f.write("\n")
            f.write(usen)
            f.close()
            p = open('Pass.txt', 'a')
            p.write("\n")
            p.write(pas1)
            p.close()
            self.master.destroy()
        else:
            self.check_ResPa = tkinter.messagebox.showerror("Registration Systems", "Re-enter your password")
            self.Password1.set("")
            self.Password2.set("")


class WindowM:
    def __init__(self, master):
        # title and size++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.master = master
        self.master.title("Manager Systems")
        # Label++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.frame_label = Frame(self.master, height=200, width=800)
        self.frame_label.grid(row=0, column=0, )

        self.LabelTitle = Label(self.frame_label, text="Manager Systems", font=("Calibre", 30, 'bold'))
        self.LabelTitle.grid(row=0, column=0, )


def main():
    root = Tk()
    app = Window1(root)


if __name__ == '__main__':
    main()
    mainloop()
