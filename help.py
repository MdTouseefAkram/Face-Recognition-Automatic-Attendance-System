from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2





class Help:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance System")

        title_lbl=Label(self.root,text ="HELP DESK", font=("times new roman",35,"bold"),bg ="white", fg ="blue")
        title_lbl.place(x=0,y=0,width=1290,height=45)

        img_top = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top= img_top.resize((1290,625),Image.LANCZOS) #500 to 700
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1290, height=635)

        dev_label = Label(f_lbl,text="E-Mail: mdtouseefakram12769@gmail.com",font=("times new roman",13,"bold"))
        dev_label.place(x=480,y=200)

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()