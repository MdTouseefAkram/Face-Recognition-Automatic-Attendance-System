from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance System")

        title_lbl=Label(self.root,text ="DEVELOPER", font=("times new roman",35,"bold"),bg ="white", fg ="blue")
        title_lbl.place(x=0,y=0,width=1290,height=45)

        img_top = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\dev.jpg")
        img_top= img_top.resize((1290,625),Image.LANCZOS) #500 to 700
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1290, height=635)

        # frame
        main_frame = Frame(f_lbl,bd=2)
        main_frame.place(x=900,y=50,width=360,height=450)

        img_top1 = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\photo.jpg")
        img_top1= img_top1.resize((150,150),Image.LANCZOS) #500 to 700
        self.photoimg_top1= ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image = self.photoimg_top1)
        f_lbl.place(x=200,y=0,width=160,height=140)

        # Developer info
        dev_label = Label(main_frame,text="Hello! My name is Touseef",font=("times new roman",13,"bold"))
        dev_label.place(x=0,y=20)

        dev_label = Label(main_frame,text="I am Full Stack Developer",font=("times new roman",22,"bold"))
        dev_label.place(x=20,y=170)

        img2 = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2= img2.resize((650,390),Image.LANCZOS) #500 to 700
        self.photoimg2= ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image = self.photoimg2)
        f_lbl.place(x=0,y=210,width=500, height=290)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()