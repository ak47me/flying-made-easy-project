from gtts import gTTS
from playsound import playsound
from datetime import datetime
import random
import cv2
import face_recognition
from tkinter import *
import tkinter
import tkinter as tk
from tkinter import Tk,StringVar,ttk
from PIL import ImageTk,Image
#pythonsql connection
import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",password="0504456370",database="airport1")
mycursor=mycon.cursor()

#intro
print('''
                  ___________                                        
                       |                                              
                  _   _|_   _                                        
                 (_)-/   \-(_)                                       
    _               /\___/\                 _                
   (_)_____________( ( . ) )_______________(_)           
                    \_____/
                              ''')
print('Welcome to AbuDhabi International airport'.center(50,'*'))
print('مطار أبو ظبي الدولي'.center(50,'*'))
#time of the day
currenttime=datetime.now()            
hr=int(currenttime.strftime('%H'))   #converts string date to int which is used in conditional statements to know the time of the day
if 0<=hr<12:
       greetings='Good Morning! '
if 12<=hr<=16:
       greetings='Good Afternoon! '
if 16<=hr<24:
       greetings='Good Evening! '

#intro speech
mytext = 'Welcome to AbuDhabi International Airport'
mytext1="مطار أبو ظبي الدولي"
language1 = 'en-us'
speech = gTTS(text=greetings+mytext, lang=language1, slow=False)      #Syntax of gtts function 
speech.save("welcome.mp3") #used to store the voice in a mp3 file
playsound('welcome.mp3') #used to play the mp3 file
language2 = 'ar'
speech = gTTS(text=mytext1, lang=language2, slow=False)
speech.save("welcome1.mp3")
playsound('welcome1.mp3')


#main prog


def one():
    '''mycursor.execute("create table oneway(Name varchar(50),Age int,Phno int,Dep_airport varchar(50),Arr_airport varchar(50),Dep_date varchar,flight varchar(30),Acc_no int)")'''
    t="enter how many tickets do you want"
    speech = gTTS(text=t, lang='en-us', slow=False)
    speech.save("how.mp3")
    playsound('how.mp3')
    
    no=int(input("enter how many tickets do you want"))
    th="enter all the personal information ahead"
    speech = gTTS(text=th, lang='en-us', slow=False)
    speech.save("w.mp3")
    playsound('w.mp3')
    c2=0
    for i in range(no):
        
        name=(input("ENTER NAME :"))
        age=int(input('ENTER AGE:'))
        phno=int(input("ENTER PHONE NO :"))
        From=input("ENTER DEPARTURE AIRPORT :")
        To=input("ENTER ARRIVAL AIRPORT:")
        Dep_date=input("ENTER DEPARTURE DATE")
        b=['Air India','Etihad','Emirates','Air India Express','Air Arabia','Qatar Airways']
        flight=random.choice(b)
        acc=random.randint(100000,700000)
        
        a="insert into oneway(Name,Age,Phno,dep_airport,arr_airport,Dep_date,flight,Acc_no) values('{}',{},{},'{}','{}','{}','{}',{})".format(name,age,phno,From,To,Dep_date,flight,acc)

        mycursor.execute(a)
        mycon.commit()
        if age>16:
               c2+=500
        elif age>2 and age<16:
               c2+=350
        else:
               c2+=0
       
    cost1="the total ticket cost is {}".format(c2)
    speech = gTTS(text=cost1, lang='en-us', slow=False)
    speech.save("wxt.mp3")
    playsound('wxt.mp3')
    a=int(input("enter your credit card no."))
    print('YOUR TICKET HAS BEEN CONFIRMED')
    final="your ticket no.={} (please do not loose it or might end up as a problem for yourself)".format(acc)
    print(final)
        

    
def roundway():
    
    t="enter how many tickets do you want"
    speech = gTTS(text=t, lang='en-us', slow=False)
    speech.save("how2.mp3")
    playsound('how2.mp3')
    t=int(input("enter the no. of tickets required"))
    '''mycursor.execute("create table roundway(Name varchar(50),Age int,Phno int,Dep_airport varchar(50),Arr_airport varchar(50),Dep_date date,Arr_date date,flight varchar(30),Acc_no int)")'''
    c2=0
    for i in range(t):
           
           name=(input("ENTER NAME :"))
           age=int(input("ENTER AGE:"))
           phno=int(input("ENTER PHONE NO :"))
           From=input("ENTER DEPARTURE AIRPORT :")
           To=input("ENTER ARRIVAL AIRPORT:")
           Dep_date=input("ENTER DEPARTURE DATE")
           Arr_date=input("ENTER ARRIVAL DATE")
           b=['Air India','Etihad','Emirates','Air India Express','Air Arabia','Qatar Airways']
           flight=random.choice(b)
           acc=random.randint(100000,700000)
    
           a="insert into roundway(Name,Age,Phno,dep_airport,arr_airport,Dep_date,Arr_date,flight,Acc_no) values('{}',{},{},'{}','{}','{}','{}','{}',{})".format(name,age,phno,From,To,Dep_date,Arr_date,flight,acc)
           mycursor.execute(a)
           mycon.commit()
           if age>16:
                  c2+=500
           elif age>2 and age<16:
                  c2+=350
           else:
                  c2+=0
       
    cost2="the total ticket cost is {}".format(c2)
    speech = gTTS(text=cost2, lang='en-us', slow=False)
    speech.save("wxt2.mp3")
    playsound('wxt2.mp3')
    a=int(input("enter your credit card no."))
    print("********************************************************************************************")
    print('YOUR ROUNDWAY TICKET HAS BEEN CONFIRMED')
    final="your ticket no.={} (please do not loose it or might end up as a problem for yourself)".format(acc)
    print(final)
#viewing the ticket

def view():
    tick="please enter your ticket no."
    speech = gTTS(text=tick, lang='en-us', slow=False)
    speech.save("wb.mp3")
    playsound('wb.mp3')
    p=int(input("enter the ticket no. "))
    print("**********************************")
    a="select*from oneway where Acc_no={}".format(p)
    mycursor.execute(a)
    data=mycursor.fetchone()
    for i in data:
           
       print(i,end='  ')
    



    

        
#cancelling ticket    
def cancelt():
    text="1 if you are a one way traveller\n2 if you are a roundway traveller"
    speech = gTTS(text=text, lang='en-us', slow=False)
    speech.save("wb1.mp3")
    playsound('wb1.mp3')
    way=int(input("1 if you are a one way traveller\n2 if you are a roundway traveller"))
    
    roller="enter your ticket number"
    speech = gTTS(text=roller, lang='en-us', slow=False)
    speech.save("wb12.mp3")
    playsound('wb12.mp3')
    guy=int(input("enter your ticket number"))


    if way==1:
        mycursor.execute("select*from oneway")
        
        data=mycursor.fetchall()
        for row in data:
            if row[8]==guy:
                mycursor.execute("delete from oneway where Acc_no={}".format(guy))
                print("your ticket has been cancelled")
                mycon.commit()
            else:
                print("try again")
    if way==2:
        mycursor.execute("select*from roundway")
        
        data=mycursor.fetchall()
        for row in data:
            hr="your ticket has been cancelled"
            speech = gTTS(text=hr, lang='en-us', slow=False)
            speech.save("wb13.mp3")
            
            
            if row[9]==guy:
                mycursor.execute("delete from roundway where Acc_no={}".format(guy))
                playsound('wb13.mp3')
                print("your ticket has been cancelled")
            else:
                playsound('wbl3.mp3')
                print("try again")
                
def baggage():
    w=0
    du="wbt.mp3"
    bo="enter the number of bags"
    speech = gTTS(text=bo, lang='en-us', slow=False)
    speech.save(du)
    playsound(du)
    j='h'
    du.replace('b',j)
    j=j+'c'
    bags=int(input("enter the no. of bags"))
    for i in range(bags):
        we=int(input("enter weight per bag_in kgs"))
        w+=we
    if w>=90:
        t="your baggage is over the limit"
        speech = gTTS(text=t, lang='en-us', slow=False)
        speech.save("wbta.mp3")
        playsound('wbta.mp3')
        
        print("your baggage is over the limit")
    else:
        t="your baggage has been checked in and now please enter to go for the immegration"
        speech = gTTS(text=t, lang='en-us', slow=False)
        speech.save("wbta.mp3")
        playsound('wbta.mp3')
        print("your baggage has been checked in and now please press y to go for the immegration")
        
#for meal
def MENU():
    
    '''b="create table MENU(ITEM_NAME varchar(50),PRICE int)"
    mycursor.execute(b)'''
    ITEM_NAME=(input("ENTER ITEM NAME :"))
    PRICE=int(input('ENTER PRICE:'))
    a="insert into MENU values('{}',{})".format(ITEM_NAME, PRICE)
    mycursor.execute(a)
    mycon.commit()
    

    
def bill():
    root=Tk()          #Creates a tkinter interface window
    root.geometry("1500x750+0+0")#Size
    root.title("menu")
    root.configure(bg="orange")




    # Create a photoimage object of the image in the path
    image1 = Image.open(r"C:\Users\Dell\Downloads\pythonshep.jpg")
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=10, y=10)


    tops=Frame(root,width=1350, height=100,bd=12,relief ="raise")#Frame is created 
    tops.pack(side=TOP)
    Label1=Label(tops,text='Duty Free Restaurant service',font=('Arial', 50,'bold'),bg='light blue') #Text to be written in the Frame 

    Label1.grid (row=0,column=0)

    bottom=Frame(root,width=1350, height=500,bd=12,relief ="raise")
    bottom.pack(side=BOTTOM)

    f1=Frame(bottom,width=500, height=650,bd=12,relief ="raise")
    f1.pack(side=LEFT)
    f2=Frame(bottom,width=500, height=650,bd=12,relief ="raise")
    f2.pack(side=RIGHT)
    var1=IntVar()         #Variables to store the numeric values entered in the menu
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    var12=IntVar()
    var13=IntVar()
    var14=IntVar()


    var1.set(0)        #Setting it to 0 by default
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)

    varTotal=StringVar()                  
    varstr1=StringVar()
    varstr2=StringVar()
    varstr3=StringVar()
    varstr4=StringVar()
    varstr5=StringVar()
    varstr6=StringVar()
    varstr7=StringVar()
    varstr8=StringVar()
    varstr9=StringVar()
    varstr10=StringVar()
    varstr11=StringVar()
    varstr12=StringVar()

    varstr1.set('0')
    varstr2.set('0')
    varstr3.set("0")
    varstr4.set("0")
    varstr5.set("0")
    varstr6.set("0")
    varstr7.set("0")
    varstr8.set("0")
    varstr9.set("0")
    varstr10.set("0")
    varstr11.set("0")
    varstr12.set("0")
    varTotal.set('0')
    #total button
    def chkButton1():
        if var1.get()==1:
                          
            txtbiru.configure(state=NORMAL)
            varstr1.set("")
        elif(var1.get()==0):
            txtbiru.configure(state=DISABLED)
            varstr1.set("0")
    def chkButton2():
        if var2.get()==1:
            txtchf.configure(state=NORMAL)
            varstr2.set("")
        elif(var2.get()==0):
            txtchf.configure(state=DISABLED)
            varstr2.set("0")
    def chkButton3():
        if var3.get()==1:
            txtdal.configure(state=NORMAL)
            varstr3.set("")
        elif(var3.get()==0):
            txtdal.configure(state=DISABLED)
            varstr3.set("0")
    def chkButton4():
        if var4.get()==1:
            txtvbi.configure(state=NORMAL)
            varstr4.set("")
        elif(var4.get()==0):
            txtvbi.configure(state=DISABLED)
            varstr4.set("0")
    def chkButton5():
        if var5.get()==1:
            txtcmn.configure(state=NORMAL)
            varstr5.set("")
        elif(var5.get()==0):
            txtcmn.configure(state=DISABLED)
            varstr5.set("0")
    def chkButton6():
        if var6.get()==1:
            txttri.configure(state=NORMAL)
            varstr6.set("")
        elif(var6.get()==0):
            txttri.configure(state=DISABLED)
            varstr6.set("0")
    def chkButton7():
        if var7.get()==1:
            txtbrt.configure(state=NORMAL)
            varstr7.set("")
        elif(var7.get()==0):
            txtbrt.configure(state=DISABLED)
            varstr7.set("0")
    def chkButton8():
        if var8.get()==1:
            txttab.configure(state=NORMAL)
            varstr8.set("")
        elif(var8.get()==0):
            txttab.configure(state=DISABLED)
            varstr8.set("0")
    def chkButton9():
        if var9.get()==1:
            txtcur.configure(state=NORMAL)
            varstr9.set("")
        elif(var9.get()==0):
            txtcur.configure(state=DISABLED)
            varstr9.set("0")
    def chkButton10():
        if var10.get()==1:
            txtcck.configure(state=NORMAL)
            varstr10.set("")
        elif(var10.get()==0):
            txtcck.configure(state=DISABLED)
            varstr10.set("0")
    def chkButton11():
        if var11.get()==1:
            txtorm.configure(state=NORMAL)
            varstr11.set("")
        elif(var11.get()==0):
            txtorm.configure(state=DISABLED)
            varstr11.set("0")
    def chkButton12():
        if var12.get()==1:
            txtpdp.configure(state=NORMAL)
            varstr12.set("")
        elif(var12.get()==0):
            txtpdp.configure(state=DISABLED)
            varstr12.set("0")

    def costofmeal():
        meal1=float(varstr1.get())
        meal2=float(varstr2.get())
        meal3=float(varstr3.get())
        meal4=float(varstr4.get())
        meal5=float(varstr5.get())
        meal6=float(varstr6.get())
        meal7=float(varstr7.get())
        meal8=float(varstr8.get())
        meal9=float(varstr9.get())
        meal10=float(varstr10.get())
        meal11=float(varstr11.get())
        meal12=float(varstr12.get())
        itotal=(meal1*20)+(meal2*15)+(meal3*12)+(meal4*18)+(meal5*25)+(meal6*2)+(meal7*4)+(meal8*5)+(meal9*8)+(meal10*5)+(meal11*4)+(meal12*5)
        varTotal.set(itotal)
        
        




    #frame 1
    Labelmeal=Label(f1,text='Meals',font=('Arial', 18,'bold'))
    Labelmeal.grid (row=0,column=0)

    biru=Checkbutton(f1,text="Chicken Biryani\t\t\t20",variable=var1,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton1).grid(row=2,column=0,sticky=W)
    txtbiru=Entry(f1,font=("arial",18,'bold'),textvariable=varstr1,width=6,state=DISABLED)
    txtbiru.grid(row=2,column=1)

    chf=Checkbutton(f1,text="Chicken Fried rice\t\t15",variable=var2,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton2).grid(row=3,column=0,sticky=W)
    txtchf=Entry(f1,font=("arial",18,'bold'),textvariable=varstr2,width=6,state=DISABLED)
    txtchf.grid(row=3,column=1)

    dal=Checkbutton(f1,text="Dal and Plain Rice\t\t12",variable=var3,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton3).grid(row=4,column=0,sticky=W)
    txtdal=Entry(f1,font=("arial",18,'bold'),textvariable=varstr3,width=6,state=DISABLED)
    txtdal.grid(row=4,column=1)

    vbi=Checkbutton(f1,text="Veg Biryani\t\t\t18",variable=var4,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton4).grid(row=5,column=0,sticky=W)
    txtvbi=Entry(f1,font=("arial",18,'bold'),textvariable=varstr4,width=6,state=DISABLED)
    txtvbi.grid(row=5,column=1)

    cmn=Checkbutton(f1,text="Chicken Manchurian\t\t25",variable=var5,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton5).grid(row=6,column=0,sticky=W)
    txtcmn=Entry(f1,font=("arial",18,'bold'),textvariable=varstr5,width=6,state=DISABLED)
    txtcmn.grid(row=6,column=1)

    tri=Checkbutton(f1,text="Tandori Roti(per ps)\t\t2",variable=var6,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton6).grid(row=7,column=0,sticky=W)
    txttri=Entry(f1,font=("arial",18,'bold'),textvariable=varstr6,width=6,state=DISABLED)
    txttri.grid(row=7,column=1)

    brt=Checkbutton(f1,text="Butter Roti(per ps)\t\t4",variable=var7,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton7).grid(row=8,column=0,sticky=W)
    txtbrt=Entry(f1,font=("arial",18,'bold'),textvariable=varstr7,width=6,state=DISABLED)
    txtbrt.grid(row=8,column=1)

    tab=Checkbutton(f1,text="Tea and Biscuits\t\t\t5",variable=var8,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton8).grid(row=9,column=0,sticky=W)
    txttab=Entry(f1,font=("arial",18,'bold'),textvariable=varstr8,width=6,state=DISABLED)
    txttab.grid(row=9,column=1)

    cur=Checkbutton(f1,text="Custard\t\t\t\t8",variable=var9,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton9).grid(row=10,column=0,sticky=W)
    txtcur=Entry(f1,font=("arial",18,'bold'),textvariable=varstr9,width=6,state=DISABLED)
    txtcur.grid(row=10,column=1)

    cck=Checkbutton(f1,text="Chocolate Cake\t\t\t5",variable=var10,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton10).grid(row=11,column=0,sticky=W)
    txtcck=Entry(f1,font=("arial",18,'bold'),textvariable=varstr10,width=6,state=DISABLED)
    txtcck.grid(row=11,column=1)

    orm=Checkbutton(f1,text="orea milkshake\t\t\t4",variable=var11,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton11).grid(row=12,column=0,sticky=W)
    txtorm=Entry(f1,font=("arial",18,'bold'),textvariable=varstr11,width=6,state=DISABLED)
    txtorm.grid(row=12,column=1)

    pdp=Checkbutton(f1,text="Pepsi(diet)\t\t\t5",variable=var12,onvalue=1,offvalue=0,
                     font=("arial",18,'bold'),command=chkButton12).grid(row=13,column=0,sticky=W)
    txtpdp=Entry(f1,font=("arial",18,'bold'),textvariable=varstr12,width=6,state=DISABLED)
    txtpdp.grid(row=13,column=1)

    #frame2
    var22=IntVar()
    var22.set(0)

    varChange1=StringVar()
    varChange2=StringVar()
    varSubTotal=StringVar()

    varSubTotal.set("")
    varChange1.set("")
    varChange2.set("")

    lblPayment=Label(f2,font=("arial",15,"bold"),text="BILL",bd=10,
                     width=16,anchor='w')
    lblPayment.grid(row=0,column=0)
    

    cardpay=ttk.Combobox(f2,textvariable=var22,state='readonly',font=('arial',15,'bold'),
                         width=20)
    cardpay['value']=('Cash','Master Card','Visa Card','Debit Card')
    cardpay.current(0)
    cardpay.grid(row=1,column=0)
    txtChange=Entry(f2,font=("arial",18,'bold'),textvariable=varChange2,width=6,justify='left')
    txtChange.grid(row=2,column=0)



    txtPayment=Label(f2,font=("arial",18,"bold"),textvariable=varChange1,width=6,
                     justify='left')
    txtPayment.grid(row=3,column=0)
    lblsubtotal=Label(f2,font=('arial',14,'bold'),text="Sub Total",bd=10,width=8,anchor='w')
    lblsubtotal.grid(row=3,column=1)
    txtsubtotal=Label(f2,font=("arial",18,"bold"),textvariable=varSubTotal,width=6,
                     justify='left')
    txtsubtotal.grid(row=3,column=2)

    lbltotal=Label(f2,font=('arial',14,'bold'),text=" Total",bd=10,width=8,anchor='w')
    lblsubtotal.grid(row=4,column=1)
    txttotal=Label(f2,font=("arial",18,"bold"),textvariable=varTotal,width=6,state=DISABLED,
                     justify='left')
    txttotal.grid(row=4,column=2)


    #button exit
    def iExit():
        qExit=messagebox.askyesno("Quit Syestem","Do you want to exit?")
        if qExit>0:
            root.destroy()
            return


            


    def createNewWindow():
              
        Label23=Label(root,text='THANKYOU FOR YOUR PAYMENT HAVE A SAFE FLIGHT',font=('Comic Sans MS',13,'bold'))
        Label23.place(x=732,y=200)
        timmy="thank you for your payment and have a safe flight a head"
        speech = gTTS(text=timmy, lang='en-us', slow=False)
        speech.save("pog69.mp3")
        playsound('pog69.mp3')
        
        

    btnTotal=Button(f2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
                    text="Pay ",command=createNewWindow).grid(row=5,column=1)
    btntotal=Button(f2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
                    text="Total ",command=costofmeal).grid(row=5,column=0)


    btnExit=Button(f2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
                    text="Exit ",command=root.destroy).grid(row=5,column=2)



    root.mainloop()


def facecam():
    cam_port=0
    ramp_frames=30
    camera=cv2.VideoCapture(cam_port)

    def get_image():
        retval,im=camera.read()
        return im

    for i in range(ramp_frames):
        temp=get_image()
    print("capturing image")

    camera_capture=get_image()
    file="test_images.jpg"
    cv2.imwrite(file, camera_capture)

    del camera
    print("picture taken")

    ch6=input("enter y to take emirates id pic - ")




    if ch6=='y':
        cam_port1=0
        ramp_frames1=40
        camera1=cv2.VideoCapture(cam_port1)

        def get_image1():
            retval1,im1=camera1.read()
            return im1

        for i in range(ramp_frames1):
            temp1=get_image1()
        print("capturing image")

        camera_capture1=get_image1()
        file1="eid_images.jpg"
        cv2.imwrite(file1, camera_capture1)

        del camera1
        print("picture taken")

    img1 = face_recognition.load_image_file("test_images.jpg")
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    faceloc = face_recognition.face_locations(img1)[0]
    encodeabu = face_recognition.face_encodings(img1)[0]
    cv2.rectangle(img1, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 2)

    img2 = face_recognition.load_image_file("eid_images.jpg")
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    facetest = face_recognition.face_locations(img2)[0]
    encodetest = face_recognition.face_encodings(img2)[0]
    cv2.rectangle(img2, (facetest[3], facetest[0]), (facetest[1], facetest[2]), (255, 0, 255), 2)

    result = face_recognition.compare_faces([encodeabu], encodetest)
    l=random.randrange(1,50)
    txt="your immigration is over and now you may wait at gate {}".format(l)
    speech = gTTS(text=txt, lang='en-us', slow=False)
    speech.save("wts.mp3")
    surur="you are arrested and now put your hands in the air"
    speech = gTTS(text=surur, lang='en-us', slow=False)
    speech.save("surur.mp3")
    try:
                  
       
           if result==[True]:
               print("your immigration is over and now you may wait at gate {}".format(l))
        
               playsound('wts.mp3')
        
           else:
               print("you are arrested and now put your hands in the air")
               playsound("surur.mp3")
    except IndexError:
           print("please try again")
           
    

def boarding():
       tam="enter 1 if you are a oneway traveller and 2 if you are a roundway traveller"
       speech = gTTS(text=tam, lang='en-us', slow=False)
       speech.save("pog.mp3")
       playsound('pog.mp3')
       
       ch8=int(input("enter 1 if you are a traveller \n2 if you are a roundway traveller"))
       dm=input("enter your name")
       
       if ch8==1:
                    
              
              
              mycursor.execute("select*from oneway")
              data=mycursor.fetchall()
              for i in data:
                     
                     if i[0]==dm:
                            
                            dc="you have cleared your boarding and now you are requested to board your flight have a safe journey"
                            speech = gTTS(text=dc, lang='en-us', slow=False)
                            speech.save("dcl.mp3")
                            playsound('dcl.mp3')
                            print("you have cleared your boarding and now you are requested to board your flight have a safe journey")
       else:
              
              mycursor.execute("select*from roundway")
              data=mycursor.fetchall()
              for i in data:
                     
                     if i[0]==dm:
                            
                            
                            dc="you have cleared your boarding and now you are requested to board your flight"
                            speech = gTTS(text=dc, lang='en-us', slow=False)
                            speech.save("dcl.mp3")
                            playsound("dcl.mp3")
                            print("you have cleared your boarding and now you are requested to board your flight have a safe journey")             
                            
              



                
#main conditions
ch5='y'
main="Enter  1 to book a ticket\n enter 2 to view ticket info\n Enter 3 to cancel the ticket \n 4to check in your baggage \n 5 to go for the immigration \n 6 to order a meal \n 7 for boarding  "
speech = gTTS(text=main, lang='en-us', slow=False)
speech.save("tick.mp3")
playsound('tick.mp3')

while ch5!='n':
    
    print()
    print("1 To book a ticket\n2 to view ticket info \n3 cancel the ticket\n4 to check in for your baggage\n5 to go for the immigration \n6 to order meal \n7 to board for the plane ")

    ch1=int(input("please enter your choice here  "))

    if ch1==1:
        way="enter 1 to book a one way and enter 2 to book a roundway ticket"
        speech = gTTS(text=way, lang='en-us', slow=False)
        speech.save("way.mp3")
        playsound('way.mp3')
        print("************************************************************")
        ch2=int(input("1 one way\n2 round way "))
        if ch2==1:
            one()
            print("*******************************************************")
            ch5=(input("enter y to return to the menu "))
        
        else:
            roundway()
            print("*******************************************************")
            ch5=(input("enter y to return to the menu "))
    elif ch1==2:
        view()
        print("\n*******************************************************")
        ch5=(input("enter y to return to the menu "))
    elif ch1==3:
        cancelt()
        print("*******************************************************")
        ch5=(input("enter y to return to the menu "))
    elif ch1==4:
        baggage()
        print("*******************************************************")
        ch5=(input("enter y to return to the menu "))
    elif ch1==5:
        facecam()
        print("********************************************************")
        ch5=(input("enter y to return to the menu "))
    elif ch1==6:
        bill()
        print("*******************************************************")
        ch5=(input("enter y to return to the menu "))
    else:
        boarding()
        print("*******************************************************")
        ch5=(input("enter y to return to the menu "))









