import os 
import csv
import tkinter
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import E, NO, RIGHT, W, Y, PhotoImage, ttk, messagebox, END
from Window_Maker import Window_Makers
from login import Login_Window
from utils.dbconfig import dbconfig
from utils.adder import addEntry
from utils.retriever import retrieveEntry
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA512
import random
import string
import pyperclip

import login
import Window_Maker
import hashlib

class Windows():

    def __init__(self):
        self.First()

    def First(self):
        Window = tk.CTk()
        WM = Window_Makers()


        def open_win2():
            self.Second_Window()

        def info():
            self.info_Window()

        def login():
            self.login()

        def close():
            try:
                Window.destroy()
            except tkinter.TclError:
                pass


        WM.Make_Home(Window = Window, window_title = "Password Manager", bgimg = "1stbg", text1 = "Login/Logout", text2 = "About", text3 = "Exit", text4 = "Manage Passwords", fgcolor = "#535359", hcolor = "#82828c", command1 = login, command2 = info, command3 = close, command4 = open_win2)


    def Second_Window(self):
        PM_Window = tk.CTkToplevel()

        WM = Window_Makers()


        def add():
            self.Add_Checker()

        def retrieve():
            self.Retrieve_Checker()

        def delete():
           self.Delete_Checker()

        def deswin():
            try:
                PM_Window.destroy()
            except tkinter.TclError:
                pass

            

        WM.Make_pm(Window = PM_Window, window_title = "Password Manager", bgimg = "1stbg", fgcolor = "#535359", hcolor = "#82828c", text1 = "Add password", text2 = "Retrieve password", text3 = "Delete password", text4 = "back", command1 = add, command2 = retrieve, command3 = delete, command4 = deswin)



    def Add_Checker(self):
        Add_Check_Window = tk.CTkToplevel()

        Add_Check_Window.title("Verify")
        
        window_height = 200
        window_width = 400

        screen_width = Add_Check_Window.winfo_screenwidth()
        screen_height = Add_Check_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Add_Check_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Add_Check_Window.resizable(False, False)


        Add_Check_Window['background'] = "#6f7a8f"



        MP = tk.CTkEntry(master = Add_Check_Window)
        MP.place(x = 50, y = 50, width = 300, height = 30)

        MP.insert(0, "Master Password")

        def on_enter(e):
            MP.delete(0, END)
        def on_leave(e):
            if MP.get() == "":
                MP.insert(0, "Master Password")

        MP.bind("<FocusIn>", on_enter)
        MP.bind("<FocusOut>", on_leave)

        def on_enter_press(e):
            sql_login()

        Add_Check_Window.bind("<Return>", on_enter_press)


        def sql_login():
            with open("temp1.txt", "r") as f:
                username = f.read()

            db = dbconfig()
            cursor = db.cursor()
            password = MP.get()
            with open("temp2.txt", "w") as f:
                f.write(MP.get())
            hashed_password = hashlib.sha256(password.encode()).hexdigest()


            query = '''use prodathon'''
            cursor.execute(query)
            query = "select * from  Prodathon.users where username = %s and masterkey_hash = %s"
            cursor.execute(query, [(username),(hashed_password)])
            data = cursor.fetchall()

            if data:
                deswin()
                self.Add_Window()
                

            else:
                messagebox.showerror("","Wrong Master Password")

        def deswin():
            try:
                Add_Check_Window.destroy()
            except tkinter.TclError:
                pass




        Button1 = tk.CTkButton(master = Add_Check_Window, text = "verify", text_font = ("Times New Roman", 28), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = sql_login)
        Button1.place(x = 100, y = 110, width = 200, height = 50)



        Add_Check_Window.mainloop()



    def Add_Window(self):
        AddPW_Window = tk.CTkToplevel()

        WM = Window_Makers()


        def add():
            deswin()
            self.add_details()


        def deswin():
            try:
                AddPW_Window.destroy()
            except tkinter.TclError:
                pass

            

        WM.Make_add(Window = AddPW_Window, window_title = "Add password", bgimg = "1stbg", fgcolor = "#535359", hcolor = "#82828c", text1 = "Enter Details", text2 = "Back", command1 = add, command2 = deswin)



    def add_details(self):
        Add_Details_Window = tk.CTkToplevel()

        Add_Details_Window.title("Generate Password")
        
        window_height = 600
        window_width = 900

        screen_width = Add_Details_Window.winfo_screenwidth()
        screen_height = Add_Details_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Add_Details_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Add_Details_Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs","1stbg.jpg"))
        bgmg.save(os.path.join("imgs","1stbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Add_Details_Window, image = bg_img)
        background.place(x = 0, y = 0)


###            
        sitename_Entry = tk.CTkEntry(master = Add_Details_Window)
        sitename_Entry.place(x = 460, y = 100, width = 300, height = 30)

        sitename_Entry.insert(0, "Site name")

        def on_enter(e):
            sitename_Entry.delete(0, END)
        def on_leave(e):
            if sitename_Entry.get() == "":
                sitename_Entry.insert(0, "Site name")

        sitename_Entry.bind("<FocusIn>", on_enter)
        sitename_Entry.bind("<FocusOut>", on_leave)

###
        siteurl_Entry = tk.CTkEntry(master = Add_Details_Window)
        siteurl_Entry.place(x = 460, y = 150, width = 300, height = 30)

        siteurl_Entry.insert(0, "Site URL")

        def on_enter(e):
            siteurl_Entry.delete(0, END)
        def on_leave(e):
            if siteurl_Entry.get() == "":
                siteurl_Entry.insert(0, "Site URL")

        siteurl_Entry.bind("<FocusIn>", on_enter)
        siteurl_Entry.bind("<FocusOut>", on_leave)

###
        email_Entry = tk.CTkEntry(master = Add_Details_Window)
        email_Entry.place(x = 460, y = 200, width = 300, height = 30)

        email_Entry.insert(0, "Email")

        def on_enter(e):
            email_Entry.delete(0, END)
        def on_leave(e):
            if email_Entry.get() == "":
                email_Entry.insert(0, "Email")

        email_Entry.bind("<FocusIn>", on_enter)
        email_Entry.bind("<FocusOut>", on_leave)

###
        siteusername_Entry = tk.CTkEntry(master = Add_Details_Window)
        siteusername_Entry.place(x = 460, y = 250, width = 300, height = 30)

        siteusername_Entry.insert(0, "Site Username")

        def on_enter(e):
            siteusername_Entry.delete(0, END)
        def on_leave(e):
            if siteusername_Entry.get() == "":
                siteusername_Entry.insert(0, "Site Username")

        siteusername_Entry.bind("<FocusIn>", on_enter)
        siteusername_Entry.bind("<FocusOut>", on_leave)

###   

        def deswin():
            try:
                Add_Details_Window.destroy()
            except tkinter.TclError:
                pass

        with open("temp2.txt", "r") as f:
            MP = f.read()
        with open("temp1.txt", "r") as g:
            username = g.read()
        db = dbconfig()
        cursor = db.cursor()
        query = "select device_secret from Prodathon.users where username = '{}';".format(username)
        cursor.execute(query)
        data = cursor.fetchall()[0][0]

        def generate():
            addEntry(MP, data, sitename_Entry.get(), siteurl_Entry.get(), email_Entry.get(), siteusername_Entry.get(), username)
            messagebox.showinfo("Success", "Seccessfully added password to database")
            deswin()

        Button1 = tk.CTkButton(master = Add_Details_Window, text = "Generate Password", text_font = ("Times New Roman", 30), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = generate)
        Button1.place(x = 441, y = 420, width = 350, height = 70)

        img = Image.open(os.path.join("imgs","back_button.png"))
        img = img.resize((50,50), resample = 0)
        button_img = ImageTk.PhotoImage(img)       

        Button2 = tk.CTkButton(master = Add_Details_Window, text = "back", text_color = "black", text_font = ("Times New Roman", 14), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = deswin, image = button_img, compound = "left")
        Button2.place(x = 10, y = 10, width = 121, height = 50)


        Add_Details_Window.mainloop()





    def Retrieve_Checker(self):
        Retrieve_Check_Window = tk.CTkToplevel()

        Retrieve_Check_Window.title("Verify")
        
        window_height = 200
        window_width = 400

        screen_width = Retrieve_Check_Window.winfo_screenwidth()
        screen_height = Retrieve_Check_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Retrieve_Check_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Retrieve_Check_Window.resizable(False, False)


        Retrieve_Check_Window['background'] = "#6f7a8f"



        MP = tk.CTkEntry(master = Retrieve_Check_Window)
        MP.place(x = 50, y = 50, width = 300, height = 30)

        MP.insert(0, "Master Password")

        def on_enter(e):
            MP.delete(0, END)
        def on_leave(e):
            if MP.get() == "":
                MP.insert(0, "Master Password")

        MP.bind("<FocusIn>", on_enter)
        MP.bind("<FocusOut>", on_leave)

        def on_enter_press(e):
            sql_login()

        Retrieve_Check_Window.bind("<Return>", on_enter_press)


        def sql_login():
            with open("temp1.txt", "r") as f:
                username = f.read()

            db = dbconfig()
            cursor = db.cursor()
            password = MP.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()


            query = '''use prodathon'''
            cursor.execute(query)
            query = "select * from  Prodathon.users where username = %s and masterkey_hash = %s"
            cursor.execute(query, [(username),(hashed_password)])
            data = cursor.fetchall()

            if data:
                deswin()
                self.Retrieve_Window()
                

            else:
                messagebox.showerror("","Wrong Master Password")
                

        def deswin():
            try:
                Retrieve_Check_Window.destroy()
            except tkinter.TclError:
                pass




        Button1 = tk.CTkButton(master = Retrieve_Check_Window, text = "verify", text_font = ("Times New Roman", 28), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = sql_login)
        Button1.place(x = 100, y = 110, width = 200, height = 50)



        Retrieve_Check_Window.mainloop()



    def Retrieve_Window(self):
        RetPW_Window = tk.CTkToplevel()

        WM = Window_Makers()


        def retrieve():
            deswin()
            self.ret_details()


        def deswin():
            try:
                RetPW_Window.destroy()
            except tkinter.TclError:
                pass

            

        WM.Make_ret(Window = RetPW_Window, window_title = "Retrieve password", bgimg = "1stbg", fgcolor = "#535359", hcolor = "#82828c", text1 = "Retrieve", text2 = "Back", command1 = retrieve, command2 = deswin)



    def ret_details(self):
        Ret_Details_Window = tk.CTkToplevel()

        Ret_Details_Window.title("Retrieve Password")
        
        window_height = 600
        window_width = 900

        screen_width = Ret_Details_Window.winfo_screenwidth()
        screen_height = Ret_Details_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Ret_Details_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Ret_Details_Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs","1stbg.jpg"))
        bgmg.save(os.path.join("imgs","1stbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Ret_Details_Window, image = bg_img)
        background.place(x = 0, y = 0)


###            
        sitename_Entry = tk.CTkEntry(master = Ret_Details_Window)
        sitename_Entry.place(x = 460, y = 100, width = 300, height = 30)

        sitename_Entry.insert(0, "Site name")

        def on_enter(e):
            sitename_Entry.delete(0, END)
        def on_leave(e):
            if sitename_Entry.get() == "":
                sitename_Entry.insert(0, "Site name")

        sitename_Entry.bind("<FocusIn>", on_enter)
        sitename_Entry.bind("<FocusOut>", on_leave)

###
        email_Entry = tk.CTkEntry(master = Ret_Details_Window)
        email_Entry.place(x = 460, y = 150, width = 300, height = 30)

        email_Entry.insert(0, "Email")

        def on_enter(e):
            email_Entry.delete(0, END)
        def on_leave(e):
            if email_Entry.get() == "":
                email_Entry.insert(0, "Email")

        email_Entry.bind("<FocusIn>", on_enter)
        email_Entry.bind("<FocusOut>", on_leave)


        def deswin():
            try:
                Ret_Details_Window.destroy()
            except tkinter.TclError:
                pass

        with open("temp2.txt", "r") as f:
            MP = f.read()
        with open("temp1.txt", "r") as g:
            username = g.read()
        db = dbconfig()
        cursor = db.cursor()
        query = "select device_secret from Prodathon.users where username = '{}';".format(username)
        cursor.execute(query)
        data = cursor.fetchall()[0][0]

        def retrieve():
            pw = retrieveEntry(MP, data, sitename_Entry.get(), email_Entry.get(), username)
            if pw == -1:
                messagebox.showerror("Not found", "No such entry")
                deswin()
            else:
                messagebox.showinfo("Retrieved","The password has been successfully copied")
                pyperclip.copy(pw.decode())
                deswin()

        Button1 = tk.CTkButton(master = Ret_Details_Window, text = "Retrieve Password", text_font = ("Times New Roman", 30), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = retrieve)
        Button1.place(x = 441, y = 420, width = 350, height = 70)

        img = Image.open(os.path.join("imgs","back_button.png"))
        img = img.resize((50,50), resample = 0)
        button_img = ImageTk.PhotoImage(img)       

        Button2 = tk.CTkButton(master = Ret_Details_Window, text = "back", text_color = "black", text_font = ("Times New Roman", 14), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = deswin, image = button_img, compound = "left")
        Button2.place(x = 10, y = 10, width = 121, height = 50)


        Ret_Details_Window.mainloop()





    def Delete_Checker(self):
        Delete_Check_Window = tk.CTkToplevel()

        Delete_Check_Window.title("Verify")
        
        window_height = 200
        window_width = 400

        screen_width = Delete_Check_Window.winfo_screenwidth()
        screen_height = Delete_Check_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Delete_Check_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Delete_Check_Window.resizable(False, False)


        Delete_Check_Window['background'] = "#6f7a8f"



        MP = tk.CTkEntry(master = Delete_Check_Window)
        MP.place(x = 50, y = 50, width = 300, height = 30)

        MP.insert(0, "Master Password")

        def on_enter(e):
            MP.delete(0, END)
        def on_leave(e):
            if MP.get() == "":
                MP.insert(0, "Master Password")

        MP.bind("<FocusIn>", on_enter)
        MP.bind("<FocusOut>", on_leave)

        def on_enter_press(e):
            sql_login()

        Delete_Check_Window.bind("<Return>", on_enter_press)


        def sql_login():
            with open("temp1.txt", "r") as f:
                username = f.read()

            db = dbconfig()
            cursor = db.cursor()
            password = MP.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()


            query = '''use prodathon'''
            cursor.execute(query)
            query = "select * from  Prodathon.users where username = %s and masterkey_hash = %s"
            cursor.execute(query, [(username),(hashed_password)])
            data = cursor.fetchall()

            if data:
                deswin()
                self.Delete_Window()
                

            else:
                messagebox.showerror("","Wrong Master Password")

        def deswin():
            try:
                Delete_Check_Window.destroy()
            except tkinter.TclError:
                pass




        Button1 = tk.CTkButton(master = Delete_Check_Window, text = "verify", text_font = ("Times New Roman", 28), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = sql_login)
        Button1.place(x = 100, y = 110, width = 200, height = 50)



        Delete_Check_Window.mainloop()



    def Delete_Window(self):
        delPW_Window = tk.CTkToplevel()

        WM = Window_Makers()


        def dell():
            deswin()
            self.del_details()

        def deswin():
            try:
                delPW_Window.destroy()
            except tkinter.TclError:
                pass

            

        WM.Make_del(Window = delPW_Window, window_title = "Delete password", bgimg = "1stbg", fgcolor = "#535359", hcolor = "#82828c", text1 = "Delete", text2 = "Back", command1 = dell, command2 = deswin)



    def del_details(self):
        del_Details_Window = tk.CTkToplevel()

        del_Details_Window.title("Delete Password")
        
        window_height = 600
        window_width = 900

        screen_width = del_Details_Window.winfo_screenwidth()
        screen_height = del_Details_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        del_Details_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        del_Details_Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs","1stbg.jpg"))
        bgmg.save(os.path.join("imgs","1stbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = del_Details_Window, image = bg_img)
        background.place(x = 0, y = 0)


###            
        sitename_Entry = tk.CTkEntry(master = del_Details_Window)
        sitename_Entry.place(x = 460, y = 100, width = 300, height = 30)

        sitename_Entry.insert(0, "Site name")

        def on_enter(e):
            sitename_Entry.delete(0, END)
        def on_leave(e):
            if sitename_Entry.get() == "":
                sitename_Entry.insert(0, "Site name")

        sitename_Entry.bind("<FocusIn>", on_enter)
        sitename_Entry.bind("<FocusOut>", on_leave)

###
        email_Entry = tk.CTkEntry(master = del_Details_Window)
        email_Entry.place(x = 460, y = 150, width = 300, height = 30)

        email_Entry.insert(0, "Email")

        def on_enter(e):
            email_Entry.delete(0, END)
        def on_leave(e):
            if email_Entry.get() == "":
                email_Entry.insert(0, "Email")

        email_Entry.bind("<FocusIn>", on_enter)
        email_Entry.bind("<FocusOut>", on_leave)


        def deswin():
            try:
                del_Details_Window.destroy()
            except tkinter.TclError:
                pass

        with open("temp1.txt", "r") as f:
            username = f.read()

        def delete():
            db = dbconfig()
            cursor = db.cursor()
            query = "delete from prodathon." + username + " where sitename = '{}' and email = '{}';".format(sitename_Entry.get(), email_Entry.get())
            cursor.execute(query)
            messagebox.showinfo("deleted", "record has been deleted")

            db.commit()
            db.close()
            deswin()

        Button1 = tk.CTkButton(master = del_Details_Window, text = "Delete Password", text_font = ("Times New Roman", 30), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = delete)
        Button1.place(x = 441, y = 420, width = 350, height = 70)

        img = Image.open(os.path.join("imgs","back_button.png"))
        img = img.resize((50,50), resample = 0)
        button_img = ImageTk.PhotoImage(img)       

        Button2 = tk.CTkButton(master = del_Details_Window, text = "back", text_color = "black", text_font = ("Times New Roman", 14), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = deswin, image = button_img, compound = "left")
        Button2.place(x = 10, y = 10, width = 121, height = 50)


        del_Details_Window.mainloop()




    def info_Window(self):
        Window = tk.CTkToplevel()
        WM = Window_Makers()


        WM.Info(Window = Window, window_title = "About", bgimg = "1stbg", hcolor = "#6f7a8f")


    def login(self):
        LWIN = tk.CTkToplevel()
        WM = Login_Window()
        WM.Make_Win(Window = LWIN, window_title = "Login", bgimg = "1stbg")




Window = Windows()