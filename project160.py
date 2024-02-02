from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open ("open_file.png")) 
save_img = ImageTk.PhotoImage(Image.open ("save_file.png")) 
run_img = ImageTk.PhotoImage(Image.open ("run.png")) 

label_file_name = Label(root, text="file Name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)

input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)

my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""
def openfile():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    textfile = filedialog.askopenfilename(title = " Open Text File",
                                          filetypes = (("text files", "*.txt"),))
    print (text_file)
    name = os.path.basename(text_file)
    formated_name = name.split(".")[0]
    inputfilename.insert(END, formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragarph = text_file.read()
    my_text.insert(END,paragarph)
    textfile.close()


open_button=Button(root,image = open_img, text= "openfile", command=openfile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

root.mainloop()