#this code will be used as module to import into login.py file so, here variables have been declared as global
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import mysql.connector
from tkinter import font as tkFont
from tkcalendar import Calendar, DateEntry #pip install tkcalendar
from tkinter import ttk
from time import time 
from datetime import date
import tkinter
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter.simpledialog import askstring
import webbrowser

#start admin
def start_admin(user,password,w="default"):
    w.destroy()
    mail_admin='iiitktm.libraryadm@gmail.com'
    today = date.today()
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="XXXX",#Replace XXXX with your MySQL password
        database="Library")
    cur = con.cursor()
           
    Regno=user

    #start
    #fetching data of user after login
    command="select Aname,Aid,Email,password from admin where Aid=%s and password=%s"
    var=[user, password]
    cur.execute(command,var)
    user_details=cur.fetchall()

    admin = Tk()
    admin.title(str("Hii, "+user_details[0][0])+"  |   Welcome to IIIT Kottayam Library")
    #admin.minsize(width=400,height=400)
    admin.geometry("1150x630+50+5")
    admin.resizable(False,False)
    #creating menubar
    menubar = Menu(admin)



    Canvas1 = Canvas(admin)
    Canvas1.config(bg="#ab9672")##B8DBE6
    Canvas1.pack(expand=True,fill=BOTH)

    def destroy(x):
        x.destroy()

    '''def SearchStudents():
        global search_entry
        search = str(search_entry.get())'''


    admin_email_password='NULL'


    def access_mail():
        global admin_email_password
        admin_email_password=askstring("Admin Email Password","Enter Your Mail Password!!",show='*')
        #,command=recheck
        passs='XXXX'
        if admin_email_password==passs:
            messagebox.showinfo('ADMIN Email Password','Password Accepted')
        else:
            messagebox.showwarning('ADMIN Email ADMIN Password','Incorrect Password')

    access_email=Button(admin,text='Access Email',bg='#525b59', fg='white', command=access_mail)
    access_email.place(relx=0.04,rely=0.02,relwidth=0.08,relheight=0.05)

    header_admin= Label(admin,text='ADMIN',bg='#525b59', fg='white')
    header_admin.place(relx=0.65,rely=0.02,relwidth=0.08,relheight=0.05)

    header_username=Button(admin,text=user_details[0][0],fg='black')
    header_username.place(relx=0.74,rely=0.02,relwidth=0.16,relheight=0.05)

    logout=Button(admin,text='Logout',command=(lambda x=admin: start_login(admin)),bg='Red',fg='Black', activeforeground='black')#, bd='2', font=fineFont, command=lambda x=admin: start_login(admin)
    logout.place(relx=0.9, rely=0.02,relwidth=0.06,relheight=0.05)

    #Reload=Button(admin,text='Reload',fg='black',command=start_admin(user_details[0][1],user_details[0][3]))
    #Reload.place(relx=0.04,rely=0.02,relwidth=0.15,relheight=0.05)

    #headingFrame1 = Frame(admin,bg="#FFBB00",bd=2)
    #headingFrame1.place(relx=0,rely=0.0,relwidth=1,relheight=0.08)

    #headingLabel = Label(headingFrame1, text="Welcome ADMIN", bg='black', fg='white', font=('Courier',15))
    #headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    def student_print(val):
        rows=val
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        lboxs.place(relx=0.02, rely=0.04,relwidth=0.94,relheight=0.91)
        lboxs.delete(0,'end')
        #start
        v = Scrollbar(labelFrame, orient='vertical')
        #v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side = RIGHT, fill = Y)
        h = Scrollbar(labelFrame, orient = 'horizontal')
        #h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side = BOTTOM, fill = X)
        t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
        #end

        reg=Label(lboxs,text='Registration Number',bg='#97cee3',fg='white',width=23,font='BOLD', anchor='w')
        t.window_create(END,window=reg)
        s_name=Label(lboxs,text='Name',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='w')
        t.window_create(END,window=s_name)
        s_mail=Label(lboxs,text='Batch',bg='#97cee3',fg='white',width=17,font='BOLD', anchor='c')
        t.window_create(END,window=s_mail)
        s_phone=Label(lboxs,text='History',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='c')
        t.window_create(END,window=s_phone)
        s_batch=Label(lboxs,text='Update',bg='#97cee3',fg='white',font='BOLD',width=10, anchor='c')
        t.window_create(END,window=s_batch)
        s_course=Label(lboxs,text='Pending',bg='#97cee3',fg='white',width=14,font='BOLD', anchor='c')
        t.window_create(END,window=s_course)
        s_fine=Label(lboxs,text='Mail',bg='#97cee3',fg='white',width=12,font='BOLD', anchor='c')
        t.window_create(END,window=s_fine)
        t.insert(END,"\n")

        for row in rows:
            x=row[0]
            reg=Label(lboxs,bg='yellow',fg='black',width=25, anchor='w',text=row[0])#)#, anchor='w',text=row[0
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text=row[1],bg='yellow',fg='black',width=33, anchor='w')
            t.window_create(END,window=s_name)
            s_mail=Label(lboxs,text=row[2],bg='yellow',fg='black',width=15, anchor='w')
            t.window_create(END,window=s_mail)
            s_phone=Button(lboxs,text='History',bg='yellow',fg='black',width=15, anchor='c',command= (lambda y=x : print_his(y)))
            t.window_create(END,window=s_phone)
            s_batch=Button(lboxs,text='Update',bg='yellow',fg='black',width=15, anchor='c',command= (lambda y=x : up_stu(y)))
            t.window_create(END,window=s_batch)
            s_course=Button(lboxs,text='Pending',bg='yellow',fg='black',width=15, anchor='c',command= (lambda y=x : pending_stu(y)))
            t.window_create(END,window=s_course)
            s_fine=Button(lboxs,text='Mail',bg='yellow',fg='black',width=15, anchor='c',command= (lambda y=x : mail_stu(y)))
            t.window_create(END,window=s_fine)
            t.insert(END,"\n")
                #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                #lboxs.insert(lboxs.size()+1, insertdata)
                #t.insert(END,insertdata)
            #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)


    def book_print(val):
        rows=val
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        lboxs.place(relx=0.02, rely=0.04,relwidth=0.94,relheight=0.91)
        lboxs.delete(0,'end')
        #start
        v = Scrollbar(labelFrame, orient='vertical')
        #v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side = RIGHT, fill = Y)
        h = Scrollbar(labelFrame, orient = 'horizontal')
        #h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side = BOTTOM, fill = X)
        t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
        #end

        reg=Label(lboxs,text='Book ID',bg='#97cee3',fg='white',width=16,font='BOLD', anchor='w')
        t.window_create(END,window=reg)
        s_name=Label(lboxs,text='Book Name',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='w')
        t.window_create(END,window=s_name)
        s_mail=Label(lboxs,text='Author',bg='#97cee3',fg='white',width=18,font='BOLD', anchor='c')
        t.window_create(END,window=s_mail)
        s_phone=Label(lboxs,text='Subject',bg='#97cee3',fg='white',width=13,font='BOLD', anchor='c')
        t.window_create(END,window=s_phone)
        s_batch=Label(lboxs,text='Category',bg='#97cee3',fg='white',font='BOLD',width=13, anchor='c')
        t.window_create(END,window=s_batch)
        s_course=Label(lboxs,text='Update',bg='#97cee3',fg='white',width=18,font='BOLD', anchor='c')
        t.window_create(END,window=s_course)
        s_fine=Label(lboxs,text='Status',bg='#97cee3',fg='white',width=12,font='BOLD', anchor='c')
        t.window_create(END,window=s_fine)
        t.insert(END,"\n")

        for row in rows:
            x=row[0]
            reg=Label(lboxs,bg='yellow',fg='black',width=15, anchor='w',text=row[0])#)#, anchor='w',text=row[0
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text=row[1],bg='yellow',fg='black',width=33, anchor='w')
            t.window_create(END,window=s_name)
            s_mail=Label(lboxs,text=row[2],bg='yellow',fg='black',width=17, anchor='w')
            t.window_create(END,window=s_mail)
            s_phone=Label(lboxs,text=row[3],bg='yellow',fg='black',width=13, anchor='c')
            t.window_create(END,window=s_phone)
            s_batch=Label(lboxs,text=row[4],bg='yellow',fg='black',width=20, anchor='c')
            t.window_create(END,window=s_batch)
            s_course=Button(lboxs,text='Update',bg='yellow',fg='black',width=18, anchor='c',command= (lambda y=x : update_book_all(y)))#,command= book_update()
            t.window_create(END,window=s_course)
            s_fine=Button(lboxs,text='Status',bg='yellow',fg='black',width=18, anchor='c',command= (lambda y=x : b_status(y)))
            t.window_create(END,window=s_fine)
            t.insert(END,"\n")
                #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                #lboxs.insert(lboxs.size()+1, insertdata)
                #t.insert(END,insertdata)
            #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)

    def search_student(val):
        if combo_student.get()=='Registation Number':
            x=search_entry.get()
            cur.execute("select Regno,Sname,Batch from student where Regno='"+ str(x) +"'")
            rows=list(cur.fetchall())
            student_print(rows)

        elif combo_student.get()=='Name':
            x=search_entry.get()
            cur.execute("select Regno,Sname,Batch from student where Sname='"+ str(x) +"'")
            rows=list(cur.fetchall())
            student_print(rows)

    def search_books(val):
        if combo_book.get()=='Category':
            x=search_entry.get()
            cur.execute("select Bid,Bname,Author,Subject_name,CName from Book where CName='"+ str(x) +"'")
            rows=list(cur.fetchall())
            book_print(rows)

        elif combo_book.get()=='Subject':
            x=search_entry.get()
            cur.execute("select Bid,Bname,Author,Subject_name,CName from Book where Subject_name='"+ str(x) +"'")
            rows=list(cur.fetchall())
            book_print(rows)

        elif combo_book.get()=='Name':
            x=search_entry.get()
            cur.execute("select Bid,Bname,Author,Subject_name,CName from Book where Bname='"+ str(x) +"'")
            rows=list(cur.fetchall())
            book_print(rows)

        elif combo_book.get()=='Book ID':
            x=search_entry.get()
            cur.execute("select Bid,Bname,Author,Subject_name,CName from Book where Bid='"+ str(x) +"'")
            rows=list(cur.fetchall())
            book_print(rows)

        elif combo_book.get()=='Sub Book ID':
            x=search_entry.get()
            cur.execute("select book.Bid,book.Bname,book.Author,book.Subject_name,book.CName from book,Subbook where book.Bid=Subbook.Bid and Sub_bid='"+ str(x) +"'")
            rows=list(cur.fetchall())
            book_print(rows)


    '''def search_placeholder(event):
        isempty=False
        search_entry.configure(state=NORMAL)
        search_entry.delete(0, END)
        try:
            search_entry.unbind('<Button-1>', onclick_id)
        except:
            print()
        if n>1:
            search_entry.config(show="*")'''

    # search entry
    search_entry=Entry(admin)
    search_entry.insert(0,'Search Students/Books')
    search_entry.place(relx=0.04,rely=0.09, relwidth=0.92, relheight=0.06)
    '''search_entry.configure(state=DISABLED)
    onclick_id=search_entry.bind('<Button-1>', search_placeholder)#'''

    # Search Students
    combo_student=ttk.Combobox(admin,values=["Search Student Using...","Registation Number","Name"],state="readonly")
    combo_student.place(relx=0.04,rely=0.15, relwidth=0.45, relheight=0.05)
    combo_student.current(0)
    combo_student.bind("<<ComboboxSelected>>",search_student)
    #combo_student.pack()
    #sr1 = Button(admin,text="Search Students",bg='#525b59', fg='white')#,command=SearchStudents)
    #sr1.place(relx=0.34,rely=0.15, relwidth=0.15, relheight=0.05)

    # Search books
    combo_book=ttk.Combobox(admin,values=["Search Books Using...","Category","Subject","Name","Book ID","Sub Book ID"],state="readonly")
    combo_book.place(relx=0.51,rely=0.15, relwidth=0.45, relheight=0.05)
    combo_book.current(0)
    combo_book.bind("<<ComboboxSelected>>",search_books)
    #combo_book.pack()
    #sr2 = Button(admin,text="Search Books",bg='#525b59', fg='white')#,command=SearchBooks)
    #sr2.place(relx=0.81,rely=0.15, relwidth=0.15, relheight=0.05)

    #img = ImageTk.PhotoImage(Image.open("D:\\IIITK\\sem3\\IT Workshop 3\\project\\tkinter\\library_1.jpg").resize((1050, 440), Image.ANTIALIAS))
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\91969\\Desktop\\SEM 3\\IT WORKSHOP 3\\Project\\Project_code\\Final\\final_one\\library_1.jpg").resize((1050, 440), Image.ANTIALIAS))
    labelFrame = Label(admin,bg="black",image=img)#
    #labelFrame.image=img
    labelFrame.place(relx=0.04,rely=0.25,relwidth=0.92,relheight=0.71)

    welcome=Label(labelFrame,text="Welcome to\nIIIT Kottayam Library",fg='white',bg='#504e4e',font='bold')#
    welcome.place(relx=0.2,rely=0.35,relheight=0.3,relwidth=0.4)
    welcome.config(font=("Comic", 24))

    # Adding student to the Database
    def adds():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        # Validating and add
        def add_stu():
            fname=str(fullname1.get())
            usern=str(username1.get())
            mail=str(email1.get())
            passwrd=str(password1.get())
            cont=str(contact1.get())
            dob=str(dob1.get())
            batch=str(batch1.get())
            course=str(course1.get())
            rest='no'
            if(res.get()==1):
                rest='yes'
            bir=dob.split('/')
            dob=''
            if len(bir[2])==4:
                dob=bir[2]+'-'+bir[1]+'-'+bir[0]
            else:
                dob='20'+bir[2]+'-'+bir[1]+'-'+bir[0]
            fine='0'
            if(fname=='' or usern=="" or mail=="" or cont==None or dob==None or batch=="" or course=="" or passwrd=="")!=False:
                messagebox.showinfo("Can't ADD","All feilds are required!")
            elif(mail.endswith('@iiitkottayam.ac.in'))!=True:
                messagebox.showinfo("Invalid Email","Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
            elif(cont.isnumeric() and len(cont)==10)!=True:
                messagebox.showinfo("Invalid Contact Number","Enter a valid Contact Number(Length 10)!")
            elif (batch.isnumeric())!=True:
                messagebox.showinfo("Invalid Batch","Batch should be number and in format '20XX' !")
            elif(usern.isalnum())!=True:
                messagebox.showinfo("Invalid Username","Username should be Alphanumeric!")
            else:
                try:
                    val='add_student'
                    addformula="INSERT INTO Student (Sname, Regno, Password, Phone, Email, Batch, DOB, Fine, Course, is_restricted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    add_student=(fname,usern,passwrd,cont,mail,batch,dob,fine,course,rest)
                    cur.execute(addformula, add_student)
                    try:
                        check_mail(usern,val,passwrd)
                        con.commit()
                        fullname1.delete(0,'end')
                        username1.delete(0,'end')
                        email1.delete(0,'end')
                        password1.delete(0,'end')
                        contact1.delete(0,'end')
                        dob1.delete(0,'end')
                        batch1.delete(0,'end')
                        course1.delete(0,'end')
                        messagebox.showinfo("Student Added","Student is added successfully!")
                    except:
                        messagebox.showwarning("Error","Error in sending mail..\nLogin to email to perform the action!!")


                except(mysql.connector.errors.IntegrityError):
                    messagebox.showinfo("Can't add Student","Oops!!\nUsername already exist!!")


        details=Label(labelFrame,text="Add Details:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        fullname=Label(labelFrame,text="Full name",bg='black',fg='white').place(relx=0.1,rely=0.18,relwidth=0.25,relheight=0.07)
        username=Label(labelFrame,text="Username",bg='black',fg='white').place(relx=0.1,rely=0.27,relwidth=0.25,relheight=0.07)
        email=Label(labelFrame,text="Email Id",bg='black',fg='white').place(relx=0.1,rely=0.36,relwidth=0.25,relheight=0.07)
        password=Label(labelFrame,text="Password",bg='black',fg='white').place(relx=0.1,rely=0.45,relwidth=0.25,relheight=0.07)
        contact=Label(labelFrame,text="Contact no.",bg='black',fg='white').place(relx=0.1,rely=0.54,relwidth=0.25,relheight=0.07)
        dob=Label(labelFrame,text="Date Of Birth",bg='black',fg='white').place(relx=0.1,rely=0.63,relwidth=0.25,relheight=0.07)
        batch=Label(labelFrame,text="Batch",bg='black',fg='white').place(relx=0.1,rely=0.72,relwidth=0.25,relheight=0.07)
        course=Label(labelFrame,text="Course",bg='black',fg='white').place(relx=0.1,rely=0.81,relwidth=0.25,relheight=0.07)
        restrict=Label(labelFrame,text="Is Restricted?",bg='black',fg='white').place(relx=0.1,rely=0.90,relwidth=0.25,relheight=0.07)

        res=IntVar()
        res.set(2)

        fullname1 = Entry(labelFrame,bg='#cecece',fg='black')
        fullname1.place(relx=0.5,rely=0.18,relwidth=0.3,relheight=0.06)
        #print('fullname1',fullname1)
        username1 = Entry(labelFrame,bg='#cecece',fg='black')
        username1.place(relx=0.5,rely=0.27,relwidth=0.3,relheight=0.06)
        email1 = Entry(labelFrame,bg='#cecece',fg='black')
        email1.place(relx=0.5,rely=0.36,relwidth=0.3,relheight=0.06)
        password1 = Entry(labelFrame,bg='#cecece',fg='black')
        password1.place(relx=0.5,rely=0.45,relwidth=0.3,relheight=0.06)
        contact1 = Entry(labelFrame,bg='#cecece',fg='black')
        contact1.place(relx=0.5,rely=0.54,relwidth=0.3,relheight=0.06)
        dob1 = DateEntry(labelFrame, date_pattern='dd/mm/yyyy',state="readonly",bg='#cecece',fg='black')
        dob1.place(relx=0.5,rely=0.63,relwidth=0.15,relheight=0.06)
        batch1 = Entry(labelFrame,bg='#cecece',fg='black')
        batch1.place(relx=0.5,rely=0.72,relwidth=0.3,relheight=0.06)
        course1 = Entry(labelFrame,bg='#cecece',fg='black')
        course1.place(relx=0.5,rely=0.81,relwidth=0.3,relheight=0.06)
        re1= Radiobutton(labelFrame, text="Yes",bg='#cecece',fg='black')
        re1.place(relx=0.5,rely=0.90,relwidth=0.12,relheight=0.06)
        re1.config(variable=res, val=1)
        re2= Radiobutton(labelFrame, text="No",bg='#cecece',fg='black')
        re2.place(relx=0.65,rely=0.90,relwidth=0.12,relheight=0.06)
        re2.config(variable=res, val=2)

        add=Button(labelFrame,text='Add',bg='#7d7d7d',fg='black',command=add_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


    # View all the students from the database
    def views():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        lboxs.place(relx=0.02, rely=0.04,relwidth=0.94,relheight=0.91)

        #print_his()

        #def show():
        lboxs.delete(0,'end')
        #start
        v = Scrollbar(labelFrame, orient='vertical')
        #v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side = RIGHT, fill = Y)
        h = Scrollbar(labelFrame, orient = 'horizontal')
        #h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side = BOTTOM, fill = X)
        t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
        #end
        cur.execute("select Regno, Sname, Email, Phone, Batch, Course, Fine from student order by Regno")
        rows=list(cur.fetchall())

        reg=Label(lboxs,text='Reg.No.',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='w')
        t.window_create(END,window=reg)
        s_name=Label(lboxs,text='Name',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='w')
        t.window_create(END,window=s_name)
        s_mail=Label(lboxs,text='Email',bg='#97cee3',fg='white',width=25,font='BOLD', anchor='c')
        t.window_create(END,window=s_mail)
        s_phone=Label(lboxs,text='Contact',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='c')
        t.window_create(END,window=s_phone)
        s_batch=Label(lboxs,text='Batch',bg='#97cee3',fg='white',font='BOLD',width=10, anchor='c')
        t.window_create(END,window=s_batch)
        s_course=Label(lboxs,text='Course',bg='#97cee3',fg='white',width=9,font='BOLD', anchor='c')
        t.window_create(END,window=s_course)
        s_fine=Label(lboxs,text='Fine',bg='#97cee3',fg='white',width=11,font='BOLD', anchor='c')
        t.window_create(END,window=s_fine)
        s_history=Label(lboxs,text='History',bg='#97cee3',fg='white', font='BOLD',width=10 , anchor='c')
        t.window_create(END,window=s_history)
        t.insert(END,"\n")

        for row in rows:
            x=row[0]
            reg=Label(lboxs,bg='yellow',fg='black',width=13, anchor='w',text=row[0])#)#, anchor='w',text=row[0
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text=row[1],bg='yellow',fg='black',width=22, anchor='w')
            t.window_create(END,window=s_name)
            s_mail=Label(lboxs,text=row[2],bg='yellow',fg='black',width=30, anchor='w')
            t.window_create(END,window=s_mail)
            s_phone=Label(lboxs,text=row[3],bg='yellow',fg='black',width=13, anchor='c')
            t.window_create(END,window=s_phone)
            s_batch=Label(lboxs,text=row[4],bg='yellow',fg='black',width=12, anchor='c')
            t.window_create(END,window=s_batch)
            s_course=Label(lboxs,text=row[5],bg='yellow',fg='black',width=12, anchor='c')
            t.window_create(END,window=s_course)
            s_fine=Label(lboxs,text=row[6],bg='yellow',fg='black',width=12, anchor='c')
            t.window_create(END,window=s_fine)
            s_history=Button(lboxs,text='History',bg='grey',fg='black',command= (lambda y=x : print_his(y)),width=14, anchor='c')#(lambda y=x : print_his(y))
            t.window_create(END,window=s_history)
            t.insert(END,"\n")
                #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                #lboxs.insert(lboxs.size()+1, insertdata)
                #t.insert(END,insertdata)
            #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
            #end

        #display = Button(labelFrame,text="CLICK TO VIEW",bg='#525b59', fg='white',command=show)
        #display.place(relx=0.35,rely=0.05,relwidth=0.3,relheight=0.1)

    #history
    def print_his(val):
        for widget in labelFrame.winfo_children():
            widget.destroy()

        cur.execute("select DISTINCT Book.Bname,Book.Author,Return_book.Approved_date,Return_book.Return_date,Book.Bid,SubBook.Sub_bid,Return_book.Borrow_ID from Book,Student,SubBook,Return_book WHERE Book.Bid=SubBook.Bid and SubBook.Sub_bid=Return_book.Sub_bid and Return_book.Student_regno='"+str(val)+"'")
        rows=list(cur.fetchall())

        back=Button(labelFrame,text="View Students",bg='#525b59', fg='white',command=views)#,command=SearchStudents)
        back.place(relx=0.02,rely=0.02, relwidth=0.155, relheight=0.06)


        lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        lboxs.place(relx=0.02, rely=0.1,relwidth=0.94,relheight=0.91)

        lboxs.delete(0,'end')
        #start
        v = Scrollbar(labelFrame, orient='vertical')
        #v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side = RIGHT, fill = Y)
        h = Scrollbar(labelFrame, orient = 'horizontal')
        #h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side = BOTTOM, fill = X)
        t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
        #end

        reg=Label(lboxs,text='Book Name',bg='#97cee3',fg='white',width=30,font='BOLD', anchor='w')
        t.window_create(END,window=reg)
        s_name=Label(lboxs,text='Author Name',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='w')
        t.window_create(END,window=s_name)
        s_mail=Label(lboxs,text='Approved Date',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='c')
        t.window_create(END,window=s_mail)
        s_phone=Label(lboxs,text='Return Date',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='c')
        t.window_create(END,window=s_phone)
        s_batch=Label(lboxs,text='Book ID',bg='#97cee3',fg='white',font='BOLD',width=10, anchor='c')
        t.window_create(END,window=s_batch)
        s_course=Label(lboxs,text='Sub Book ID',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='c')
        t.window_create(END,window=s_course)
        s_fine=Label(lboxs,text='Borrow ID',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='c')
        t.window_create(END,window=s_fine)
        t.insert(END,"\n")

        for row in rows:
            #x=row[0]
            reg=Label(lboxs,bg='yellow',fg='black',width=38, anchor='w',text=row[0])#)#, anchor='w',text=row[0
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text=row[1],bg='yellow',fg='black',width=22, anchor='w')
            t.window_create(END,window=s_name)
            s_mail=Label(lboxs,text=row[2],bg='yellow',fg='black',width=22, anchor='w')
            t.window_create(END,window=s_mail)
            s_phone=Label(lboxs,text=row[3],bg='yellow',fg='black',width=14, anchor='w')
            t.window_create(END,window=s_phone)
            s_batch=Label(lboxs,text=row[4],bg='yellow',fg='black',width=13, anchor='c')
            t.window_create(END,window=s_batch)
            s_course=Label(lboxs,text=row[5],bg='yellow',fg='black',width=13, anchor='c')
            t.window_create(END,window=s_course)
            s_fine=Label(lboxs,text=row[6],bg='yellow',fg='black',width=13, anchor='c')
            t.window_create(END,window=s_fine)
            t.insert(END,"\n")
                #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                #lboxs.insert(lboxs.size()+1, insertdata)
                #t.insert(END,insertdata)
            #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)


    # Deleting Student from the Database
    def deletes():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        # Verufy and delete
        def del_stu():
            delst=str(dusername.get())
            if(delst==''):
                messagebox.showinfo("Can't Delete","Enter Student's Registration Number!")
            cur.execute("DELETE FROM Student WHERE Regno='"+ delst +"'")
            val='delete_student'
            s_bid='Student'
            check_mail(delst,val,s_bid)
            try:
                con.commit()
                dusername.delete(0,'end')
                messagebox.showinfo("Student Deleted","Student is Deleted successfully!")
            except:
                messagebox.showwarning("Error","Error in sending mail..\nLogin to email to perform the action!!")

        details=Label(labelFrame,text="Enter Details:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        username=Label(labelFrame,text="Registration ID",bg='black',fg='white').place(relx=0.1,rely=0.28,relwidth=0.25,relheight=0.08)
        dusername = Entry(labelFrame,bg='#cecece',fg='black')
        dusername.place(relx=0.5,rely=0.28,relwidth=0.3,relheight=0.08)
        delete=Button(labelFrame,text='Delete',bg='#7d7d7d',fg='black',command=del_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)

    # Update student details
    def updates():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        def up_stu():
            regi=str(st_reg.get())
            for widget in labelFrame.winfo_children():
                widget.destroy()

            cur.execute("select * from student where Regno='"+ regi +"'")
            rows=list(cur.fetchall())

            def update_stu():
                fname=str(fullname1.get())
                fine=str(fine1.get())
                mail=str(email1.get())
                passwrd=str(password1.get())
                cont=str(contact1.get())
                dob=str(dob1.get())
                batch=str(batch1.get())
                course=str(course1.get())
                rest='no'
                if(res.get()==1):
                    rest='yes'
                bir=dob.split('/')
                dob=''
                if len(bir[2])==4:
                    dob=bir[2]+'-'+bir[1]+'-'+bir[0]
                else:
                    dob='20'+bir[2]+'-'+bir[1]+'-'+bir[0]

                if(fname=='' or fine=="" or mail=="" or cont==None or dob==None or batch=="" or course=="" or passwrd=="")!=False:
                    messagebox.showinfo("Can't ADD","All feilds are required!")
                elif(mail.endswith('@iiitkottayam.ac.in'))!=True:
                    messagebox.showinfo("Invalid Email","Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
                elif(cont.isnumeric() and len(cont)==10)!=True:
                    messagebox.showinfo("Invalid Contact Number","Enter a valid Contact Number(Length 10)!")
                elif (batch.isnumeric())!=True:
                    messagebox.showinfo("Invalid Batch","Batch should be number and in format '20XX' !")
                else:
                    try:
                        val='update_student'
                        #addformula="INSERT INTO Student (Sname, Regno, Password, Phone, Email, Batch, DOB, Fine, Stream_id, is_restricted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        #add_student=(fname,usern,passwrd,cont,mail,batch,dob,fine,course,rest)
                        #cur.execute(addformula, add_student)
                        cur.execute("UPDATE Student SET Sname='"+ fname +"',Password='"+ passwrd +"',Phone='"+ cont +"',Email='"+ mail +"',Batch='"+ batch +"',DOB='"+ dob +"',Fine='"+ fine +"',Course='"+ course +"',is_restricted='"+ rest +"' WHERE Regno='"+ regi +"'")
                        try:
                            check_mail(regi,val,passwrd)
                            con.commit()
                            fullname1.delete(0,'end')
                            fine1.delete(0,'end')
                            email1.delete(0,'end')
                            password1.delete(0,'end')
                            contact1.delete(0,'end')
                            dob1.delete(0,'end')
                            batch1.delete(0,'end')
                            course1.delete(0,'end')
                            messagebox.showinfo("Student Updated","Student Details are updated successfully!")
                            updates()
                        except:
                            messagebox.showwarning("Error","Error in sending mail..\nLogin to email to perform the action!!")
                    except:
                        messagebox.showinfo("Can't Update Student","Oops!!\nSomething went wrong!!")


            details=Label(labelFrame,text="Enter Details to Update:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
            fullname=Label(labelFrame,text="Full name",bg='black',fg='white').place(relx=0.1,rely=0.18,relwidth=0.25,relheight=0.07)
            fine=Label(labelFrame,text="Fine",bg='black',fg='white').place(relx=0.1,rely=0.27,relwidth=0.25,relheight=0.07)
            email=Label(labelFrame,text="Email Id",bg='black',fg='white').place(relx=0.1,rely=0.36,relwidth=0.25,relheight=0.07)
            password=Label(labelFrame,text="Password",bg='black',fg='white').place(relx=0.1,rely=0.45,relwidth=0.25,relheight=0.07)
            contact=Label(labelFrame,text="Contact no.",bg='black',fg='white').place(relx=0.1,rely=0.54,relwidth=0.25,relheight=0.07)
            dob=Label(labelFrame,text="Date Of Birth",bg='black',fg='white').place(relx=0.1,rely=0.63,relwidth=0.25,relheight=0.07)
            batch=Label(labelFrame,text="Batch",bg='black',fg='white').place(relx=0.1,rely=0.72,relwidth=0.25,relheight=0.07)
            course=Label(labelFrame,text="Course",bg='black',fg='white').place(relx=0.1,rely=0.81,relwidth=0.25,relheight=0.07)
            restrict=Label(labelFrame,text="Is Restricted?",bg='black',fg='white').place(relx=0.1,rely=0.90,relwidth=0.25,relheight=0.07)

            res=IntVar()
            restricted=rows[0][9].lower()
            if restricted=='no':
                res.set(2)
            else:
                res.set(1)

            st_birth=str(rows[0][6])
            stu_bir=st_birth.split('-')
            st_birth=''
            st_birth=stu_bir[2]+'/'+stu_bir[1]+'/'+stu_bir[0]

            fullname1 = Entry(labelFrame,bg='#cecece',fg='black')
            fullname1.insert(0,str(rows[0][0]))
            fullname1.place(relx=0.5,rely=0.18,relwidth=0.3,relheight=0.06)
            fine1 = Entry(labelFrame,bg='#cecece',fg='black')
            fine1.insert(0,str(rows[0][7]))
            fine1.place(relx=0.5,rely=0.27,relwidth=0.3,relheight=0.06)
            email1 = Entry(labelFrame,bg='#cecece',fg='black')
            email1.insert(0,str(rows[0][4]))
            email1.place(relx=0.5,rely=0.36,relwidth=0.3,relheight=0.06)
            password1 = Entry(labelFrame,bg='#cecece',fg='black')
            password1.insert(0,str(rows[0][2]))
            password1.place(relx=0.5,rely=0.45,relwidth=0.3,relheight=0.06)
            contact1 = Entry(labelFrame,bg='#cecece',fg='black')
            contact1.insert(0,str(rows[0][3]))
            contact1.place(relx=0.5,rely=0.54,relwidth=0.3,relheight=0.06)
            dob1 = DateEntry(labelFrame, date_pattern='dd/mm/yyyy',bg='#cecece',fg='black')
            dob1.delete(0,'end')
            dob1.insert(0,st_birth)
            dob1.place(relx=0.5,rely=0.63,relwidth=0.15,relheight=0.06)
            batch1 = Entry(labelFrame,bg='#cecece',fg='black')
            batch1.insert(0,str(rows[0][5]))
            batch1.place(relx=0.5,rely=0.72,relwidth=0.3,relheight=0.06)
            course1 = Entry(labelFrame,bg='#cecece',fg='black')
            course1.insert(0,str(rows[0][8]))
            course1.place(relx=0.5,rely=0.81,relwidth=0.3,relheight=0.06)
            re1= Radiobutton(labelFrame, text="Yes",bg='#cecece',fg='black')
            re1.place(relx=0.5,rely=0.90,relwidth=0.12,relheight=0.06)
            re1.config(variable=res, val=1)
            re2= Radiobutton(labelFrame, text="No",bg='#cecece',fg='black')
            re2.place(relx=0.65,rely=0.90,relwidth=0.12,relheight=0.06)
            re2.config(variable=res, val=2)

            update=Button(labelFrame,text='Update',bg='#7d7d7d',fg='black',command=update_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


        details=Label(labelFrame,text="Update Student Details:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        user=Label(labelFrame,text="Registration Number",bg='black',fg='white').place(relx=0.1,rely=0.28,relwidth=0.25,relheight=0.08)
        st_reg = Entry(labelFrame,bg='#cecece',fg='black')
        st_reg.place(relx=0.5,rely=0.28,relwidth=0.3,relheight=0.08)
        delete=Button(labelFrame,text='Proceed',bg='#7d7d7d',fg='black',command=up_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


    #update FUNCTION
    def up_stu(regi):
        #regi=str(st_reg.get())
        for widget in labelFrame.winfo_children():
            widget.destroy()

        cur.execute("select * from student where Regno='"+ regi +"'")
        rows=list(cur.fetchall())

        def update_stu():
            fname=str(fullname1.get())
            fine=str(fine1.get())
            mail=str(email1.get())
            passwrd=str(password1.get())
            cont=str(contact1.get())
            dob=str(dob1.get())
            batch=str(batch1.get())
            course=str(course1.get())
            rest='no'
            if(res.get()==1):
                rest='yes'
            bir=dob.split('/')
            dob=''
            if len(bir[2])==4:
                dob=bir[2]+'-'+bir[1]+'-'+bir[0]
            else:
                dob='20'+bir[2]+'-'+bir[1]+'-'+bir[0]

            if(fname=='' or fine=="" or mail=="" or cont==None or dob==None or batch=="" or course=="" or passwrd=="")!=False:
                messagebox.showinfo("Can't ADD","All feilds are required!")
            elif(mail.endswith('@iiitkottayam.ac.in'))!=True:
                messagebox.showinfo("Invalid Email","Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
            elif(cont.isnumeric() and len(cont)==10)!=True:
                messagebox.showinfo("Invalid Contact Number","Enter a valid Contact Number(Length 10)!")
            elif (batch.isnumeric())!=True:
                messagebox.showinfo("Invalid Batch","Batch should be number and in format '20XX' !")
            else:
                try:
                    #addformula="INSERT INTO Student (Sname, Regno, Password, Phone, Email, Batch, DOB, Fine, Stream_id, is_restricted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    #add_student=(fname,usern,passwrd,cont,mail,batch,dob,fine,course,rest)
                    #cur.execute(addformula, add_student)
                    cur.execute("UPDATE Student SET Sname='"+ fname +"',Password='"+ passwrd +"',Phone='"+ cont +"',Email='"+ mail +"',Batch='"+ batch +"',DOB='"+ dob +"',Fine='"+ fine +"',Course='"+ course +"',is_restricted='"+ rest +"' WHERE Regno='"+ regi +"'")
                    con.commit()
                    fullname1.delete(0,'end')
                    fine1.delete(0,'end')
                    email1.delete(0,'end')
                    password1.delete(0,'end')
                    contact1.delete(0,'end')
                    dob1.delete(0,'end')
                    batch1.delete(0,'end')
                    course1.delete(0,'end')
                    messagebox.showinfo("Student Updated","Student Details are updated successfully!")
                    updates()
                except:
                    messagebox.showinfo("Can't Update Student","Oops!!\nSomething went wrong!!")


        details=Label(labelFrame,text="Enter Details to Update:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        fullname=Label(labelFrame,text="Full name",bg='black',fg='white').place(relx=0.1,rely=0.18,relwidth=0.25,relheight=0.07)
        fine=Label(labelFrame,text="Fine",bg='black',fg='white').place(relx=0.1,rely=0.27,relwidth=0.25,relheight=0.07)
        email=Label(labelFrame,text="Email Id",bg='black',fg='white').place(relx=0.1,rely=0.36,relwidth=0.25,relheight=0.07)
        password=Label(labelFrame,text="Password",bg='black',fg='white').place(relx=0.1,rely=0.45,relwidth=0.25,relheight=0.07)
        contact=Label(labelFrame,text="Contact no.",bg='black',fg='white').place(relx=0.1,rely=0.54,relwidth=0.25,relheight=0.07)
        dob=Label(labelFrame,text="Date Of Birth",bg='black',fg='white').place(relx=0.1,rely=0.63,relwidth=0.25,relheight=0.07)
        batch=Label(labelFrame,text="Batch",bg='black',fg='white').place(relx=0.1,rely=0.72,relwidth=0.25,relheight=0.07)
        course=Label(labelFrame,text="Course",bg='black',fg='white').place(relx=0.1,rely=0.81,relwidth=0.25,relheight=0.07)
        restrict=Label(labelFrame,text="Is Restricted?",bg='black',fg='white').place(relx=0.1,rely=0.90,relwidth=0.25,relheight=0.07)

        res=IntVar()
        restricted=rows[0][9].lower()
        if restricted=='no':
            res.set(2)
        else:
            res.set(1)

        st_birth=str(rows[0][6])
        stu_bir=st_birth.split('-')
        st_birth=''
        st_birth=stu_bir[2]+'/'+stu_bir[1]+'/'+stu_bir[0]

        fullname1 = Entry(labelFrame,bg='#cecece',fg='black')
        fullname1.insert(0,str(rows[0][0]))
        fullname1.place(relx=0.5,rely=0.18,relwidth=0.3,relheight=0.06)
        fine1 = Entry(labelFrame,bg='#cecece',fg='black')
        fine1.insert(0,str(rows[0][7]))
        fine1.place(relx=0.5,rely=0.27,relwidth=0.3,relheight=0.06)
        email1 = Entry(labelFrame,bg='#cecece',fg='black')
        email1.insert(0,str(rows[0][4]))
        email1.place(relx=0.5,rely=0.36,relwidth=0.3,relheight=0.06)
        password1 = Entry(labelFrame,bg='#cecece',fg='black')
        password1.insert(0,str(rows[0][2]))
        password1.place(relx=0.5,rely=0.45,relwidth=0.3,relheight=0.06)
        contact1 = Entry(labelFrame,bg='#cecece',fg='black')
        contact1.insert(0,str(rows[0][3]))
        contact1.place(relx=0.5,rely=0.54,relwidth=0.3,relheight=0.06)
        dob1 = DateEntry(labelFrame, date_pattern='dd/mm/yyyy',bg='#cecece',fg='black')
        dob1.delete(0,'end')
        dob1.insert(0,st_birth)
        dob1.place(relx=0.5,rely=0.63,relwidth=0.15,relheight=0.06)
        batch1 = Entry(labelFrame,bg='#cecece',fg='black')
        batch1.insert(0,str(rows[0][5]))
        batch1.place(relx=0.5,rely=0.72,relwidth=0.3,relheight=0.06)
        course1 = Entry(labelFrame,bg='#cecece',fg='black')
        course1.insert(0,str(rows[0][8]))
        course1.place(relx=0.5,rely=0.81,relwidth=0.3,relheight=0.06)
        re1= Radiobutton(labelFrame, text="Yes",bg='#cecece',fg='black')
        re1.place(relx=0.5,rely=0.90,relwidth=0.12,relheight=0.06)
        re1.config(variable=res, val=1)
        re2= Radiobutton(labelFrame, text="No",bg='#cecece',fg='black')
        re2.place(relx=0.65,rely=0.90,relwidth=0.12,relheight=0.06)
        re2.config(variable=res, val=2)

        update=Button(labelFrame,text='Update',bg='#7d7d7d',fg='black',command=update_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


    #restrict student
    def restricts():
        for widget in labelFrame.winfo_children():
             widget.destroy()


        def rest_stu():
            st_res=str(st_rest.get())
            y='Yes'
            cur.execute("UPDATE Student SET is_restricted='"+ 'Yes' +"' WHERE Regno='"+ st_res +"'")
            val='restrict_student'
            s_bid='Student'
            try:
                check_mail(st_res,val,s_bid)
                con.commit()
                st_rest.delete(0,'end')
                messagebox.showinfo("Student Restricted","Student is Restricted successfully!")
            except:
                messagebox.showwarning("Error","Error in sending mail..\nLogin to email to perform the action!!")

        details=Label(labelFrame,text="Restrict Student:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        st_res=Label(labelFrame,text="Registration Number",bg='black',fg='white').place(relx=0.1,rely=0.28,relwidth=0.25,relheight=0.08)
        st_rest = Entry(labelFrame,bg='#cecece',fg='black')
        st_rest.place(relx=0.5,rely=0.28,relwidth=0.3,relheight=0.08)
        delete=Button(labelFrame,text='Restrict',bg='#7d7d7d',fg='black',command=rest_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


    #pending books at student
    def pending_stu(reg):
        x=reg
        for widget in labelFrame.winfo_children():
             widget.destroy()

        ls = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        ls.place(relx=0.04, rely=0.04,relwidth=0.92,relheight=0.92)

        #def show():
        ls.delete(0,'end')
        #start
        h = Scrollbar(ls, orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(ls)
        v.pack(side = RIGHT, fill = Y)
        t = Text(ls, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
        #end
        cur.execute("select student.Sname,student.Regno,book.bname,SubBook.Sub_bid, Borrow.Approved_date,Borrow.borrow_id From student,Book,SubBook,Borrow where Book.Bid = SubBook.Bid and Student.Regno = Borrow.student_regno and SubBook.Sub_bid = Borrow.Sub_bid and Student.Regno='"+ x +"' ")
        rows=list(cur.fetchall())
        reg=Label(ls,text='Reg.No.',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='w')
        t.window_create(END,window=reg)
        s_name=Label(ls,text='Name',bg='#97cee3',fg='white',width=17,font='BOLD', anchor='w')
        t.window_create(END,window=s_name)
        s_bookname=Label(ls,text='book name',bg='#97cee3',fg='white',width=25,font='BOLD', anchor='w')
        t.window_create(END,window=s_bookname)
        s_sub_id=Label(ls,text='sub bookid',bg='#97cee3',fg='white',width=13,font='BOLD', anchor='c')
        t.window_create(END,window=s_sub_id)
        s_borrow=Label(ls,text='borrow date',bg='#97cee3',fg='white',font='BOLD',width=13, anchor='c')
        t.window_create(END,window=s_borrow)
        s_borrowid=Label(ls,text='borrow id',bg='#97cee3',fg='white',width=13,font='BOLD', anchor='c')
        t.window_create(END,window=s_borrowid)
        s_receive=Label(ls,text='Receive book',bg='#97cee3',fg='white', font='BOLD',width=10 , anchor='c')
        t.window_create(END,window=s_receive)

        t.insert(END,"\n")
        for row in rows:
            val=row
            reg=Label(ls,text=row[1],bg='yellow',fg='black',width=13, anchor='w')
            t.window_create(END,window=reg)
            s_name=Label(ls,text=row[0],bg='yellow',fg='black',width=22, anchor='w')
            t.window_create(END,window=s_name)
            s_bookid=Label(ls,text=row[2],bg='yellow',fg='black',width=35, anchor='w')
            t.window_create(END,window=s_bookid)
            s_sub_id=Label(ls,text=row[3],bg='yellow',fg='black',width=15, anchor='c')
            t.window_create(END,window=s_sub_id)
            s_borrow=Label(ls,text=row[4],bg='yellow',fg='black',width=16, anchor='c')
            t.window_create(END,window=s_borrow)
            s_borrowid=Label(ls,text=row[5],bg='yellow',fg='black',width=14, anchor='c')
            t.window_create(END,window=s_borrowid)
            s_receive=Button(ls,text='Recieve Book',bg='grey',fg='black',command= (lambda x=val : b_receive(x)),width=14, anchor='c')
            t.window_create(END,window=s_receive)
            t.insert(END,"\n")

        #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        #end

    #sending mail to particular student after search
    def mail_stu(reg_no):
        global admin_email_password
        global window1
        def send_mail():
            '''def dis():
                window1.distroy()
            global admin_email_password'''
            #global window1
            try:
                sub_m=str(sub_entry.get('1.0','end-1c'))
                msg_m=str(msg_entry.get('1.0','end-1c'))
                #print(sub_m+'\n'+msg_m)
                msg= MIMEMultipart()
                msg['From'] = "ADMIN IIIT KOTTAYAM"
                msg['To'] = name_s
                msg['Subject'] =sub_m
                body = msg_m
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                sm= smtplib.SMTP('smtp.gmail.com', 587)
                sm.starttls()
                sm.login(mail_admin, admin_email_password)
                sm.sendmail(mail_admin, mail_s, text)
                sm.quit()
                messagebox.showinfo('Mail Status','Mail is sent Successfully..!')
                #window1.distroy()

            except Exception as e:
                print(e)
                messagebox.showinfo('Mail Status','Mail could not be sent.\nPlease login to the mail under "Access Mail" section to perform the action.\nOr check Your mail settings..! ')


        if reg_no=='mail_student':
            cur.execute("select Sname,Email from student ")
            data_s=list(cur.fetchall())
            name_s=[i[0] for i in data_s]
            mail_s=[i[1] for i in data_s]
        elif reg_no=='mail_admin':
            cur.execute("select aname,Email from admin")
            data_s=list(cur.fetchall())
            name_s=[i[0] for i in data_s]
            mail_s=[i[1] for i in data_s]
        elif reg_no=='mail_iiitk':
            cur.execute("select sname,Email from student")
            data_s=list(cur.fetchall())
            cur.execute("select aname,Email from admin")
            data_a=list(cur.fetchall())
            name_s=[i[0] for i in data_s]+[i[0] for i in data_a]
            mail_s=[i[1] for i in data_s]+[i[1] for i in data_a]
        else:
            cur.execute("select Sname,Email from student where Regno='"+ str(reg_no) +"'")
            data_s=list(cur.fetchall())
            name_s=data_s[0][0]
            mail_s=data_s[0][1]
        window1 = Toplevel(admin)
        window1.geometry('500x500+50+50')
        window1.resizable(False,False)
        canvas = Canvas(window1)
        canvas.config(bg="#c9f0ff")
        canvas.pack(expand=True,fill=BOTH)
        sub=Label(window1,text='Subject:',bg='#519790',fg='black',font=12).place(relx=0.04,rely=0.06,relwidth=0.2,relheight=0.07)
        sub_entry=Text(window1,bg='white',fg='#464646',font=12)
        sub_entry.place(relx=0.25,rely=0.06,relwidth=0.71,relheight=0.15)
        msg=Label(window1,text='Message:',bg='#519790',fg='black',font=12).place(relx=0.04,rely=0.22,relwidth=0.2,relheight=0.07)
        msg_entry=Text(window1,bg='white',fg='#323c36',font=12)
        msg_entry.place(relx=0.25,rely=0.22,relwidth=0.71,relheight=0.68)
        okBtn = Button(window1,text="Send",bg='green', fg='black', command=send_mail)
        okBtn.place(relx=0.78,rely=0.92, relwidth=0.18,relheight=0.05)
        quitBtn = Button(window1,text="Cancel",bg='orange', fg='black', command=window1.destroy)
        quitBtn.place(relx=0.25,rely=0.92, relwidth=0.18,relheight=0.05)


    # Manage Students

    lb1 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Manage Students',menu=lb1)
    lb1.add_command(label='Add Student',command=adds)
    lb1.add_command(label='Update Details',command=updates)
    lb1.add_command(label='View Students',command=views)
    lb1.add_separator()
    lb1.add_command(label='Delete Student',command=deletes)
    lb1.add_command(label='Restrict Student',command=restricts)




    #FUNCTION TO VIEW LIBRARY
    def view():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        lboxs.place(relx=0.02, rely=0.04,relwidth=0.94,relheight=0.91)

        #print_his()
        def print_his():
            reg_no=str(reg.get())
            print(reg_no)

        #def show():
        lboxs.delete(0,'end')
        #start
        v = Scrollbar(labelFrame, orient='vertical')
        #v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side = RIGHT, fill = Y)
        h = Scrollbar(labelFrame, orient = 'horizontal')
        #h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side = BOTTOM, fill = X)
        t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
        #end
        cur.execute("select Bid, Bname, Author, Subject_name, CName, Rating from book order by Bid")
        rows=list(cur.fetchall())



        b_id=Label(lboxs,text='Book ID',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='w')
        t.window_create(END,window=b_id)
        b_name=Label(lboxs,text='Book Name',bg='#97cee3',fg='white',width=25,font='BOLD', anchor='w')
        t.window_create(END,window=b_name)
        author=Label(lboxs,text='Author',bg='#97cee3',fg='white',width=20,font='BOLD', anchor='c')
        t.window_create(END,window=author)
        b_numb=Label(lboxs,text='Number of Books',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='c')
        t.window_create(END,window=b_numb)
        b_course=Label(lboxs,text='Course',bg='#97cee3',fg='white',font='BOLD',width=12, anchor='c')
        t.window_create(END,window=b_course)
        b_subject=Label(lboxs,text='Subject',bg='#97cee3',fg='white',width=12,font='BOLD', anchor='c')
        t.window_create(END,window=b_subject)
        b_rating=Label(lboxs,text='Rating',bg='#97cee3',fg='white',width=11,font='BOLD', anchor='c')
        t.window_create(END,window=b_rating)
        t.insert(END,"\n")


        for row in rows:
            x = str(row[0])
            count_val = cur.execute("select count(*) from subbook where Bid='"+ x +"'")
            count_list=list(cur.fetchall())

            reg=Label(lboxs,bg='#c9ffa0',fg='black',width=13, anchor='w',text=row[0])#)#, anchor='w',text=row[0]
            #reg.delete(0,'end')
            #reg.insert(0,row[0])
            #reg.configure(state='readonly')
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text=row[1],bg='#c9ffa0',fg='black',width=42, anchor='w')
            t.window_create(END,window=s_name)
            s_mail=Label(lboxs,text=row[2],bg='#c9ffa0',fg='black',width=23, anchor='w')
            t.window_create(END,window=s_mail)
            s_phone=Label(lboxs,text=count_list[0],bg='#c9ffa0',fg='black',width=10, anchor='w')
            t.window_create(END,window=s_phone)
            s_batch=Label(lboxs,text=row[3],bg='#c9ffa0',fg='black',width=17, anchor='c')
            t.window_create(END,window=s_batch)
            s_course=Label(lboxs,text=row[4],bg='#c9ffa0',fg='black',width=18, anchor='c')
            t.window_create(END,window=s_course)
            s_fine=Label(lboxs,text=row[5],bg='#c9ffa0',fg='black',width=12, anchor='c')
            t.window_create(END,window=s_fine)
            t.insert(END,"\n")
                #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                #lboxs.insert(lboxs.size()+1, insertdata)
                #t.insert(END,insertdata)
            #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
            #end


    #Adding Books
    #Adding Books
    def add_book():
        for widget in labelFrame.winfo_children():
            widget.destroy()


        lbox_ch = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        lbox_ch.place(relx=0.03, rely=0.59,relwidth=0.94,relheight=0.37)

        #print_his()
        '''def print_his():
            reg_no=str(reg.get())
            print(reg_no)'''

        #def show():
        #lboxs.delete(0,'end')

        def check():
            #def show():
            lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
            lboxs.place(relx=0.03, rely=0.59,relwidth=0.94,relheight=0.37)

            lboxs.delete(0,'end')
            #start
            h = Scrollbar(lboxs, orient = 'horizontal')
            h.pack(side = BOTTOM, fill = X)
            v = Scrollbar(lboxs)
            v.pack(side = RIGHT, fill = Y)
            t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)

            Subject_name = str(e_subject.get())
            CName = str(e_category.get())
            #Bid = str(e_bid.get())
            #Bname = str(e_bname.get())
            #Author = str(e_author.get())
            Rating = '0.0'
            Thumbnail = None

            select_state = "select Book.Bid, Book.Bname, Book.Author from book where Subject_name = '"+ Subject_name +"' and CName = '"+ CName +"' ORDER BY Bid"
            cur.execute(select_state)
            rows=list(cur.fetchall())

            reg=Label(lboxs,text='Book ID',bg='#97cee3',fg='white',width=16,font='BOLD', anchor='w')#, state='disabled')#, anchor='w')
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text='Book Name',bg='#97cee3',fg='white',width=32,font='BOLD', anchor='w')
            t.window_create(END,window=s_name)
            s_author=Label(lboxs,text='Author',bg='#97cee3',fg='white',width=22,font='BOLD', anchor='w')
            t.window_create(END,window=s_author)
            s_num=Label(lboxs,text='Number of books',bg='#97cee3',fg='white',width=16,font='BOLD', anchor='c')
            t.window_create(END,window=s_num)
            s_history=Label(lboxs,text='ADD',bg='#97cee3',fg='white', font='BOLD',width=18 , anchor='c')
            t.window_create(END,window=s_history)
            t.insert(END,"\n")

            def add_old(val):
                cur.execute("insert into subbook (Bid) values('"+ str(val) +"')")
                cur.execute("commit")
                check()

            for row in rows:
                lboxs.delete(0,'end')

                x = str(row[0])
                count_val = cur.execute("select count(*) from subbook where Bid='"+ x +"'")
                count_list=list(cur.fetchall())

                bid=Label(lboxs,text=row[0],bg='yellow',fg='black',width=20, anchor='w')
                t.window_create(END,window=bid)
                bname=Label(lboxs,text=row[1],bg='yellow',fg='black',width=40, anchor='w')
                t.window_create(END,window=bname)
                author=Label(lboxs,text=row[2],bg='yellow',fg='black',width=30, anchor='w')
                t.window_create(END,window=author)
                numb=Label(lboxs,text=count_list[0],bg='yellow',fg='black',width=25, anchor='c')
                t.window_create(END,window=numb)
                ADD=Button(lboxs,text='ADD',bg='grey',fg='black',command= (lambda x=row[0] : add_old(x)),width=18, anchor='c')
                t.window_create(END,window=ADD)
                t.insert(END,"\n")
                    #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                    #lboxs.insert(lboxs.size()+1, insertdata)
                    #t.insert(END,insertdata)
            #start
            t.configure(state="disabled")
            t.pack(side=TOP, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)
                #end


        Subject_name = Label(labelFrame,text="SUBJECT",bg="black",fg="white",anchor='w')
        Subject_name.place(relx=0.15,rely=0.12,relwidth=0.2,relheight=0.06)

        CName = Label(labelFrame,text="CATEGORY",bg="black",fg="white",anchor='w')
        CName.place(relx=0.15,rely=0.20,relwidth=0.2,relheight=0.06)

        #Bid = Label(labelFrame,text="BOOK ID",bg="black",fg="white",anchor='w')
        #Bid.place(relx=0.15,rely=0.28,relwidth=0.2,relheight=0.06)

        Bname= Label(labelFrame,text="BOOK_NAME",bg="black",fg="white",anchor='w')
        Bname.place(relx=0.15,rely=0.36,relwidth=0.2,relheight=0.06)

        Author = Label(labelFrame,text="AUTHOR",bg="black",fg="white",anchor='w')
        Author.place(relx=0.15,rely=0.44,relwidth=0.2,relheight=0.06)



        e_subject = Entry(labelFrame)
        e_subject.place(relx=0.48,rely=0.12,relwidth=0.3,relheight=0.06)

        e_category = Entry(labelFrame)
        e_category.place(relx=0.48,rely=0.20,relwidth=0.3,relheight=0.06)

        #e_bid = Entry(labelFrame)
        #e_bid.place(relx=0.48,rely=0.28,relwidth=0.3,relheight=0.06)

        e_bname = Entry(labelFrame)
        e_bname.place(relx=0.48,rely=0.36,relwidth=0.3,relheight=0.06)

        e_author = Entry(labelFrame)
        e_author.place(relx=0.48,rely=0.44,relwidth=0.3,relheight=0.06)


        def add_new():
            Subject_name = e_subject.get()
            CName = e_category.get()
            #Bid = e_bid.get()
            Bname = e_bname.get()
            Author = e_author.get()
            Rating = '0.0'
            Thumbnail = 'None'
            if(Subject_name=='' or CName=='' or Bname=='' or Author==''):# or Bid==''
                messagebox.showinfo("Insert Status", "All fields are required!")
            else:
                try:
                    cur.execute("insert into Subject values('"+ Subject_name +"')")
                    con.commit()
                    try:
                        cur.execute("insert into Category values('"+ CName +"','"+ Subject_name +"')")
                        con.commit()
                    except Exception as e:
                        #print(e) 
                        pass   
                except Exception as e:
                    #print(e)
                    try:
                        cur.execute("insert into Category values('"+ CName +"','"+ Subject_name +"')")
                        con.commit()
                    except Exception as e:
                        #print(e)
                        pass  
                    

                try:
                    add_new_book_formula="INSERT INTO book (Bname, Author, Rating, Subject_name, CName, Thumbnail) VALUES (%s, %s, %s, %s, %s, %s)"
                    add_book=(Bname,Author,Rating,Subject_name,CName,Thumbnail)
                    cur.execute(add_new_book_formula,add_book)
                    con.commit()
                    #
                    #command='insert into '
                    #
                    messagebox.showinfo("Insert Status","Successfully inserted into database")
                except Exception as e:
                    print(e)
                    messagebox.showinfo("Error!","coudn't add book\nSomething went wrong")    

                #e_bid.delete(0, 'end')
                e_bname.delete(0, 'end')
                e_author.delete(0, 'end')

                check()

        Check = Button(labelFrame,text="Check",fg="black",bg="#7d7d7d",command=check)
        Check.place(relx=0.80,rely=0.20,relwidth=0.14,relheight=0.06)

        ADD = Button(labelFrame,text="ADD NEW BOOK",fg="black",bg="#7d7d7d",command=add_new)
        ADD.place(relx=0.80,rely=0.44,relwidth=0.14,relheight=0.06)
    #FUNCTION FOR DELETING BOOK

    def delete():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="#cecece", relief="sunken",font=("courier",15),fg="white")
        lboxs.place(relx=0.03, rely=0.59,relwidth=0.94,relheight=0.37)

        def check():
            for widget in lboxs.winfo_children():
                widget.destroy()
            #lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
            #lboxs.place(relx=0.03, rely=0.59,relwidth=0.94,relheight=0.37)

            #def show():
            lboxs.delete(0,'end')
            #start
            h = Scrollbar(lboxs, orient = 'horizontal')
            h.pack(side = BOTTOM, fill = X)
            v = Scrollbar(lboxs)
            v.pack(side = RIGHT, fill = Y)
            t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)

            Subject_name = str(e_subject.get())
            CName = str(e_category.get())
            Bid = e_bid.get()

            select_state = "select Book.Bid, Book.Bname, Book.Author, Book.Rating from book where Subject_name = '"+ Subject_name +"' and CName = '"+ CName +"' ORDER BY Bid"
            cur.execute(select_state)
            rows=list(cur.fetchall())

            reg=Label(lboxs,text='Book ID',bg='#97cee3',fg='white',width=16,font='BOLD', anchor='w')#, state='disabled')#, anchor='w')
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text='Book Name',bg='#97cee3',fg='white',width=32,font='BOLD', anchor='w')
            t.window_create(END,window=s_name)
            s_author=Label(lboxs,text='Author',bg='#97cee3',fg='white',width=22,font='BOLD', anchor='w')
            t.window_create(END,window=s_author)
            s_num=Label(lboxs,text='Number of books',bg='#97cee3',fg='white',width=16,font='BOLD', anchor='c')
            t.window_create(END,window=s_num)
            s_rating=Label(lboxs,text='Rating',bg='#97cee3',fg='white',width=18,font='BOLD', anchor='c')
            t.window_create(END,window=s_rating)
            t.insert(END,"\n")

            for row in rows:
                lboxs.delete(0,'end')
                bid=Label(lboxs,text=row[0],bg='yellow',fg='black',width=20, anchor='w')
                t.window_create(END,window=bid)
                bname=Label(lboxs,text=row[1],bg='yellow',fg='black',width=40, anchor='w')
                t.window_create(END,window=bname)
                author=Label(lboxs,text=row[2],bg='yellow',fg='black',width=30, anchor='w')
                t.window_create(END,window=author)
                numb=Label(lboxs,text='1',bg='yellow',fg='black',width=25, anchor='c')
                t.window_create(END,window=numb)
                rat=Label(lboxs,text=row[3],bg='yellow',fg='black',width=19, anchor='c')
                t.window_create(END,window=rat)
                t.insert(END,"\n")

            t.configure(state="disabled")
            t.pack(side=TOP, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)

        Subject_name = Label(labelFrame,text="SUBJECT",bg="black",fg="white",anchor='w')
        Subject_name.place(relx=0.15,rely=0.12,relwidth=0.2,relheight=0.06)

        CName = Label(labelFrame,text="CATEGORY",bg="black",fg="white",anchor='w')
        CName.place(relx=0.15,rely=0.20,relwidth=0.2,relheight=0.06)

        Bid = Label(labelFrame,text="BOOK ID",bg="black",fg="white",anchor='w')
        Bid.place(relx=0.15,rely=0.36,relwidth=0.2,relheight=0.06)

        e_subject = Entry(labelFrame,bg='#cecece',fg='black')
        e_subject.place(relx=0.48,rely=0.12,relwidth=0.3,relheight=0.06)

        e_category = Entry(labelFrame,bg='#cecece',fg='black')
        e_category.place(relx=0.48,rely=0.20,relwidth=0.3,relheight=0.06)

        e_bid = Entry(labelFrame,bg='#cecece',fg='black')
        e_bid.place(relx=0.48,rely=0.36,relwidth=0.3,relheight=0.06)

        def remove():
            Bid = e_bid.get()

            if(Bid==""):
                messagebox.showinfo("Insert Status", "All fields are required!")
            elif(Bid.isdigit() is False):
                messagebox.showinfo("Insert Status","BOOK ID should be an integer")
            else:
                cur.execute("delete from subbook where Bid='" + Bid + "'")
                con.commit()
                cur.execute("delete from book where Bid='"+ Bid +"'")
                cur.execute("commit")
                messagebox.showinfo("Delete Status","Successfully deleted from database")
            #e_subject.delete(0, 'end')
            #e_category.delete(0, 'end')
            e_bid.delete(0, 'end')

            check()

        Check = Button(labelFrame,text="Check",fg="black",bg="#7d7d7d",command=check)
        Check.place(relx=0.80,rely=0.20,relwidth=0.14,relheight=0.06)

        DELETE = Button(labelFrame,text="DELETE BOOK",fg="black",bg="#7d7d7d",command=remove)
        DELETE.place(relx=0.80,rely=0.36,relwidth=0.14,relheight=0.06)

    #Update Book Details
    def book_update():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="#cecece", relief="sunken",font=("courier",15),fg="white")
        lboxs.place(relx=0.03, rely=0.55,relwidth=0.94,relheight=0.42)

        def check():
            for widget in lboxs.winfo_children():
                widget.destroy()
            #lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
            #lboxs.place(relx=0.03, rely=0.55,relwidth=0.94,relheight=0.42)

            lboxs.delete(0,'end')

            def add_old(val):
                cur.execute("insert into subbook (Bid) values('"+ str(val) +"')")
                con.commit()
                check()

            #start
            h = Scrollbar(lboxs, orient = 'horizontal')
            h.pack(side = BOTTOM, fill = X)
            v = Scrollbar(lboxs)
            v.pack(side = RIGHT, fill = Y)
            t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)

            Subject_name = str(e_subject.get())
            CName = str(e_category.get())
            #Bid = str(e_bid.get())
            #Bname = str(e_bname.get())
            #Author = str(e_author.get())
            Rating = '0.0'
            Thumbnail = None

            select_state = "select Book.Bid, Book.Bname, Book.Author, book.Rating from book where Subject_name = '"+ Subject_name +"' and CName = '"+ CName +"' ORDER BY Bid"
            cur.execute(select_state)
            rows=list(cur.fetchall())

            reg=Label(lboxs,text='Book ID',bg='#97cee3',fg='white',width=16,font='BOLD', anchor='w')#, state='disabled')#, anchor='w')
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text='Book Name',bg='#97cee3',fg='white',width=32,font='BOLD', anchor='w')
            t.window_create(END,window=s_name)
            s_author=Label(lboxs,text='Author',bg='#97cee3',fg='white',width=16,font='BOLD', anchor='w')
            t.window_create(END,window=s_author)
            s_num=Label(lboxs,text='Number of books',bg='#97cee3',fg='white',width=16,font='BOLD', anchor='c')
            t.window_create(END,window=s_num)
            s_rate=Label(lboxs,text='Rating',bg='#97cee3',fg='white',width=8,font='BOLD', anchor='c')
            t.window_create(END,window=s_rate)
            s_history=Label(lboxs,text='ADD',bg='#97cee3',fg='white', font='BOLD',width=16 , anchor='c')
            t.window_create(END,window=s_history)
            t.insert(END,"\n")

            for row in rows:
                lboxs.delete(0,'end')
                x=str(row[0])
                count_val = cur.execute("select count(*) from subbook where Bid='"+ x +"'")
                count_list=list(cur.fetchall())
                bid=Label(lboxs,text=row[0],bg='yellow',fg='black',width=20, anchor='w')
                t.window_create(END,window=bid)
                bname=Label(lboxs,text=row[1],bg='yellow',fg='black',width=40, anchor='w')
                t.window_create(END,window=bname)
                author=Label(lboxs,text=row[2],bg='yellow',fg='black',width=30, anchor='w')
                t.window_create(END,window=author)
                numb=Label(lboxs,text=count_list[0],bg='yellow',fg='black',width=12, anchor='c')
                t.window_create(END,window=numb)
                rating=Label(lboxs,text=row[3],bg='yellow',fg='black',width=13, anchor='c')
                t.window_create(END,window=rating)
                ADD=Button(lboxs,text='ADD',bg='grey',fg='black',command=(lambda x=row[0] : add_old(x)),width=18, anchor='c')
                t.window_create(END,window=ADD)
                t.insert(END,"\n")
                    #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                    #lboxs.insert(lboxs.size()+1, insertdata)
                    #t.insert(END,insertdata)
            #start
            t.configure(state="disabled")
            t.pack(side=TOP, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)
                #end


        Subject_name = Label(labelFrame,text="SUBJECT",bg="black",fg="white",anchor='w')
        Subject_name.place(relx=0.15,rely=0.06,relwidth=0.2,relheight=0.06)

        CName = Label(labelFrame,text="CATEGORY",bg="black",fg="white",anchor='w')
        CName.place(relx=0.15,rely=0.14,relwidth=0.2,relheight=0.06)

        Bid = Label(labelFrame,text="BOOK ID(Not to be Updated)",bg="black",fg="white",anchor='w')
        Bid.place(relx=0.15,rely=0.22,relwidth=0.2,relheight=0.06)

        Bname= Label(labelFrame,text="BOOK_NAME",bg="black",fg="white",anchor='w')
        Bname.place(relx=0.15,rely=0.30,relwidth=0.2,relheight=0.06)

        Author = Label(labelFrame,text="AUTHOR",bg="black",fg="white",anchor='w')
        Author.place(relx=0.15,rely=0.38,relwidth=0.2,relheight=0.06)

        Rating = Label(labelFrame,text="RATING",bg="black",fg="white",anchor='w')
        Rating.place(relx=0.15,rely=0.46,relwidth=0.2,relheight=0.06)



        e_subject = Entry(labelFrame,bg='#cecece',fg='black')
        e_subject.place(relx=0.48,rely=0.06,relwidth=0.3,relheight=0.06)

        e_category = Entry(labelFrame,bg='#cecece',fg='black')
        e_category.place(relx=0.48,rely=0.14,relwidth=0.3,relheight=0.06)

        e_bid = Entry(labelFrame,bg='#cecece',fg='black')
        e_bid.place(relx=0.48,rely=0.22,relwidth=0.3,relheight=0.06)

        e_bname = Entry(labelFrame,bg='#cecece',fg='black')
        e_bname.place(relx=0.48,rely=0.30,relwidth=0.3,relheight=0.06)

        e_author = Entry(labelFrame,bg='#cecece',fg='black')
        e_author.place(relx=0.48,rely=0.38,relwidth=0.3,relheight=0.06)

        e_rating = Entry(labelFrame,bg='#cecece',fg='black')
        e_rating.place(relx=0.48,rely=0.46,relwidth=0.3,relheight=0.06)

        def b_update():
            Subject_name = e_subject.get()
            CName = e_category.get()
            Bid = e_bid.get()
            Bname = e_bname.get()
            Author = e_author.get()
            Rating = e_rating.get()
            Thumbnail = 'None'
            if(Subject_name==''or Bid=='' or CName=='' or Bname=='' or Author=='' or Rating==''):# or Bid==''
                messagebox.showinfo("Update Status", "All fields are required!")
            else:
                try:
                    cur.execute("insert into Subject values('"+ Subject_name +"')")
                    cur.execute("insert into Category values('"+ CName +"','"+ Subject_name +"')")
                except(mysql.connector.errors.IntegrityError):
                    pass

                cur.execute("UPDATE book SET Bname='"+ Bname +"',Author='"+ Author +"',Rating='"+ Rating +"',Subject_name='"+ Subject_name +"',CName='"+ CName +"',Thumbnail='"+ Thumbnail +"' WHERE Bid='"+ str(Bid) +"'")
                con.commit()

                #add_new_book_formula="INSERT INTO book (Bname, Author, Rating, Subject_name, CName, Thumbnail) VALUES (%s, %s, %s, %s, %s, %s)"
                #add_book=(Bname,Author,Rating,Subject_name,CName,Thumbnail)

                #cur.execute(add_new_book_formula,add_book)
                #cur.execute("commit")

                e_bid.delete(0, 'end')
                e_bname.delete(0, 'end')
                e_author.delete(0, 'end')
                e_rating.delete(0, 'end')

                messagebox.showinfo("Update Status","Successfully Updated into database")

                check()

        Check = Button(labelFrame,text="Check",fg="black",bg="#7d7d7d",command=check)
        Check.place(relx=0.80,rely=0.14,relwidth=0.14,relheight=0.06)

        ADD = Button(labelFrame,text="UPDATE BOOK",fg="black",bg="#7d7d7d",command=b_update)
        ADD.place(relx=0.80,rely=0.46,relwidth=0.14,relheight=0.06)


    #book status
    def b_status(bid):
        x=bid
        for widget in labelFrame.winfo_children():
            widget.destroy()

        cur.execute("select Bid, Bname, Author, Subject_name, CName, Rating from book where Bid='"+ str(x) +"'")
        rows=list(cur.fetchall())

        details=Label(labelFrame,text="Book Status",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        fullname=Label(labelFrame,text="Book ID",bg='black',fg='white').place(relx=0.1,rely=0.18,relwidth=0.25,relheight=0.07)
        username=Label(labelFrame,text="Book Name",bg='black',fg='white').place(relx=0.1,rely=0.27,relwidth=0.25,relheight=0.07)
        email=Label(labelFrame,text="Author",bg='black',fg='white').place(relx=0.1,rely=0.36,relwidth=0.25,relheight=0.07)
        password=Label(labelFrame,text="Course",bg='black',fg='white').place(relx=0.1,rely=0.45,relwidth=0.25,relheight=0.07)
        contact=Label(labelFrame,text="Subject",bg='black',fg='white').place(relx=0.1,rely=0.54,relwidth=0.25,relheight=0.07)
        dob=Label(labelFrame,text="Sub Book ID",bg='black',fg='white').place(relx=0.1,rely=0.63,relwidth=0.25,relheight=0.07)
        batch=Label(labelFrame,text="Stock of Library",bg='black',fg='white').place(relx=0.1,rely=0.72,relwidth=0.25,relheight=0.07)
        course=Label(labelFrame,text="Currently Available",bg='black',fg='white').place(relx=0.1,rely=0.81,relwidth=0.25,relheight=0.07)
        rating=Label(labelFrame,text="Rating",bg='black',fg='white').place(relx=0.1,rely=0.90,relwidth=0.25,relheight=0.07)

        fullname1 = Label(labelFrame,text=rows[0][0],bg='#cecece',fg='black')
        fullname1.place(relx=0.5,rely=0.18,relwidth=0.3,relheight=0.06)
        #print('fullname1',fullname1)
        username1 = Label(labelFrame, text=rows[0][1],bg='#cecece',fg='black')
        username1.place(relx=0.5,rely=0.27,relwidth=0.3,relheight=0.06)
        email1 = Label(labelFrame, text=rows[0][2],bg='#cecece',fg='black')
        email1.place(relx=0.5,rely=0.36,relwidth=0.3,relheight=0.06)
        password1 = Label(labelFrame, text=rows[0][4] ,bg='#cecece',fg='black')
        password1.place(relx=0.5,rely=0.45,relwidth=0.3,relheight=0.06)
        contact1 = Label(labelFrame, text=rows[0][3],bg='#cecece',fg='black')
        contact1.place(relx=0.5,rely=0.54,relwidth=0.3,relheight=0.06)
        cur.execute("select distinct sub_bid from subbook where bid='"+ str(x) +"'")
        sub_b=list(cur.fetchall())
        dob1 = Label(labelFrame,text=sub_b,bg='#cecece',fg='black')
        dob1.place(relx=0.5,rely=0.63,relwidth=0.3,relheight=0.06)
        cur.execute("select count(distinct sub_bid) from subbook where bid='"+ str(x) +"'")
        b_num=list(cur.fetchall())
        batch1 = Label(labelFrame,text=b_num[0][0],bg='#cecece',fg='black')
        batch1.place(relx=0.5,rely=0.72,relwidth=0.3,relheight=0.06)
        cur.execute("select count(distinct sub_bid) from subbook where is_available='yes' and bid='"+ str(x) +"'")
        stock=list(cur.fetchall())
        course1 = Label(labelFrame,text=stock[0][0],bg='#cecece',fg='black')
        course1.place(relx=0.5,rely=0.81,relwidth=0.3,relheight=0.06)
        rating1 = Label(labelFrame,text=rows[0][5],bg='#cecece',fg='black')
        rating1.place(relx=0.5,rely=0.90,relwidth=0.3,relheight=0.06)


    def update_book_all(val):
        x=val
        for widget in labelFrame.winfo_children():
            widget.destroy()

        def all_update():
            Subject_name = e_subject.get()
            CName = e_category.get()
            #Bid = e_bid.get()
            Bname = e_bname.get()
            Author = e_author.get()
            Rating = rating1.get()
            Thumbnail = thumbnail1.get()
            if(Subject_name=='' or CName=='' or Bname=='' or Author=='' or Rating=='' or Thumbnail==''):# or Bid==
                messagebox.showinfo("Insert Status", "All fields are required!")
            else:
                try:
                    cur.execute("insert into Subject values('"+ Subject_name +"')")
                    cur.execute("insert into Category values('"+ CName +"','"+ Subject_name +"')")
                except(mysql.connector.errors.IntegrityError):
                    pass


            cur.execute("UPDATE book SET Bname='"+ Bname +"',Author='"+ Author +"',Rating='"+ Rating +"',Subject_name='"+ Subject_name +"',CName='"+ CName +"',Thumbnail='"+ Thumbnail +"' WHERE Bid='"+ str(x) +"'")
            con.commit()

            #e_bid.delete(0, 'end')
            e_subject.delete(0, 'end')
            e_category.delete(0, 'end')
            rating1.delete(0, 'end')
            thumbnail1.delete(0, 'end')
            e_bname.delete(0, 'end')
            e_author.delete(0, 'end')

            messagebox.showinfo("Update Status","Successfully Updated into database")


        cur.execute("select Bname,Author,CName,Subject_name,Rating,Thumbnail from book where Bid='"+ str(x) +"'")
        rows=list(cur.fetchall())

        details=Label(labelFrame,text="Book Update",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        fullname=Label(labelFrame,text="Book Name",bg='black',fg='white').place(relx=0.1,rely=0.18,relwidth=0.25,relheight=0.07)
        username=Label(labelFrame,text="Author",bg='black',fg='white').place(relx=0.1,rely=0.27,relwidth=0.25,relheight=0.07)
        email=Label(labelFrame,text="Course",bg='black',fg='white').place(relx=0.1,rely=0.36,relwidth=0.25,relheight=0.07)
        password=Label(labelFrame,text="Subject",bg='black',fg='white').place(relx=0.1,rely=0.45,relwidth=0.25,relheight=0.07)
        contact=Label(labelFrame,text="Rating",bg='black',fg='white').place(relx=0.1,rely=0.54,relwidth=0.25,relheight=0.07)
        dob=Label(labelFrame,text="Thumbnail",bg='black',fg='white').place(relx=0.1,rely=0.63,relwidth=0.25,relheight=0.07)

        e_bname = Entry(labelFrame,bg='#cecece',fg='black')
        e_bname.insert(0,rows[0][0])
        e_bname.place(relx=0.5,rely=0.18,relwidth=0.3,relheight=0.06)
        #print('fullname1',fullname1)
        e_author = Entry(labelFrame,bg='#cecece',fg='black')
        e_author.insert(0,rows[0][1])
        e_author.place(relx=0.5,rely=0.27,relwidth=0.3,relheight=0.06)
        e_category = Entry(labelFrame,bg='#cecece',fg='black')
        e_category.insert(0,rows[0][2])
        e_category.place(relx=0.5,rely=0.36,relwidth=0.3,relheight=0.06)
        e_subject = Entry(labelFrame ,bg='#cecece',fg='black')
        e_subject.insert(0,rows[0][3])
        e_subject.place(relx=0.5,rely=0.45,relwidth=0.3,relheight=0.06)
        rating1 = Entry(labelFrame,bg='#cecece',fg='black')
        rating1.insert(0,rows[0][4])
        rating1.place(relx=0.5,rely=0.54,relwidth=0.3,relheight=0.06)
        thumbnail1 = Entry(labelFrame,bg='#cecece',fg='black')
        thumbnail1.insert(0,rows[0][5])
        thumbnail1.place(relx=0.5,rely=0.63,relwidth=0.3,relheight=0.06)

        add=Button(labelFrame,text='Update',bg='#7d7d7d',fg='black',command=all_update).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)



    # Manage Books

    lb2 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Manage Books',menu=lb2)
    lb2.add_command(label='View Library',command=view)
    #lb2.add_command(label='Issued Books',command=None)
    lb2.add_separator()
    lb2.add_command(label='Add Books',command=add_book)
    lb2.add_command(label='Update Book Details',command=book_update)
    lb2.add_command(label='Delete Book',command=delete)


    def check_mail(regno,val,s_bid):
        global admin_email_password
        cur.execute("select Sname,Email from student where Regno='"+ str(regno) +"'")
        data_s=list(cur.fetchall())
        name_s=data_s[0][0]
        mail_s=data_s[0][1]
        if val=='accept':
            sub_m='Book Request Approved'
            msg_m='Book Request for sub book id '+str(s_bid)+' is approved. You can collect it from the library.\nHave a great day ahead..'
        elif val=='deny':
            sub_m='Book Request Denied'
            msg_m='Book Request for sub book id '+str(s_bid)+' is denied.\nTry after some days!!'
        elif val=='return':
            sub_m='Book Return Request Approved'
            msg_m='Book Return Request for sub book id '+str(s_bid)+' is approved. Book is successfully accepted in the library.\n Have a nice day ahead..!'
        elif val=='add_student':
            sub_m='Welcome to IIIT Kottayam Library!'
            msg_m='You are now registered to access IIIT Kottayam Library.\nYour Registation Id and Password for login are '+regno+' and '+s_bid+' respectively.\nEnjoy Learning...\nFor any query or updating details contact to Library.\nHave a great day ahead!!'
        elif val=='update_student':
            sub_m='User Details Updated!'
            msg_m="Your Details are updated!\nContact to Library if you didn't request for any update!!\nHave a great day ahead!!"
        elif val=='restrict_student':
            sub_m='User access restricted!'
            msg_m="Attention user!!\n This is to inform you that you are now restricted to use IIIT Kottayam college library and you will not be able to access the college library.\nPlease contact to library in this regard.\nHave a great day ahead!!"
        elif val=='delete_student':
            sub_m='User No Longer Exists!'
            msg_m="This is to inform you that your details has been removed from the college database and you no longer allowed to access college library with the registration id and password provided to you.\n We wish you all the best for your future.\n Have a great day ahead!!"
        '''try:
            #print(sub_m+'\n'+msg_m)
            msg= MIMEMultipart()
            msg['From'] = "ADMIN IIIT KOTTAYAM"
            msg['To'] = name_s
            msg['Subject'] =sub_m
            body = msg_m
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            sm= smtplib.SMTP('smtp.gmail.com', 587)
            sm.starttls()
            sm.login(mail_admin, admin_email_password)
            sm.sendmail(mail_admin, mail_s, text)
            messagebox.showinfo('Mail Status','Mail is sent Successfully..!')
            sm.quit()
        except(smtplib.SMTPAuthenticationError):
            messagebox.showinfo('Mail Status','Mail could not be sent.\nPlease login to the mail under "Access Mail" section to perform the action.\nOr check Your mail settings..! ')
        except:
            messagebox.showinfo('Error','Some error happened in sending mail.Please send the mail manually!!')'''
        msg= MIMEMultipart()
        msg['From'] = "ADMIN IIIT KOTTAYAM"
        msg['To'] = name_s
        msg['Subject'] =sub_m
        body = msg_m
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        sm= smtplib.SMTP('smtp.gmail.com', 587)
        sm.starttls()
        sm.login(mail_admin, admin_email_password)
        sm.sendmail(mail_admin, mail_s, text)
        messagebox.showinfo('Mail Status','Mail is sent Successfully..!')
        sm.quit()


    # Pending files
    #pending Requests
    def pending_request():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        #refresh=Button(labelFrame, bg="black",fg="white")
        #refresh.place(relx=0.01,rely=0.01,relwidth=0.03,relheight=0.05)

        ls = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        ls.place(relx=0.04, rely=0.04,relwidth=0.92,relheight=0.92)

        def r_accept(r_a_val):
            x=r_a_val
            d1 = today.strftime("%Y-%m-%d")
            cur.execute("select is_available from subbook where sub_bid='"+ str(x[1]) +"'")
            ch=list(cur.fetchall())
            check=str(ch[0][0])
            val='accept'
            #print(check,x[1])
            if check.lower()=='yes':
                addformula="INSERT INTO borrow (Student_regno,Sub_bid, Approved_date) VALUES (%s, %s, %s)"
                add_accept=(x[0],x[1],d1)
                cur.execute(addformula, add_accept)
                cur.execute("UPDATE Subbook SET is_available='no' WHERE Sub_bid='"+ str(x[1]) +"'")
                try:
                    check_mail(x[0],val,x[1])
                    messagebox.showinfo("Approved","Book is Approved to Student whose Reg.no is '"+ str(x[0])+"'!!")
                    cur.execute("delete from book_request where Sub_bid='"+ str(x[1]) +"'")
                    con.commit()
                except:
                    messagebox.showwarning("Error","Error in sending mail..\nLogin to email to perform the action!!")
                pending_request()
            else:
                messagebox.showinfo("Failed","Approval Failed!!!\n Book is not available!!")


        def r_deny(r_a_val):
            x=r_a_val
            val='deny'
            cur.execute("delete from book_request where Sub_bid='"+ str(x[1]) +"'")
            try:
                check_mail(x[0],val,x[1])
                con.commit()
                messagebox.showinfo("Denied","Request for this book is denied!!!")
            except:
                messagebox.showwarning("Error","Error in sending mail..\nLogin to email to perform the action!!")
            pending_request()

            #def show():
        ls.delete(0,'end')
            #start
        h = Scrollbar(ls, orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(ls)
        v.pack(side = RIGHT, fill = Y)
        t = Text(ls, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
            #end
        cur.execute("select DISTINCT book_request.student_regno, book_request.sub_bid,book_request.date, subbook.Bid, book.BName, book.Author from book_request,book,subbook where book.Bid=Subbook.Bid AND book_request.Sub_bid=subbook.Sub_bid;")#  where book_request.student_regno")
        rows=list(cur.fetchall())
        reg=Label(ls,text='Reg.No.',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='w')
        t.window_create(END,window=reg)
        s_bookid=Label(ls,text='Bookid',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='w')
        t.window_create(END,window=s_bookid)
        s_sub=Label(ls,text='Sub BookID',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='c')
        t.window_create(END,window=s_sub)
        s_name=Label(ls,text='Book Name',bg='#97cee3',fg='white',width=20,font='BOLD', anchor='c')
        t.window_create(END,window=s_name)
        s_au=Label(ls,text='Author',bg='#97cee3',fg='white',width=20,font='BOLD', anchor='c')
        t.window_create(END,window=s_au)
        s_date=Label(ls,text='Date',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='c')
        t.window_create(END,window=s_date)
        s_accept_deny=Label(ls,text='Accept/Deny',bg='#97cee3',fg='white', font='BOLD',width=14 , anchor='c')
        t.window_create(END,window=s_accept_deny)

        t.insert(END,"\n")
        for row in rows:
            val=row
            reg=Label(ls,text=row[0],bg='yellow',fg='black',width=13, anchor='w')
            t.window_create(END,window=reg)
            s_name=Label(ls,text=row[3],bg='yellow',fg='black',width=12, anchor='c')
            t.window_create(END,window=s_name)
            s_book=Label(ls,text=row[1],bg='yellow',fg='black',width=15, anchor='c')
            t.window_create(END,window=s_book)
            s_au=Label(ls,text=row[4],bg='yellow',fg='black',width=30, anchor='w')
            t.window_create(END,window=s_au)
            s_sb=Label(ls,text=row[5],bg='yellow',fg='black',width=27, anchor='w')
            t.window_create(END,window=s_sb)
            s_date=Label(ls,text=row[2],bg='yellow',fg='black',width=12, anchor='w')
            t.window_create(END,window=s_date)
            s_accept=Button(ls,text='Accept',bg='grey',fg='black',command= (lambda x=val : r_accept(x)),width=8, anchor='c')
            t.window_create(END,window=s_accept)
            s_deny=Button(ls,text='Deny',bg='grey',fg='black',command= (lambda x=val : r_deny(x)),width=8, anchor='c')
            t.window_create(END,window=s_deny)
            t.insert(END,"\n")
                #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                #lboxs.insert(lboxs.size()+1, insertdata)
                #t.insert(END,insertdata)
            #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
            #end

    #pending books
    def pending_books():
        #x=val
        for widget in labelFrame.winfo_children():
            widget.destroy()

        #refresh=Button(labelFrame, bg="black",fg="white")
        #refresh.place(relx=0.01,rely=0.01,relwidth=0.03,relheight=0.05)


        ls = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        ls.place(relx=0.04, rely=0.04,relwidth=0.92,relheight=0.92)

            #def show():
        ls.delete(0,'end')
            #start
        h = Scrollbar(ls, orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(ls)
        v.pack(side = RIGHT, fill = Y)
        t = Text(ls, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
            #end
        cur.execute("select student.Sname,student.Regno,book.bname,SubBook.Sub_bid, Borrow.Approved_date,Borrow.borrow_id From student,Book,SubBook,Borrow where Book.Bid = SubBook.Bid and Student.Regno = Borrow.student_regno and SubBook.Sub_bid = Borrow.Sub_bid ")
        rows=list(cur.fetchall())
        reg=Label(ls,text='Reg.No.',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='w')
        t.window_create(END,window=reg)
        s_name=Label(ls,text='Name',bg='#97cee3',fg='white',width=17,font='BOLD', anchor='w')
        t.window_create(END,window=s_name)
        s_bookname=Label(ls,text='book name',bg='#97cee3',fg='white',width=25,font='BOLD', anchor='w')
        t.window_create(END,window=s_bookname)
        s_sub_id=Label(ls,text='sub bookid',bg='#97cee3',fg='white',width=13,font='BOLD', anchor='c')
        t.window_create(END,window=s_sub_id)
        s_borrow=Label(ls,text='borrow date',bg='#97cee3',fg='white',font='BOLD',width=13, anchor='c')
        t.window_create(END,window=s_borrow)
        s_borrowid=Label(ls,text='borrow id',bg='#97cee3',fg='white',width=13,font='BOLD', anchor='c')
        t.window_create(END,window=s_borrowid)
        s_receive=Label(ls,text='Receive book',bg='#97cee3',fg='white', font='BOLD',width=10 , anchor='c')
        t.window_create(END,window=s_receive)

        t.insert(END,"\n")
        for row in rows:
            val=row
            reg=Label(ls,text=row[1],bg='yellow',fg='black',width=13, anchor='w')
            t.window_create(END,window=reg)
            s_name=Label(ls,text=row[0],bg='yellow',fg='black',width=22, anchor='w')
            t.window_create(END,window=s_name)
            s_bookid=Label(ls,text=row[2],bg='yellow',fg='black',width=35, anchor='w')
            t.window_create(END,window=s_bookid)
            s_sub_id=Label(ls,text=row[3],bg='yellow',fg='black',width=15, anchor='c')
            t.window_create(END,window=s_sub_id)
            s_borrow=Label(ls,text=row[4],bg='yellow',fg='black',width=16, anchor='c')
            t.window_create(END,window=s_borrow)
            s_borrowid=Label(ls,text=row[5],bg='yellow',fg='black',width=15, anchor='c')
            t.window_create(END,window=s_borrowid)
            s_receive=Button(ls,text='Recieve Book',bg='grey',fg='black',command= (lambda x=val : b_receive(x)),width=13, anchor='c')
            t.window_create(END,window=s_receive)
            t.insert(END,"\n")
                #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                #lboxs.insert(lboxs.size()+1, insertdata)
                #t.insert(END,insertdata)
            #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
            #end

    #receive BOOK
    def b_receive(data):
        x=data
        val='return'
        d1 = today.strftime("%Y-%m-%d")
        addformula="INSERT INTO return_book (Student_regno,Sub_bid, Approved_date,Return_date,Borrow_id) VALUES (%s, %s, %s, %s, %s)"
        add_receive=(x[1],x[3],x[4],d1,x[5])
        try:
            cur.execute(addformula, add_receive)
            cur.execute("UPDATE Subbook SET is_available='yes' WHERE Sub_bid='"+ str(x[3]) +"'")
            try:
                check_mail(x[1],val,x[3])
                cur.execute("delete from borrow where Borrow_id='"+ str(x[5]) +"'")
                con.commit()
                messagebox.showinfo("Added Successfully","Book is received and history is updated of Student with Reg.no '"+str(x[1])+"'!!")
            except:
                messagebox.showwarning("Error","Error in sending mail..\nLogin to email to perform the action!!")
            pending_books()
        except(mysql.connector.errors.IntegrityError):
            messagebox.showwarning('Error','This borrow ID already exists. Please check the details manually.')


    lb3 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Pending Files',menu=lb3)
    lb3.add_command(label='Pending Requests',command=pending_request)
    lb3.add_command(label='Pending Books',command=pending_books)


    # Query/Feedback

    '''lb4 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Qwery/Feedback',menu=lb4)
    lb4.add_command(label='Feedback',command=None)
    lb4.add_command(label='Query',command=None)'''


    #sending mail to Others
    def mail_others():
        global admin_email_password
        global window1
        def send_mail():
            #global window1
            try:
                sub_m=str(sub_entry.get('1.0','end-1c'))
                msg_m=str(msg_entry.get('1.0','end-1c'))
                send_m=str(sender_entry.get('1.0','end-1c'))
                #print(sub_m+'\n'+msg_m)
                msg= MIMEMultipart()
                msg['From'] = "ADMIN IIIT KOTTAYAM"
                msg['To'] = send_m
                msg['Subject'] =sub_m
                body = msg_m
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                sm= smtplib.SMTP('smtp.gmail.com', 587)
                sm.starttls()
                sm.login(mail_admin, admin_email_password)
                sm.sendmail(mail_admin, send_m, text)
                sm.quit()
                messagebox.showinfo('Mail Status','Mail is sent Successfully..!')
                #window1.distroy()

            except Exception as e:
                print(e)
                messagebox.showinfo('Mail Status','Mail could not be sent.\nPlease login to the mail under "Access Mail" section to perform the action.\nOr check Your mail settings..! ')

        window1 = Toplevel(admin)
        window1.geometry('500x500+50+50')
        window1.resizable(False,False)
        canvas = Canvas(window1)
        canvas.config(bg="#c9f0ff")
        canvas.pack(expand=True,fill=BOTH)
        sender=Label(window1,text='To:',bg='#519790',fg='black',font=12).place(relx=0.04,rely=0.06,relwidth=0.2,relheight=0.05)
        sender_entry=Text(window1,bg='white',fg='#464646',font=12)
        sender_entry.place(relx=0.25,rely=0.06,relwidth=0.71,relheight=0.08)
        sub=Label(window1,text='Subject:',bg='#519790',fg='black',font=12).place(relx=0.04,rely=0.15,relwidth=0.2,relheight=0.05)
        sub_entry=Text(window1,bg='white',fg='#464646',font=12)
        sub_entry.place(relx=0.25,rely=0.15,relwidth=0.71,relheight=0.10)
        msg=Label(window1,text='Message:',bg='#519790',fg='black',font=12).place(relx=0.04,rely=0.26,relwidth=0.2,relheight=0.05)
        msg_entry=Text(window1,bg='white',fg='#323c36',font=12)
        msg_entry.place(relx=0.25,rely=0.26,relwidth=0.71,relheight=0.64)
        okBtn = Button(window1,text="Send",bg='green', fg='black', command=send_mail)
        okBtn.place(relx=0.78,rely=0.92, relwidth=0.18,relheight=0.05)
        quitBtn = Button(window1,text="Cancel",bg='orange', fg='black', command=window1.destroy)
        quitBtn.place(relx=0.25,rely=0.92, relwidth=0.18,relheight=0.05)



    #Mail sending
    lb5 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Send Email',menu=lb5)
    lb5.add_command(label='Student',command=lambda: mail_stu('mail_student'))
    lb5.add_command(label='Admin',command=lambda: mail_stu('mail_admin'))
    lb5.add_command(label='IIITK Family',command=lambda: mail_stu('mail_iiitk'))
    lb5.add_command(label='Others',command=lambda: mail_others())


    #quitBtn = Button(admin,text="Quit",bg='#f7f1e3', fg='black', command=admin.destroy)
    #quitBtn.place(relx=0.05,rely=0.92, relwidth=0.18,relheight=0.05)

    admin.config(menu=menubar)
    admin.mainloop()

#end admin

#login------------------------------------------------------------------------------------
def start_login(win=False):
    if win:
        win.destroy()
    global n,win1,username,password,isempty
    #if __name__!="__main__":
        #w.destroy()
    win1 = Tk()
    #win1=w
    win1.title('Library Management System   |   Welcome to IIIT Kottayam Library')
    h=(win1.winfo_screenheight()*4.4)//5
    win1.geometry('%sx%s+%s+%s'%(1150,int(h),50,6)) #here 50, 6 is the x, y co-ordinate of window respectively
    win1.config(bg='White')
    win1.resizable(False, False)

    n = 1
    username = password = ""
    isempty=True

    #search_user funtion will be used to serch username and password into database and then it will open the next window 
    def search_user():
        global n,username,password,win1
        found=False
        command1 = "select Aid, Password from Admin where Aid=%s AND Password=%s"
        var=[username,password]
        command2 = "select Regno, Password, is_restricted from Student where Regno=%s AND Password=%s"
        try:
            # Add your own database name and password here to reflect in the code
            # before running this program create a databse python_pro
            #Create tables admin and student in database python_pro  
            con1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="goloo",#Replace XXXX with your MySQL password
                database="Library")
            cur1 = con1.cursor()
            cur1.execute(command1,var)
            admin=cur1.fetchall()
            cur1.execute(command2,var)
            user=cur1.fetchall()
            
            if (len(admin)+len(user))<1:
                messagebox.showinfo('Error!','Invalid user name or password') 
                #back() will erase the data entered by user 
                back()
            else:          
                if len(admin)>0:
                    #messagebox.showinfo('sucess','Login Success as Admin')
                    cur1.close()
                    con1.close()
                    found=True
                    back()
                    start_admin(admin[0][0],admin[0][1],win1)
                    #start_admin(admin[0][0],admin[0][1])  -----> admin function call
                    #admin function call will be there
                    #win.destroy()
                if(found!=True):  
                    cur1.close()
                    con1.close()
                    back()
                    if str(user[0][2])=="yes":
                        messagebox.showinfo('Message','You are restricted.')
                    else:
                        start_student(user[0][0],user[0][1],win1)
                         
        except Exception as e:
            print(e)
            found=False
            back()
            messagebox.showinfo("Error!","Something went wrong")
            #back() will erase the data entered by user 
            





    def next_or_login():
        global n,username,password,isempty
        if(login_input.get() == '' or isempty):
            #print("Empty input")
            messagebox.showinfo("Error!", "Input field can't be empty")
            return
        
        #if n==1 then read username from login_input
        if n == 1:
            username = str(login_input.get())

            login_input.delete(0, END)
            backbt.place(relx=0.345555, rely=0.58+0.1, anchor=CENTER)
            unsername_display.configure(text=username)
            unsername_display.place(relx=0.5, rely=0.5, anchor=CENTER)
            n = n+1
            login.config(text="Login")

            #start
            isempty=True
            login_input.insert(0,"Password")     
            login_input.configure(state=DISABLED)                       
            login_input.place(relx=0.5, rely=0.5+0.08, anchor=CENTER)
            onclick_id=login_input.bind('<Button-1>', placeholder)
            #end
            return

        #if n>=2 then read password from login_input
        if n >= 2:
            password = str(login_input.get())
            # from here login process will start
            search_user()

    def back():
        global n
        login_input.delete(0, END)
        n = 1
        login_input.config(show='')
        unsername_display.place_forget()
        backbt.place_forget()
        login.config(text="Next")
        #start
        isempty=True
        login_input.configure(state=NORMAL)
        login_input.delete(0, END)
        login_input.insert(0,"Username")     
        login_input.configure(state=DISABLED)                       
        login_input.place(relx=0.5, rely=0.5+0.08, anchor=CENTER)
        onclick_id=login_input.bind('<Button-1>', placeholder)
        #end

    def placeholder(event):
        global isempty,n
        isempty=False
        login_input.configure(state=NORMAL)
        login_input.delete(0, END)
        try:
            login_input.unbind('<Button-1>', onclick_id)  
        except:
            print()    
        if n>1:
            login_input.config(show="*")

    #Next button
    buttonsFont = tkFont.Font(family='product sans', size=15)
    login = Button(win1, text="Next", bg="#4285F4", cursor='hand2',activebackground="#356AC3", activeforeground="white",
                        font=buttonsFont, anchor='c', width=13, relief="flat", fg="white",command=next_or_login)
    login.place(relx=0.655555, rely=0.58+0.1, anchor=CENTER)

    # Login Picture
    #img = PhotoImage(file="D:\\team_project\\project\\login_logo.png")
    img = PhotoImage(file="C:\\Users\\91969\\Desktop\\SEM 3\\IT WORKSHOP 3\\Project\\Project_code\\Student_section\\Student\\Changable_code\\login_logo.png")
    login_logo = Label(image=img, bg="white", height=250, width=250)
    login_logo.place(relx=0.5, rely=0.25, anchor=CENTER)

    # Login input
    entryFont = tkFont.Font(family='product sans', size=15)
    login_input = Entry(win1, width=38, highlightthickness=3, font=entryFont, selectborderwidth=3,
                                relief='flat', bg="pink", selectbackground="white")   
    #start                                                     
    login_input.insert(0,"Username")     
    login_input.configure(state=DISABLED)                       
    login_input.place(relx=0.5, rely=0.5+0.08, anchor=CENTER)
    onclick_id=login_input.bind('<Button-1>', placeholder)
    #end
    login_input.bind('<Return>', (lambda event: next_or_login()))
    login_input.bind('<Escape>', (lambda event: next_or_login()))

    # Login buttons
    #buttonsFont = tkFont.Font(family='product sans', size=15)
    #Label to display user name after clicking on next button
    unsername_display = Label(bg="white", borderwidth=1, font=buttonsFont)

    # Back Button
    backbt = Button(win1, text="Back", cursor='hand2',bg="#4285F4", activebackground="#356AC3", activeforeground="white",
                            font=buttonsFont, anchor='c', width=13, relief="flat", fg="white", command=back)


    win1.mainloop()
#end of login


#conneting MySQL


#Regno=""

'''
topF = tkinter.Frame(win, width=1150, borderwidth=-1, height=150, bg='black')
topF.grid(column=0, row=0, columnspan=2)

bottomF = tkinter.Frame(win, width=1150, relief=SUNKEN, height=450, bg="yellow")
bottomF.grid(column=0, row=2)

tabF = tkinter.Frame(win, width=1150, height=80, relief=SUNKEN, bg="red")
tabF.grid(column=0, row=1,columnspan=2)

'''


    
#start student
def start_student(reg,password,win1="default"):     
    global cur,con,Regno,win,topF,bottomF,tabF,listbox1
    win1.destroy()
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="goloo",#Replace XXXX with your MySQL password
        database="Library")
    cur = con.cursor()
    #initialize Regno of the student to argument passed from module login.py into start() function after login 
    Regno=reg
    
    #start
    #fetching data of user after login
    command='select Book.Bname,Book.Author,Borrow.Approved_date,ADDDATE(Borrow.Approved_date, 14),DATEDIFF(CURDATE(),ADDDATE(Borrow.Approved_date, 14))*1 from Borrow, SubBook, Book where Student_regno=%s and Borrow.sub_bid=SubBook.sub_bid and SubBook.bid=Book.bid and DATEDIFF(CURDATE(),ADDDATE(Borrow.Approved_date, 14)) > 0'
    var=[Regno]
    cur.execute(command,var)
    var=cur.fetchall()
    fine=0
    for i in range(len(var)):
        fine += float(var[i][4])

    command='update student set fine=%s where Regno=%s'
    var=[fine,Regno]
    cur.execute(command,var)
    con.commit()

    command="select Sname, Fine from student where Regno=%s and Password=%s"
    var=[reg, password]
    cur.execute(command,var)
    user_details=cur.fetchall()
    #end

    # Making the window -------------------------------------
    win = Tk()
    #win=Toplevel()
    #win=win1
    win.title(str("Hii, "+user_details[0][0])+"  |   Welcome to IIIT Kottayam Library   |   Student Section")
    h=(win.winfo_screenheight()*4.4)//5
    win.geometry('%sx%s+%s+%s'%(1150,int(h),50,6))
    win.config(bg='White')
    win.resizable(False, False)


    # Frames ----------------------------------------------------------------------------------------------------
    
    #start
    topF = Frame(win, borderwidth=-1, bg='white')
    topF.place(relx=0, rely=0, relwidth=1, relheight=0.2206)

    tabF = Frame(win, relief=SUNKEN, bg="red")
    tabF.place(relx=0, rely=0.2206, relwidth=1, relheight=0.1176)

    bottomF = Frame(win, relief=SUNKEN, bg='light yellow')
    bottomF.place(relx=0, rely=0.2206+0.1176, relwidth=1, relheight=1-0.2206-0.1176)
    #end
    
    #start of Fine
    #creting listbox1 to insert fine into this listbox
    listbox1 = Listbox(topF,relief="sunken",font=("courier",15),bg='black')
    listbox1.place(relx=0.8, rely=0,relwidth=1,relheight=1)

    #function to display message of PayFine button
    def payFine():
        try:
            webbrowser.open("https://www.onlinesbi.com/sbicollect/icollecthome.htm")
        except:
            messagebox.showinfo("Error!","Something went wrong")

    fineFont = tkFont.Font(size=12)
    user = Label(listbox1, text='User : ' + str(user_details[0][0]), fg="green", font=fineFont)   
    user.place(relx=0, rely=0)
    Fine = Label(listbox1, text='Fine  : ' + str(user_details[0][1]), fg="red", font=fineFont)   
    Fine.place(relx=0, rely=0.25+0.05)
    if fine>0:
        pay_fine=Button(listbox1,text='Pay Fine',bg='green',fg='white', activeforeground='black', command=payFine, bd='2',cursor='hand2', font=fineFont)
        pay_fine.place(relx=0.125, rely=0.23+0.05)
    
    #logoutbutton
    
    logout=Button(listbox1,text='Logout',bg='Red',fg='Black', activeforeground='black', command=lambda x=win: start_login(win), bd='2', font=fineFont)
    logout.place(relx=0.125-0.05, rely=0.23+0.51)
    #end of Fine

    def titleBar():
        global cur,Regno,win,topF,bottomF,tabF 
        
        img = ImageTk.PhotoImage(Image.open(r"C:\Users\91969\Desktop\SEM 3\IT WORKSHOP 3\Project\Project_code\Student_section\Student\iiit.jpg").resize((400, 120), Image.ANTIALIAS))
        logo = Label(topF, bg="red", borderwidth=0,image=img, height=120, width=400)
        logo.image = img
        logo.place(relx=0, rely=0)

    titleBar()   
    #calling tab() function from start() function to display tabs
    tabs()
    win.mainloop()
#end  of start() function
 

# Library --------------------------------------------------------------------------------------------------------------

def search_book():
    global cur,win,topF,bottomF,tabF,subject_name,keyword,notselected,category
    keyword=category=""
    notselected=True
    subject_name="select category"

    
    #diaplay category list combobox
    def show_category_list():
        global category,subject_name
        #function for handling categoty combobox event
        def category_dropdown(event):
            global category
            category=str(cdropdown.get()) 

        categories=[]
        if subject_name=="select subject":
            categories += ["select category"]
        else:
            cmd1='select Cname from category where Subject_name=%s'
            var1=[subject_name]
            cur.execute(cmd1,var1)
            result=cur.fetchall()
            categories=[]
            for r in result:
                categories.append(r[0])
            
        #creating category dropdown
        cdropdown = ttk.Combobox(bottomF,width=30,state="readonly")
        if len(categories)==0:
            categories += ["select category"]
            cdropdown['values']=categories
        else:
            cdropdown['values']=categories
            category=categories[0]
        
        cdropdown.current(0)
        cdropdown.bind("<<ComboboxSelected>>", category_dropdown)
        cdropdown.place(relx=0.22+0.25, rely=0.48)    


    #function for handling subject combobox event
    def dropdown_fun(event):
        #if strem.get()=="CSE":
        global subject_name,notselected,category,cur,listbox,bottomF
        notselected=False
        subject_name=str(subject.get()) 

        show_category_list()#to change the content of category combobox based on subject
        


    def display_search_result(flag="default"):
        global cur,win,con,topF,bottomF,tabF,subject_name,keyword,notselected,category
        if flag=='drop_down': 
            if subject_name=='select subject' or notselected:
                messagebox.showinfo("Error!","Kindly select a subject")
                return
            command='select Bname,Author,Bid from book where subject_name=%s and CName=%s'
            subject_name=[subject_name,category]
            cur.execute(command,subject_name)
        else: 
            if key.get()=="":
                messagebox.showinfo("Error!","Input field can't be empty")
                return
            #command='select Bname,Author from book where subject_name like "%{0}%" or Bname like "%{0}%"'.format(key.get())
            
            command='select Bname,Author,Bid from book where subject_name REGEXP "%{0}%" or Bname like "%{0}%"'.format(key.get())
            cur.execute(command)
        
        
        result=cur.fetchall()    

        listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
        listbox.place(relx=0, rely=0,relwidth=0.9848,relheight=0.959)

        if len(result)<1:
            messageFont = tkFont.Font(family='product sans', size=18)
            message = Label(listbox, text='Sorry, No such book found in database!', bg="yellow", fg='black', width=40, borderwidth=0, font=messageFont, anchor='c')
            message.place(relx=0.3,rely=0.4)
            return
        
        h = Scrollbar(bottomF, orient='horizontal')
        h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
        v = Scrollbar(bottomF, orient='vertical')
        v.pack(side=RIGHT, fill=Y)
        v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
        t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)

        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox,text='Book Name', bg="black", fg='white',width=55, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        authorFont = tkFont.Font(family='product sans', size=13)
        author = Label(listbox, text='Author', bg="black", fg='white', width=35, borderwidth=0, font=authorFont, anchor='w')
        t.window_create(END,window=author)

        requestFont = tkFont.Font(family='product sans', size=12)
        reuqest = Label(listbox, text='Request Book', bg="black", fg='white', width=17, borderwidth=0, font=requestFont, anchor='c')
        t.window_create(END,window=reuqest)

        favorite  = Label(listbox, text='Add to favorite', bg="black", fg='white', width=17, borderwidth=0, font=requestFont, anchor='c')
        t.window_create(END,window=favorite)
        t.insert(END,"\n")
        #t.insert(END,"\n")
        def add_favorite(bid):
            try:
                global Regno,cur,con
                command1='select * from favorite_book where Student_regno=%s'
                var=[Regno]
                cur.execute(command1,var)
                res=cur.fetchall()
                flag="insert"
                for r in res:
                    if r[0]==bid:
                        flag="not insert"
                        break 
                if flag=="insert":
                    command2='insert into favorite_book values(%s,%s)'
                    var=[bid,Regno]
                    cur.execute(command2,var)
                    con.commit()
                    messagebox.showinfo("Message","added to your favorite book list.")
                    
                    
            except Exception as e:
                print(e)    

        
        for r in result:
            bookNameFont = tkFont.Font(family='product sans', size=13)
            bookName = Label(listbox,text=r[0], bg="green", fg='white',width=55, borderwidth=0,font=bookNameFont, anchor='w')
            t.window_create(END,window=bookName)

            authorFont = tkFont.Font(family='product sans', size=13)
            author = Label(listbox, text=r[1], bg="yellow", fg='black', width=35, borderwidth=0, font=authorFont, anchor='w')
            t.window_create(END,window=author)

            requestFont = tkFont.Font(family='product sans', size=12)
            reuqest = Button(listbox, text="Request", command=lambda y=r[2]:send_book_request(y),font=requestFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
            t.window_create(END,window=reuqest)

            favFont = tkFont.Font(family='product sans', size=12)
            favorite = Button(listbox, text="Add to favorite", command=lambda x=r[2]:add_favorite(x),font=favFont, bg="#FFD666", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
            t.window_create(END,window=favorite)



            t.insert(END,"\n")
            #t.insert(END,"\n")

        #start   
        t.configure(state="disabled") 
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)  
        #end  


            
    # Entry labels ----------------------------------------------
    for widget in bottomF.winfo_children():
        widget.destroy()

    label3 = Label(bottomF,text="SEARCH BOOK",bg='#525b59', fg='white', font='BOLD')
    label3.place(relx=0.35,rely=0.11,relwidth=0.3,relheight=0.1)

    titleFont = tkFont.Font(family='product sans', size=13)
    strem1 = Label(bottomF, text='Select Subject : ', bg="light yellow", width=15,
                              borderwidth=0, font=titleFont, anchor='e').place(relx=0.04+0.25+0.05, rely=0.4)
    category1 = Label(bottomF, text='Select Category : ', bg="light yellow", width=15,
                              borderwidth=0, font=titleFont, anchor='e').place(relx=0.04+0.25+0.05, rely=0.48)
    keyword1 = Label(bottomF, text='Enter keyword : ', bg="light yellow", borderwidth=0,
                           width=15, font=titleFont, anchor='e').place(relx=0.04+0.25+0.05, rely=0.6)
    #creating Dropdown
    subject = ttk.Combobox(bottomF,width=30,state="readonly")
    command='select * from Subject'
    cur.execute(command)
    val=cur.fetchall()
    val1=[e[0] for e in val]
    val1 += ["select subject"]
    subject['values']=val1
    #subject.current(2)
    subject.current(len(val1)-1)
    subject.bind("<<ComboboxSelected>>", dropdown_fun)
    subject.place(relx=0.22+0.25, rely=0.4)
    
    key = Entry(bottomF, width=33, selectbackground="white") 
    key.place(relx=0.22+0.25, rely=0.6,relheight=0.06)
    #search_btn1 for search by subject
    search_btn1 = Button(bottomF,text="SEARCH",bg='Orange', command=(lambda x="drop_down":display_search_result(x)),width=15,fg='white',font='BOLD', cursor='hand2')
    search_btn1.place(relx=0.22+0.45, rely=0.42)
    #search_btn1 for search by keyword
    search_btn2 = Button(bottomF,text="SEARCH",bg='Orange', command=display_search_result,width=15,fg='white',font='BOLD', cursor='hand2')
    search_btn2.place(relx=0.22+0.45, rely=0.58)
    show_category_list() #to display category list combobox when 1st time search_book() will be called  
    

#common_request() wil be used for inset sub book id into boo_request table   
def send_book_request(bookid):
    global cur,win,topF,bottomF,tabF,Regno,con
    try:
        #command='select subbook.sub_bid from book, subbook where book.bid=subbook.bid and book.bid=%s and subbook.is_available="yes" and subbook.sub_bid not in(select sub_bid from book_request) and (subbook.sub_bid,%s) not in(select subbook.sub_bid, book_request.student_regno from subbook,book_request where )'
        command='select subbook.sub_bid from subbook where subbook.bid=%s and subbook.is_available="yes" and subbook.sub_bid not in(select sub_bid from book_request) and %s not in(select book_request.student_regno from subbook,book_request where subbook.sub_bid=book_request.sub_bid and subbook.bid=%s)'
        var=[bookid,Regno,bookid]
        cur.execute(command,var)
        result=cur.fetchall()
       
        if len(result)==0:
            messagebox.showinfo("Message","Try after some time.")
            return
        command='insert into book_request values(%s,%s,CURDATE())'
        var=[result[0][0],Regno]
        cur.execute(command,var)
        con.commit()   
        messagebox.showinfo("Sucess","Request added") 
    except Exception as e:
        print(e)

#display book that you have currently requested(i.e, Book from Book_request table) 
def display_book_reuqests():
    global con,cur,win,topF,bottomF,tabF,Regno
    for widget in bottomF.winfo_children():
        widget.destroy()

    #function to cancle book request     
    def cancel_request(subid):
        try:
            command='delete from book_request where sub_bid=%s and student_regno=%s'
            var=[subid,Regno]
            cur.execute(command,var)
            con.commit()
            messagebox.showinfo("Sucess","Book request cancelled sucessfully")
            display_book_reuqests()
        except Exception as e:
            print(e)    
            

    #start
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0, rely=0,relwidth=0.9848,relheight=0.959)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set) 
    #end
    command="select Book.Bname,Book_request.Date,Book_request.sub_bid from book_request,subbook,book where book_request.sub_bid=subbook.sub_bid and subbook.bid=book.bid and Book_request.student_regno=%s"
    var=[Regno]
    cur.execute(command,var)
    result1=cur.fetchall()

    if len(result1)==0:
        messageFont = tkFont.Font(family='product sans', size=18)
        message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0, font=messageFont, anchor='c')
        message.place(relx=0.4,rely=0.4)
        return
    
    bookNameFont = tkFont.Font(family='product sans', size=13)
    bookName = Label(listbox,text='Book Name', bg="black",fg='white',width=55, borderwidth=0,font=bookNameFont, anchor='w')
    t.window_create(END,window=bookName)

    dateFont = tkFont.Font(family='product sans', size=13)
    date = Label(listbox, text='Request Date', bg="black",fg='white', width=40, borderwidth=0, font=dateFont, anchor='c')
    t.window_create(END,window=date)

    statusFont = tkFont.Font(family='product sans', size=13)
    status = Label(listbox, text='Sub BookID', bg="black",fg='white', width=13, borderwidth=0, font=statusFont, anchor='c') 
    t.window_create(END,window=status)

    cancelFont = tkFont.Font(family='product sans', size=13)
    cancelbtn = Label(listbox, text='Cancel Request', bg="black",fg='white',width=16, borderwidth=0, font=cancelFont, anchor='c') 
    t.window_create(END,window=cancelbtn)


    
    t.insert(END,"\n")

    for r in result1:
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox,text=r[0], bg="green",fg='white',width=55, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        dateFont = tkFont.Font(family='product sans', size=13)
        date = Label(listbox, text=r[1], bg="orange", fg='blue', width=40, borderwidth=0, font=dateFont, anchor='c')
        t.window_create(END,window=date)

        statusFont = tkFont.Font(family='product sans', size=13)
        status = Label(listbox, text=r[2], bg="green",fg='white',width=13, borderwidth=0, font=statusFont, anchor='c') 
        t.window_create(END,window=status)

        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = Button(listbox, text="Cancel Request", command=(lambda x=r[2]:cancel_request(x)),font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16,cursor='hand2') 
        t.window_create(END,window=cancel)
        t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  

def mybooks(arg='Favorite Book'):
    global regno,cur,win,topF,bottomF,tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    #start
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0, rely=0,relwidth=0.9848,relheight=0.959)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set) 
    #end    

    #start 22/10  
    def decide_mybook(event):
        if(str(mybook_combo.get())=='Favorite Book'):
            mybooks('Favorite Book')
        elif(str(mybook_combo.get())=='Borrowed Book'):   
            mybooks('Borrowed Book')
        else:
            messagebox.showinfo("Error!","Something went wrong")  
            return 

    #creating Combobox
    mybook_combo = ttk.Combobox(listbox,width=15,state="readonly",font="arial 12 bold")
    val=['Favorite Book','Borrowed Book']
    mybook_combo['values']=val
    if(arg=='Favorite Book'):
        mybook_combo.current(0)
    elif(arg=='Borrowed Book'):   
        mybook_combo.current(1)
    else:
        messagebox.showinfo("Error!","Something went wrong")  
    
    mybook_combo.bind("<<ComboboxSelected>>", decide_mybook)
    mybook_combo.place(relx=0.22+0.25, rely=0.03)  
    #end 22/10  

    def borrowed_book():
        try:
            command='select book.bname,book.author,borrow.approved_date,borrow.borrow_id,ADDDATE(borrow.approved_date,14),book.bid,subbook.sub_bid from borrow,subbook,book where borrow.sub_bid=subbook.sub_bid and subbook.bid=book.bid and borrow.student_regno=%s'
            var=[Regno]
            cur.execute(command,var)
            result=cur.fetchall()
        except Exception as e:
            messagebox.showinfo("Error!","Something went worng")
            print(e)    

        if len(result)==0:
            messageFont = tkFont.Font(family='product sans', size=18)
            message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0, font=messageFont, anchor='c')
            message.place(relx=0.4,rely=0.4)
            return

        t.insert(END,"\n")
        t.insert(END,"\n")
        t.insert(END,"\n")
        bookNameFont = tkFont.Font(family='product sans', size=12)
        bookName = Label(listbox,text='Book Name', bg="black", fg='white',width=55, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        authorFont = tkFont.Font(family='product sans', size=12)
        author = Label(listbox, text='Author', bg="black", fg='white', width=35, borderwidth=0, font=authorFont, anchor='w')
        t.window_create(END,window=author)

        approveddateFont = tkFont.Font(family='product sans', size=12)
        approveddate = Label(listbox, text='Approved Date', bg="black", fg='white', width=15, borderwidth=0, font=approveddateFont, anchor='c')
        t.window_create(END,window=approveddate)

        borrowIDFont = tkFont.Font(family='product sans', size=12)
        borrowID = Label(listbox, text='Borrow ID', bg="black", fg='white', width=10, borderwidth=0, font=borrowIDFont, anchor='c')
        t.window_create(END,window=borrowID)

        exp_returnFont = tkFont.Font(family='product sans', size=12)
        exp_return = Label(listbox, text='Expected return date', bg="black", fg='white', width=18, borderwidth=0, font=exp_returnFont, anchor='c')
        t.window_create(END,window=exp_return)

        bidFont = tkFont.Font(family='product sans', size=12)
        bid = Label(listbox, text='Book ID', bg="black", fg='white', width=10, borderwidth=0, font=bidFont, anchor='c')
        t.window_create(END,window=bid)

        sub_bidFont = tkFont.Font(family='product sans', size=12)
        sub_bid = Label(listbox, text='Sub BookID', bg="black", fg='white', width=12, borderwidth=0, font=sub_bidFont, anchor='c')
        t.window_create(END,window=sub_bid)

        t.insert(END,"\n")

        for r in result:
            bookNameFont = tkFont.Font(family='product sans', size=12)
            bookName = Label(listbox,text=r[0], bg="green",fg='white',width=55, borderwidth=0,font=bookNameFont, anchor='w')
            t.window_create(END,window=bookName)

            authorFont = tkFont.Font(family='product sans', size=12)
            author = Label(listbox, text=r[1], bg="yellow",width=35, borderwidth=0, font=authorFont, anchor='w')
            t.window_create(END,window=author)

            approveddateFont = tkFont.Font(family='product sans', size=12)
            approveddate = Label(listbox, text=r[2], bg="gray",width=15, borderwidth=0, font=approveddateFont, anchor='c')
            t.window_create(END,window=approveddate)

            borrowIDFont = tkFont.Font(family='product sans', size=12)
            borrowID = Label(listbox, text=r[3], bg="green",fg='white',width=10, borderwidth=0, font=borrowIDFont, anchor='c')
            t.window_create(END,window=borrowID)

            exp_returnFont = tkFont.Font(family='product sans', size=12)
            exp_return = Label(listbox, text=r[4], bg="yellow",width=18, borderwidth=0, font=exp_returnFont, anchor='c')
            t.window_create(END,window=exp_return)

            bidFont = tkFont.Font(family='product sans', size=12)
            bid = Label(listbox, text=r[5], bg="gray",width=10, borderwidth=0, font=bidFont, anchor='c')
            t.window_create(END,window=bid)

            sub_bidFont = tkFont.Font(family='product sans', size=12)
            sub_bid = Label(listbox, text=r[6], bg="green",fg='white',width=12, borderwidth=0, font=sub_bidFont, anchor='c')
            t.window_create(END,window=sub_bid)

            t.insert(END,"\n")

        t.configure(state="disabled") 
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)  
    #end borrowed_book()            

    #start favorite_book()
    def favorite_book():
        
        try:
            command='select Book.Bname, Book.Author, Book.bid from Book, favorite_book where book.bid=favorite_book.Bid and favorite_book.student_regno=%s'
            var=[Regno]
            cur.execute(command,var)
            result=cur.fetchall()
        except Exception as e:
            messagebox.showinfo("Error!","Something went worng")
            print(e)    

        if len(result)==0:
            messageFont = tkFont.Font(family='product sans', size=18)
            message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0, font=messageFont, anchor='c')
            message.place(relx=0.4,rely=0.4)
            return

        t.insert(END,"\n")
        t.insert(END,"\n")
        t.insert(END,"\n")
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox,text='Book Name', bg="black", fg='white',width=55, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        authorFont = tkFont.Font(family='product sans', size=13)
        author = Label(listbox, text='Author', bg="black", fg='white', width=35, borderwidth=0, font=authorFont, anchor='w')
        t.window_create(END,window=author)

        requestFont = tkFont.Font(family='product sans', size=12)
        reuqest = Label(listbox, text='Request Book', bg="black", fg='white', width=15, borderwidth=0, font=requestFont, anchor='c')
        t.window_create(END,window=reuqest)

        removeFont = tkFont.Font(family='product sans', size=12)
        remove = Label(listbox, text='Remove from favorite', bg="black", fg='white', width=19, borderwidth=0, font=removeFont, anchor='c')
        t.window_create(END,window=remove)

        #favorite  = Label(listbox, text='Request Button', bg="black", fg='white', width=17, borderwidth=0, font=requestFont, anchor='c')
        #t.window_create(END,window=favorite)
        t.insert(END,"\n")
        for r in result:
                bookNameFont = tkFont.Font(family='product sans', size=13)
                bookName = Label(listbox,text=r[0], bg="green", fg='white',width=55, borderwidth=0,font=bookNameFont, anchor='w')
                t.window_create(END,window=bookName)

                authorFont = tkFont.Font(family='product sans', size=13)
                author = Label(listbox, text=r[1], bg="yellow", fg='black', width=35, borderwidth=0, font=authorFont, anchor='w')
                t.window_create(END,window=author)

                requestFont = tkFont.Font(family='product sans', size=12)
                reuqest = Button(listbox, text="Request", command=(lambda x=r[2]:send_book_request(x)),font=requestFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=14, cursor='hand2') 
                t.window_create(END,window=reuqest)

                removeFont = tkFont.Font(family='product sans', size=12)
                remove = Button(listbox, text="Remove", command=(lambda x=r[2],y=r[0]:remove_favorite(x,y)),font=removeFont, bg="#FFD666", activebackground="#FFD666", anchor='c', width=19, cursor='hand2') 
                t.window_create(END,window=remove)

                #favFont = tkFont.Font(family='product sans', size=12)
                #favorite = Button(listbox, text="Add to favorite", command=lambda x=r[2]:remove_favorite(x),font=favFont, bg="#FFD666", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
                #t.window_create(END,window=favorite)

                t.insert(END,"\n")
                #t.insert(END,"\n")

        t.configure(state="disabled") 
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)  
    #end favorite_book()  
    #calling function based on the value of combobox
    if(arg=='Favorite Book'):
        favorite_book()
    elif(arg=='Borrowed Book'):
        borrowed_book()
    else:
        messagebox.showinfo("Error!","Something went wrong")  
        return 

    #start remove_favorite()
    def remove_favorite(book_id,bname):
        try:
            command='delete from favorite_book where bid=%s'
            var=[book_id]
            cur.execute(command,var)
            con.commit()
            messagebox.showinfo("Message",str(bname)+" has been removed from your favorite book list.")
            mybooks()
        except Exception as e:
            messagebox.showinfo("Error!","Something went worng")
            print(e)        
   

        
    

def history():
    global Regno,cur,win,topF,bottomF,tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    #start
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0, rely=0,relwidth=0.9848,relheight=0.959)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set) 
    #end
    command='select distinct Book.Bname,Book.Author,Return_book.Approved_date,Return_book.Return_date,Book.Bid,SubBook.Sub_bid,Return_book.Borrow_ID from Book,SubBook,Return_book WHERE Book.Bid=SubBook.Bid and SubBook.Sub_bid=Return_book.Sub_bid and Return_book.Student_regno=%s'
    var=[Regno]
    cur.execute(command,var)
    rows=cur.fetchall()
    if len(rows)==0:
        messageFont = tkFont.Font(family='product sans', size=18)
        message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0, font=messageFont, anchor='c')
        message.place(relx=0.4,rely=0.4)
        return

    bookNameFont = tkFont.Font(family='product sans', size=15)
    bookName = Label(listbox,text='Book Name', bg="black", fg='white',width=50, borderwidth=0,font=bookNameFont, anchor='w')
    t.window_create(END,window=bookName)

    authorFont = tkFont.Font(family='product sans', size=15)
    author = Label(listbox, text='Author', bg="black", fg='white', width=40, borderwidth=0, font=authorFont, anchor='w')
    t.window_create(END,window=author)

    requestFont = tkFont.Font(family='product sans', size=15)
    reuqest = Label(listbox, text='Request Book', bg="black", fg='white', width=12, borderwidth=0, font=requestFont, anchor='c')
    t.window_create(END,window=reuqest)

    approveddateFont = tkFont.Font(family='product sans', size=15)
    approveddate = Label(listbox, text='Approved Date', bg="black", fg='white', width=13, borderwidth=0, font=approveddateFont, anchor='c') 
    t.window_create(END,window=approveddate)

    returndateFont = tkFont.Font(family='product sans', size=15)
    returndate = Label(listbox, text='Return date', bg="black", fg='white', width=13, borderwidth=0, font=returndateFont, anchor='c') 
    t.window_create(END,window=returndate)

    bidFont = tkFont.Font(family='product sans', size=15)
    bid = Label(listbox, text='Book ID', bg="black", fg='white', width=13, borderwidth=0, font=bidFont, anchor='c') 
    t.window_create(END,window=bid)

    subbidFont = tkFont.Font(family='product sans', size=15)
    subbid = Label(listbox, text='Sub Book ID', bg="black", fg='white', width=13, borderwidth=0, font=subbidFont, anchor='c') 
    t.window_create(END,window=subbid)

    borrowidFont = tkFont.Font(family='product sans', size=15)
    borrowid = Label(listbox, text='Borrow ID', bg="black", fg='white', width=13, borderwidth=0, font=borrowidFont, anchor='c') 
    t.window_create(END,window=borrowid)
    t.insert(END,"\n")
    #t.insert(END,"\n")

    for a in rows:
        bookNameFont = tkFont.Font(family='product sans', size=15)
        bookName = Label(listbox,text=str(a[0]), bg="gray",width=50, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        authorFont = tkFont.Font(family='product sans', size=15)
        author = Label(listbox, text=str(a[1]), bg="green", fg='white', width=40, borderwidth=0, font=authorFont, anchor='w')
        t.window_create(END,window=author)

        requestFont = tkFont.Font(family='product sans', size=9)
        reuqest = Button(listbox, text="Request", command=(lambda x=a[4]:send_book_request(x)),font=requestFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=18, cursor='hand2') 
        t.window_create(END,window=reuqest)

        approveddateFont = tkFont.Font(family='product sans', size=15)
        approveddate = Label(listbox, text=str(a[2]), bg="gray", width=13, borderwidth=0, font=approveddateFont, anchor='c') 
        t.window_create(END,window=approveddate)

        returndateFont = tkFont.Font(family='product sans', size=15)
        returndate = Label(listbox, text=str(a[3]), bg="yellow", width=13, borderwidth=0, font=returndateFont, anchor='c') 
        t.window_create(END,window=returndate)

        bidFont = tkFont.Font(family='product sans', size=15)
        bid = Label(listbox, text=str(a[4]), bg="green", fg='white',width=13, borderwidth=0, font=bidFont, anchor='c') 
        t.window_create(END,window=bid)

        subbidFont = tkFont.Font(family='product sans', size=15)
        subbid = Label(listbox, text=str(a[5]), bg="yellow", width=13, borderwidth=0, font=subbidFont, anchor='c') 
        t.window_create(END,window=subbid)

        borrowidFont = tkFont.Font(family='product sans', size=15)
        borrowid = Label(listbox, text=str(a[6]), bg="gray", width=13, borderwidth=0, font=borrowidFont, anchor='c') 
        t.window_create(END,window=borrowid)

        '''
        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
        t.window_create(END,window=cancel)
        '''
        t.insert(END,"\n")
        #t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  

def fine():
    global Regno,cur,win,topF,bottomF,tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    #start
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0, rely=0,relwidth=0.9848,relheight=0.959)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set) 
    #end
    command='select Book.Bname,Book.Author,Borrow.Approved_date,ADDDATE(Borrow.Approved_date, 14),DATEDIFF(CURDATE(),ADDDATE(Borrow.Approved_date, 14))*1,Borrow.Borrow_id,Book.bid,SubBook.sub_bid from Borrow, SubBook, Book where Student_regno=%s and Borrow.sub_bid=SubBook.sub_bid and SubBook.bid=Book.bid and DATEDIFF(CURDATE(),ADDDATE(Borrow.Approved_date, 14)) > 0'
    #bookname-0,author-1,approved_date-2,expexted_return_date-3,fine-4
    var=[Regno]
    cur.execute(command,var)
    rows=cur.fetchall()
    if len(rows)==0:
        messageFont = tkFont.Font(family='product sans', size=18)
        message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0, font=messageFont, anchor='c')
        message.place(relx=0.4,rely=0.4)
        return

    Font0 = tkFont.Font(family='product sans', size=13)
    Bname = Label(listbox,text='Book Name', bg="black", fg='white', width=38, borderwidth=0,font=Font0, anchor='w')
    t.window_create(END,window=Bname)

    Font1 = tkFont.Font(family='product sans', size=13)
    author = Label(listbox, text='Author', bg="black", fg='white', width=38, borderwidth=0, font=Font1, anchor='w')
    t.window_create(END,window=author)

    Font2 = tkFont.Font(family='product sans', size=13)
    approveddate = Label(listbox, text='Approved Date', bg="black", fg='white', width=13, borderwidth=0, font=Font2, anchor='c') 
    t.window_create(END,window=approveddate)

    Font3 = tkFont.Font(family='product sans', size=13)
    returndate = Label(listbox, text='Expected Return date', bg="black", fg='white', width=23, borderwidth=0, font=Font3, anchor='c') 
    t.window_create(END,window=returndate)

    Font4 = tkFont.Font(family='product sans', size=13)
    fine = Label(listbox, text='Fine', bg="black", fg='white', width=13, borderwidth=0, font=Font4, anchor='c') 
    t.window_create(END,window=fine)

    Font5 = tkFont.Font(family='product sans', size=13)
    borrowID = Label(listbox, text='Borrow ID', bg="black", fg='white', width=13, borderwidth=0, font=Font5, anchor='c') 
    t.window_create(END,window=borrowID)

    Font6 = tkFont.Font(family='product sans', size=13)
    bookID = Label(listbox, text='Book ID', bg="black", fg='white', width=13, borderwidth=0, font=Font6, anchor='c') 
    t.window_create(END,window=bookID)

    Font7 = tkFont.Font(family='product sans', size=13)
    sub_bookID = Label(listbox, text='Sub Book ID', bg="black", fg='white', width=15, borderwidth=0, font=Font7, anchor='c') 
    t.window_create(END,window=sub_bookID)
    '''
    Font4 = tkFont.Font(family='product sans', size=13)
    bid = Label(listbox, text='Return Button', bg="black", fg='white', width=17, borderwidth=0, font=Font4, anchor='c') 
    t.window_create(END,window=bid)
    '''
    t.insert(END,"\n")
    #t.insert(END,"\n")

    for a in rows:
        #bookname-0,author-1,approved_date-2,expexted_return_date-3,fine-4
        Font0 = tkFont.Font(family='product sans', size=13)
        Bname = Label(listbox,text=a[0], bg="gray",width=38, borderwidth=0,font=Font0, anchor='w')
        t.window_create(END,window=Bname)

        Font1 = tkFont.Font(family='product sans', size=13)
        author = Label(listbox, text=a[1], bg="green", fg='white', width=38, borderwidth=0, font=Font1, anchor='w')
        t.window_create(END,window=author)

        Font2 = tkFont.Font(family='product sans', size=13)
        approveddate = Label(listbox, text=a[2], bg="yellow", width=13, borderwidth=0, font=Font2, anchor='c') 
        t.window_create(END,window=approveddate)

        Font3 = tkFont.Font(family='product sans', size=13)
        returndate = Label(listbox, text=a[3], bg="gray", width=23, borderwidth=0, font=Font3, anchor='c') 
        t.window_create(END,window=returndate)

        Font4 = tkFont.Font(family='product sans', size=13)
        fine = Label(listbox, text=a[4], bg="red", width=13, borderwidth=0, font=Font4, anchor='c') 
        t.window_create(END,window=fine)

        Font5 = tkFont.Font(family='product sans', size=13)
        borrowID = Label(listbox, text=a[5], bg="gray", width=13, borderwidth=0, font=Font5, anchor='c') 
        t.window_create(END,window=borrowID)

        Font6 = tkFont.Font(family='product sans', size=13)
        bookID = Label(listbox, text=a[6], bg="green", fg='white', width=13, borderwidth=0, font=Font6, anchor='c') 
        t.window_create(END,window=bookID)

        Font7 = tkFont.Font(family='product sans', size=13)
        sub_bookID = Label(listbox, text=a[7], bg="yellow", width=15, borderwidth=0, font=Font7, anchor='c') 
        t.window_create(END,window=sub_bookID)
        
        '''
        Font5 = tkFont.Font(family='product sans', size=12)
        return_btn = Button(listbox, text="Return",command="", font=Font5, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16,cursor='hand2') 
        t.window_create(END,window=return_btn)
        '''
        t.insert(END,"\n")
        #t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  



def tabs():
    global cur,win,topF,bottomF,tabF
    # Functional buttons ----------------------------------------------
    btFont = tkFont.Font(family='product sans', size=15, weight=tkFont.BOLD)
    search_bt = Button(tabF,highlightthickness=0, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='Search Book', width=10, foreground='white', background='#4285F4', font=btFont, command=search_book).place(relx=0.01923076+0.035, rely=0.2)

    fines_bt = Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", cursor='hand2',
                              text='Fines', width=10, foreground='white', background='#4285F4', font=btFont,command=fine).place(relx=0.21153846+0.032, rely=0.2)

    history_bt = Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='History', width=10, foreground='white', background='#4285F4', font=btFont,command=history).place(relx=0.40384615+0.032, rely=0.2)

    request_bt = Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='Requests', width=10, foreground='white', background='#4285F4', font=btFont, command=display_book_reuqests).place(relx=0.59615384+0.032, rely=0.2)

    mybooks_bt = Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='My Books', width=10, foreground='white', background='#4285F4', font=btFont,command=mybooks).place(relx=0.78846153+0.032, rely=0.2)

    search_book()
    #win.mainloop()     

#end student                      

if __name__ == "__main__":
    start_login()
    #start_student('2019BCS0034','shiva') 
    #comment out this this line if you don't want to run this program as a main program
    #if you directely use this code before login, it will show  a message box with "Error!, Kindly login before accessing It!" and 
    #after clicking on the ok button the whole window will be destroyed.
    #start
    '''
    write this code into the end of library function(the last called function)
    if __name__ == "__main__":
        messagebox.showinfo("Error!", "Kindly login before accessing It!")
        win.destroy()
    ''' 
    #end


