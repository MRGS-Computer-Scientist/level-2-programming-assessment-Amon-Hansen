from tkinter import *
from app_settings import *

class App():

    def _init_(self):
        w_width = 500
        w_height = 700

        bg_color = "#E7DFF"

        window = Tk()
        window. geometry(str(w_width) + "x" +str(w_height))
        window. title("My App")

        top_frame = Frame(background='black', width=w_width, height=100)
        top_frame.pack()    

        main_frame = Frame(background="orange", width=w_width, height=w_height)        
        main_frame.pack()

        hello_label = Label (text="Home!")
        hello_label.place (x=20, y=20)

        hello_label = Label (text="Sports")
        hello_label.place (x=70, y=20)

        hello_label = Label (text="Help")
        hello_label.place (x=450, y=20)

        home_button

        window.mainloop() 
