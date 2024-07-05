from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
import random
from time import strftime
from datetime import datetime
import mysql.connector
import os
from main import Automatic_Attendance_System
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from student import Student



def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\university.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=100,width=340,height=450)

        img1=Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=115,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=110)

        # label
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=50,y=152)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=50,y=220)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)

        # Icon
        img2=Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=534,y=253,width=25,height=25)

        img3=Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=534,y=324,width=25,height=25)
        
        # Login Button
        btn_login=Button(frame,text="Login",borderwidth=3,relief=RAISED,command=self.login,cursor="hand2",font=("times new roman",15,"bold"),bd=3,fg="white",bg="red",activeforeground="white",activebackground="red")
        btn_login.place(x=110,y=300,width=120,height=35)


        # register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=350,width=160)

        # forget Button
        forgetbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=5,y=380,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="******" and self.txtpass.get()=="******":
            messagebox.showinfo("Success","Welcome to this Project")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="********",database="DB_NAME")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Automatic_Attendance_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")
        
    # reset password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="*********",database="DB_NAME")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been Reset, Please Login with New Password",parent=self.root)
                self.root2.destroy()

    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the E-mail and Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="*********",database="DB_NAME")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Please Enter the valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)


                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favourite Food","Your Pet Name")

                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)


                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                # reset buuton
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=130,y=290)
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1400x700+0+0")

        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\un.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=20,y=50,width=470,height=550)
        
        # main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=490,y=50,width=600,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # label and entry

        # row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=240)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=220)

        # row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

       
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=240)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=220)

        
        # row 3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

       
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favourite Food","Your Pet Name")

        self.combo_security_Q.place(x=50,y=270,width=220)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=220)


        # row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

       
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=240)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm.place(x=370,y=340,width=220)

        # check button
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check, text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        # buttons
        img=Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\register-now-button1.jpg")
        img=img.resize((200,55),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\loginpng.png")
        img1=img1.resize((200,45),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=330,y=420,width=200)

    # functionn declare
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="*******",database="DB_NAME")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, Please try another E-Mail")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")
    def return_login(self):
        self.root.destroy()

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

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=60,width=220,height=160)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        b1_1.place(x=700,y=220,width=220,height=40)

        # for direct open attendace in excel
        # b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_attendance)
        # b1.place(x=700,y=60,width=220,height=160)

        # b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.open_attendance,font=("times new roman",15,"bold"),bg ="darkblue", fg ="white")
        # b1_1.place(x=700,y=220,width=220,height=40)


        
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
    # def open_attendance(self):
    #     os.startfile(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Attendance.csv")

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
                

if __name__=="__main__":
    main()