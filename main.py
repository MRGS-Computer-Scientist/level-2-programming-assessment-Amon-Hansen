from tkinter import *

w_width = 500
w_height = 700

window = Tk()
window. geometry(str(w_width) + "x" +str(w_height))
window. title("My App")

bottom_frame = Frame(background='grey', width=w_width, height=100)
bottom_frame.pack()    

main_frame = Frame(background="orange", width=w_width, height=w_height)        
main_frame.pack()

hello_label = Label (text="Home!")
hello_label.place (x=20, y=20)

hello_label = Label (text="Sports")
hello_label.place (x=70, y=20)

hello_label = Label (text="Help")
hello_label.place (x=450, y=20)

window.mainloop() 