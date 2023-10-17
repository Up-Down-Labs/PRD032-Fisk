import os
import tkinter 
from PIL import Image, ImageTk
from tkinter import PhotoImage, ttk, messagebox, END, INSERT

import customtkinter as tk


PW = None


class Window_Makers():

    def __init__(self):
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("dark-blue")



    def Make_Home(self, Window, window_title, bgimg, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4):


        def home_buttons(Window, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4):
            Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
            Button1.place(x = 510, y = 170, width = 350, height = 70)

            Button2 = tk.CTkButton(master = Window, text = text2, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2)
            Button2.place(x = 510, y = 450, width = 350, height = 70)

            Button4 = tk.CTkButton(master = Window, text = text4, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor, command = command4)
            Button4.place(x = 510, y = 310, width = 350, height = 70)


            img = Image.open(os.path.join("imgs","back_button.png"))
            img = img.resize((50,50), resample = 0)
            button_img = ImageTk.PhotoImage(img)       

            Button3 = tk.CTkButton(master = Window, text = text3, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command3, image = button_img, compound = "left")
            Button3.place(x = 10, y = 10, width = 121, height = 50)


        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        home_buttons(Window, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4)

        Window.mainloop()




    def Make_pm(self, Window, window_title, bgimg, fgcolor, hcolor, text1, text2, text3, text4,  command1, command2, command3, command4):
        
        def pm_buttons(Window, fgcolor, hcolor, text1, text2, text3, text4,  command1, command2, command3, command4):
            Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
            Button1.place(x = 510, y = 170, width = 350, height = 70)

            Button2 = tk.CTkButton(master = Window, text = text2, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2)
            Button2.place(x = 510, y = 310, width = 350, height = 70)

            Button3 = tk.CTkButton(master = Window, text = text3, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor, command = command3)
            Button3.place(x = 510, y = 450, width = 350, height = 70)

            img = Image.open(os.path.join("imgs","back_button.png"))
            img = img.resize((50,50), resample = 0)
            button_img = ImageTk.PhotoImage(img)       

            Button4 = tk.CTkButton(master = Window, text = text4, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command4, image = button_img, compound = "left")
            Button4.place(x = 10, y = 10, width = 121, height = 50)



        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        pm_buttons(Window,fgcolor, hcolor, text1, text2, text3, text4, command1, command2, command3, command4)

        Window.mainloop()





    def Make_add(self, Window, window_title, bgimg, fgcolor, hcolor, text1, text2, command1, command2):
        
        def add_widgets(Window, fgcolor, hcolor, text1, text2, command1, command2):
            data = "In order to add a password, please enter your \nrespective site name, site url, site username and email address that was \nused to register on the site"
            L = tk.CTkLabel(master = Window, text = data, text_font = ("Calibri", 20), bg_color = hcolor)
            L.place(x = 0, y = 0, width = 900, height = 600)

            Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
            Button1.place(x = 441, y = 420, width = 350, height = 70)

            img = Image.open(os.path.join("imgs","back_button.png"))
            img = img.resize((50,50), resample = 0)
            button_img = ImageTk.PhotoImage(img)       

            Button2 = tk.CTkButton(master = Window, text = text2, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2, image = button_img, compound = "left")
            Button2.place(x = 10, y = 10, width = 121, height = 50)




        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        add_widgets(Window,fgcolor, hcolor, text1, text2, command1, command2)

        Window.mainloop()




    def Make_ret(self, Window, window_title, bgimg, fgcolor, hcolor, text1, text2, command1, command2):
        
        def ret_widgets(Window, fgcolor, hcolor, text1, text2, command1, command2):
            data = "In order to retrieve a password, please enter your respective site name \nand email address that was used to register on the site"
            L = tk.CTkLabel(master = Window, text = data, text_font = ("Calibri", 20), bg_color = hcolor)
            L.place(x = 0, y = 0, width = 900, height = 600)

            Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
            Button1.place(x = 441, y = 420, width = 350, height = 70)

            img = Image.open(os.path.join("imgs","back_button.png"))
            img = img.resize((50,50), resample = 0)
            button_img = ImageTk.PhotoImage(img)       

            Button2 = tk.CTkButton(master = Window, text = text2, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2, image = button_img, compound = "left")
            Button2.place(x = 10, y = 10, width = 121, height = 50)

        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        ret_widgets(Window,fgcolor, hcolor, text1, text2, command1, command2)

        Window.mainloop()



    def Make_del(self, Window, window_title, bgimg, fgcolor, hcolor, text1, text2, command1, command2):
        
        def del_widgets(Window, fgcolor, hcolor, text1, text2, command1, command2):
            data = "In order to delete a password, please enter your respective site name \nand email address that was used to register on the site"
            L = tk.CTkLabel(master = Window, text = data, text_font = ("Calibri", 20), bg_color = hcolor)
            L.place(x = 0, y = 0, width = 900, height = 600)


            Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
            Button1.place(x = 441, y = 420, width = 350, height = 70)

            img = Image.open(os.path.join("imgs","back_button.png"))
            img = img.resize((50,50), resample = 0)
            button_img = ImageTk.PhotoImage(img)       

            Button2 = tk.CTkButton(master = Window, text = text2, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2, image = button_img, compound = "left")
            Button2.place(x = 10, y = 10, width = 121, height = 50)

        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        del_widgets(Window,fgcolor, hcolor, text1, text2, command1, command2)

        Window.mainloop()


    def Info(self, Window, window_title, bgimg, hcolor):
        
        def Info_widgets(Window, hcolor):
            with open ("info.txt", "r") as f:
                data = f.read()

            L = tk.CTkLabel(master = Window, text = data, text_font = ("Calibri", 30), bg_color = hcolor)
            L.place(x = 0, y = 0)

        Window.title(window_title)
        
        window_height = 400
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        Info_widgets(Window, hcolor)

        Window.mainloop()
