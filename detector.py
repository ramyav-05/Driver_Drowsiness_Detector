import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('MTC PROJECT')
frame.config(background='DodgerBlue3')
label = Label(frame, text="Drowsiness Alert",bg='DodgerBlue3',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="E:\Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)
root.resizable(True,True)
photo= PhotoImage(file="E:\Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\mtc.png")
root.iconphoto(False,photo)


def hel():
   tkinter.messagebox.showinfo("Software & Packages","\n Python 3.8.6\n Numpy\n Opencv\n Tkinter \n Pygame ")

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Abhyudaya Ram\n2. Amshula M S \n3. Manoj B R \n4.Prathik U H\n5. Ramya V")


def anotherWin():
   tkinter.messagebox.showinfo("Overview",'◆This proposed system works by monitoring the eyes of the driver . If the driver''s eyes remain' 
'closed for more than a certain period of time, the driver is said to be drowsy and an alarm is produced.\n' 
'◆The programming for this is done in Python using Open CV, the Haar Cascade library for the detection of facial features and UI is done using Tkinter')  

menu = Menu(root,relief=SUNKEN)
root.config(menu=menu)

subm1 = Menu(menu,fg='firebrick1',bg='white',activebackground='Cornflower Blue',relief=SUNKEN)
menu.add_cascade(label="Info",menu=subm1)
subm1.add_command(label="Software Info",command=hel)

subm2 = Menu(menu,fg='firebrick1',bg='white',activebackground='Cornflower Blue',relief=SUNKEN)
menu.add_cascade(label="Project Info",menu=subm2)
subm2.add_command(label="Overview",command=anotherWin)
subm2.add_command(label="Team",command=Contri)



def exitt():
   exit()

  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   

def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'FACE',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   capture.release()
   cv2.destroyAllWindows()
def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'FACE',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.9)
   alert.play()   
   
def blink():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
  
   capture.release()
   cv2.destroyAllWindows()

   


but1=Button(frame,padx=5,pady=5,width=30,bg='RoyalBlue3',fg='white',relief=SUNKEN,command=webdet,text='FACE & EYES DETECTION',font=('helvetica 15 bold'))
but1.place(x=45,y=220)


but2=Button(frame,padx=5,pady=5,width=30,bg='RoyalBlue3',fg='white',relief=SUNKEN,command=blink,text='DRIVER BLINK ALERT',font=('helvetica 15 bold'))
but2.place(x=45,y=320)

but3=Button(frame,padx=2,pady=3,width=5,height=1,bg='pink',fg='black',relief=FLAT,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but3.place(x=212,y=432)

root.resizable(True,True)
root.mainloop()

