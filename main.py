from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help





class Automatic_Attendance_System:
    
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance System")


        #first image
        img = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\BestFacialRecognition.jpg")
        img = img.resize((500,130),Image.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=0,y=0,width=400, height=130)

        #second image
        img1 = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\facialrecognition.png")
        img1= img1.resize((500,130),Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=400,y=0,width=470, height=130)

        #third image
        img2 = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\images.jpg")
        img2= img2.resize((500,130),Image.LANCZOS) #500 to 700
        self.photoimg2= ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=870,y=0,width=470, height=130)
        
    
        
        #bg image
        img3 = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\wp2551980.jpg")
        img3= img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image= self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=550)

        title_lbl=Label(bg_img,text ="AUTOMATIC ATTENDANCE SYSTEM", font=("times new roman",35,"bold"),bg ="white", fg ="red")
        title_lbl.place(x=0,y=0,width=1290,height=45)

        # Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time) #ms
        lbl = Label(title_lbl,font=('times new romain',14,'bold'),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=150,height=40)
        time()

        #student button
        img4= Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\gettyimages-1022573162.jpg")
        img4= img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=60,width=220,height=160)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=100,y=220,width=220,height=40)

        #Detect face button
        img5= Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\face_detector1.jpg")
        img5= img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=60,width=220,height=160)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=400,y=220,width=220,height=40)


        #Attendance face button
        img6= Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\report.jpg")
        img6= img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        # b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        # b1.place(x=700,y=60,width=220,height=160)

        # b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        # b1_1.place(x=700,y=220,width=220,height=40)

        # for direct open attendace in excel
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_attendance)
        b1.place(x=700,y=60,width=220,height=160)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.open_attendance,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=700,y=220,width=220,height=40)


        
        #Help face button
        img7= Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7= img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=60,width=220,height=160)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=1000,y=220,width=220,height=40)

        #Train face button
        img8= Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\Train.jpg")
        img8= img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=300,width=220,height=160)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=100,y=460,width=220,height=40)

        #Photos face button
        img9= Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\opencv_face_reco_more_data.jpg")
        img9= img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=220,height=160)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=400,y=460,width=220,height=40)


        #Develepor face button
        img10= Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\Team-Management-Software-Development.jpg")
        img10= img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=300,width=220,height=160)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=700,y=460,width=220,height=40)

        #Exit face button
        img11= Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\exit.jpg")
        img11= img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=300,width=220,height=160)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=1000,y=460,width=220,height=40)

    
    def open_img(self):
        os.startfile(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\data")

    # for direct open attendace in excel
    def open_attendance(self):
        os.startfile(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Attendance.csv")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Automatic Attendance System","Are You Sure To Exit this Project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
    # Function buttons
    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app= Student(self.new_window)


    def train_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Train(self.new_window)


    
    def face_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Attendance(self.new_window)

    def developer_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Developer(self.new_window)
    
    def help_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Help(self.new_window)

    # def login_window(self):
    #     self.new_window= Toplevel(self.root)
    #     self.app= Login_window(self.new_window)




        

if __name__ == "__main__":
    root=Tk()
    obj=Automatic_Attendance_System(root)
    root.mainloop()