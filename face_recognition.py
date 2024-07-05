from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import time
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np




class Face_Recognition:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance System")

        title_lbl=Label(self.root,text ="FACE RECOGNITION", font=("times new roman",35,"bold"),bg ="white", fg ="green")
        title_lbl.place(x=0,y=0,width=1290,height=40)

        # 1st Image
        img_left = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\face_detector1.jpg")
        img_left= img_left.resize((650,700),Image.LANCZOS) #500 to 700
        self.photoimg_left= ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image = self.photoimg_left)
        f_lbl.place(x=0,y=40,width=650, height=610)


        # 2nd Image
        img_right = Image.open(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_right= img_right.resize((950,610),Image.LANCZOS) #500 to 700
        self.photoimg_right= ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image = self.photoimg_right)
        f_lbl.place(x=650,y=40,width=650, height=610)


        # button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg ="darkgreen", fg ="white")
        b1_1.place(x=220,y=536,width=200,height=40)



    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
        
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
   
    #  face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)  # 3 is thickness
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="********",database="DB_NAME")
                my_cursor=conn.cursor(buffered=True)

              
                my_cursor.execute("select Name from student where Student_Id="+str(id))
                n=my_cursor.fetchone()
                n=str(n)

                my_cursor.execute("select Roll_No from student where Student_Id="+str(id))
                r=my_cursor.fetchone()
                r=str(r)

                
                
                my_cursor.execute("select Department from student where Student_Id="+str(id))
                d=my_cursor.fetchone()
                d=str(d)

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i=my_cursor.fetchone()
                i=str(i)
            
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                       cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                       cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\mdtou\OneDrive\Desktop\Automatic Attendance System\Classifier.xml")
        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recoginition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
        





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()