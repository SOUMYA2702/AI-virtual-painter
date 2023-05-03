import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox

def database():
    global conn, cursor
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    q1 = "Create table if not exists user (id integer primary key AUTOINCREMENT,email varchar(150) unique,password TEXT, name TEXT,phone_no TEXT)"
    cursor.execute(q1)

def login():
    root = Tk()
    em=StringVar(root)
    passwrd=StringVar(root)
    root.title("AI virtual painter")
    root.geometry("780x450")
    root.config(bg="#343434")
    def log_in():
        database()
        try:
            e = em.get()
            p = passwrd.get()
            cursor.execute(f'SELECT * FROM user WHERE email = ? AND password = ?', (e, p))
            data=cursor.fetchone()

            if data:
                name = data[3]
                f = open("cache.txt","w")
                f.write(name)
                f.close()
                try:
                    import os
                    os.mkdir(name)
                except:
                    pass
                tkMessageBox.showinfo("AI virtual painter","Logged In Successfully !!!")
                root.destroy()
                import Ai_virtual_painter
            else:
                tkMessageBox.showinfo("AI virtual painter","Failed To Login !!!")
                em.set("")
                passwrd.set("")
                
        except Exception as e:
            tkMessageBox.showinfo("AI virtual painter",e)
            
    h1 = Label(root, text="-- LOGIN --",fg="#DCB86F",bg="#343434",font=("",24,"bold"))
    h1.place(x=300,y=15)
    h2 = Label(root, text="Email: ",fg="#DCB86F",bg="#343434",font=("",20,"bold"))
    h2.place(x=114,y=120)
    h3 = Label(root, text="Password: ",fg="#DCB86F",bg="#343434",font=("",20,"bold"))
    h3.place(x=60,y=205)
    e1 = Entry(root,textvariable=em,bg="#DCB86F",fg="#343434",font=("",20),width=30)
    e1.place(x=250,y=120)
    e2 = Entry(root,textvariable=passwrd,bg="#DCB86F",fg="#343434",font=("",20),width=30,show='*')
    e2.place(x=250,y=205)
    b1 = Button(root, text="Register",bg="#DCB86F",fg="#343434",font=("",20,"bold"),bd=2,relief="solid",width=18,command=signup)
    b1.place(x=60,y=290)
    b2 = Button(root, text="LOGIN",bg="#DCB86F",fg="#343434",font=("",20,"bold"),bd=2,relief="solid",width=18,command=log_in)
    b2.place(x=390,y=290)
    root.mainloop()

def signup():
    global nme,passwrd,em,phone
    root2 = Tk()
    nme=StringVar(root2)
    passwrd=StringVar(root2)
    em = StringVar(root2)
    phone = StringVar(root2)
    branch = StringVar(root2)

    root2.title("AI virtual painter")
    root2.geometry("780x480")
    root2.config(bg="#343434")
    def reg():
   
        global nme,passwrd,em,phone
        database()
        try:
            cursor.execute(f"INSERT INTO user(name,password,email,phone_no) VALUES('{nme.get()}','{passwrd.get()}','{em.get()}','{phone.get()}')")
            conn.commit()
            conn.close()
            tkMessageBox.showinfo("AI virtual painter","Registered Successfully !!!")
            root2.destroy()
            login()
        except Exception as e:
            tkMessageBox.showinfo("AI virtual painter",e)
            
    def login2():
            root2.destroy()
            login()
            
    h1 = Label(root2, text="-- REGISTER --",fg="#DCB86F",bg="#343434",font=("",24,"bold"))
    h1.place(x=280,y=15)
    h2 = Label(root2, text="Name: ",fg="#DCB86F",bg="#343434",font=("",20,"bold"))
    h2.place(x=60,y=120)
    h3 = Label(root2, text="Password: ",fg="#DCB86F",bg="#343434",font=("",20,"bold"))
    h3.place(x=60,y=180)
    e1 = Entry(root2,textvariable=nme,bg="#DCB86F",fg="#343434",font=("",20),width=30)
    e1.place(x=250,y=120)
    e2 = Entry(root2,textvariable=passwrd,bg="#DCB86F",fg="#343434",font=("",20),width=30)
    e2.place(x=250,y=180)
    h4 = Label(root2, text="Email: ",fg="#DCB86F",bg="#343434",font=("",20,"bold"))
    h4.place(x=60,y=240)
    h5 = Label(root2, text="Phone No.: ",fg="#DCB86F",bg="#343434",font=("",20,"bold"))
    h5.place(x=60,y=300)
    e4 = Entry(root2,textvariable=em,bg="#DCB86F",fg="#343434",font=("",20),width=30)
    e4.place(x=250,y=240)
    e5 = Entry(root2,textvariable=phone,bg="#DCB86F",fg="#343434",font=("",20),width=30)
    e5.place(x=250,y=300)


    b1 = Button(root2, text="Register",font=("",20,"bold"),bg="#DCB86F",fg="#343434",bd=2,relief="solid",width=18,command=reg)
    b1.place(x=60,y=400)
    b2 = Button(root2, text="Back To Login",bg="#DCB86F",fg="#343434",font=("",20,"bold"),bd=2,relief="solid",width=18,command=login2)
    b2.place(x=390,y=400)
    root2.mainloop()
    
signup()
