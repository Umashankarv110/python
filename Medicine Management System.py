# Tkinter based Project

import tkinter as tk

def MEDICINE_INFORMATION_SYSYEM():
    f1.pack()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    f6.pack_forget()

def CREATE_NEW_ACCOUNT():
    f1.pack_forget()
    f2.pack()

def ADMIN_LOGIN():
    f1.pack_forget()
    f3.pack()

def New_User():
    f1.pack_forget()
    f5.pack()    

def New_User_info():
    f5.pack_forget()
    f6.pack()

def submit():
    f3.pack_forget()
    f4.pack()


# ~~~~~~~MEDICINE INFORMATION SYSYEM MAIN PAGE~~~~~~~~~~


root = tk.Tk()
root.geometry("650x380")
root.title("Medicine Information System")
f1 = tk.Frame(root)
l1 = tk.Label(f1, text=" SHETH LUJ AND SIR MV COLLEGE ",width="300",height="1", bg="Light Grey", font=("Calibri", 23)).pack()
lbl = tk.Label(f1, text="-----:: MEDICINE INFORMATION SYSYEM ::-----",width="50",height="1", bg="Light Grey", font=("Calibri", 18)).pack()
spc = tk.Label(f1,height="2").pack()
b1 = tk.Button(f1, text="CREATE_NEW_ACCOUNT",width="50",height="1",font=("Calibri", 12), command=CREATE_NEW_ACCOUNT).pack()
b3 = tk.Button(f1, text="ADMIN_LOGIN",width="50",height="1",  font=("Calibri", 12),command=ADMIN_LOGIN).pack()
b2 = tk.Button(f1, text="USER_LOGIN",width="50",height="1",  font=("Calibri", 12),command=New_User).pack()
    
def close_window():
    root.destroy()
b4 = tk.Button(f1, text= "CANCEL",width="40",height="1",  font=("Calibri", 12), command = close_window).pack()



#CREATE NEW ACCOUNT

f2 = tk.Frame(root)
root.title("Umashankar Vishwakarma")
l2 = tk.Label(f2, text="-----:: CREATE_NEW_ACCOUNT ::-----",fg="blue",bg="Light Grey", font=("Calibri", 23)).grid(columnspan=5)
name = tk.Label(f2, text='FULL NAME').grid(row=1,column=0)
gender = tk.Label(f2, text='SELECT GENDER').grid(row=2,column=0)
r1=tk.Radiobutton(f2, text="Male",  value=1).grid(row=2,column=1)
r2=tk.Radiobutton(f2, text="Female",  value=2).grid(row=2,column=2)
mob = tk.Label(f2, text='USER ID').grid(row=3,column=0)
password = tk.Label(f2, text='CREATE_PASSWORD').grid(row=4,column=0)
password2 = tk.Label(f2, text='CONFIRM_PASSWORD').grid(row=5,column=0)

def show_entry_fields1():
    print(" FULL NAME :. %s\n USER ID: %s" % (entry1.get(), entry2.get()))
    print(" Successfully  Account Created.........")
entry1 = tk.Entry(f2)
entry1.grid(row=1,column=1)
entry2 = tk.Entry(f2)
entry2.grid(row=3,column=1)
entry3 =tk.Entry(f2,show="*")
entry3.grid(row=4,column=1)
entry4= tk.Entry(f2,show="*")
entry4.grid(row=5,column=1)
b5=tk.Button(f2,text="CREATE", command=show_entry_fields1).grid(row=6,column=1)
b6 = tk.Button(f2, text="CANCEL", command=MEDICINE_INFORMATION_SYSYEM).grid(row=7,column=1)



#~~~~~~~New User Account~~~~~~~~

f5 = tk.Frame(root)
lbl=tk.Label(f5,text="~~~:: NEW USER ACCOUNT ::~~~",fg="blue",bg="Light Grey", font=("Calibri", 23)).grid(columnspan=3)
un1=tk.Label(f5,text="Userame").grid(row=1,column=0)
e1=tk.Entry(f5).grid(row=1,column=1)
w=tk.Label(f5,text="Password").grid(row=2,column=0)
e2=tk.Entry(f5,show="*").grid(row=2,column=1)
b8=tk.Button(f5,text="Login",command=New_User_info).grid(row=3,column=1)
b9 = tk.Button(f5, text="CANCEL", command=MEDICINE_INFORMATION_SYSYEM).grid(row=4,column=1)
chk1= tk.Checkbutton(f5, text="Keep me login").grid(row=3,column=2)

#New User Info Page

f6 = tk.Frame(root)
lbl= tk.Label(f6, text="~~~~: NEW USER INFO PAGE :~~~~",fg="blue",bg="Light Grey", font=("Calibri", 23)).grid(columnspan=2)
lbl1=tk.Label(f6, text="Medicine Sr.No:. ").grid(row=1)
lbl2=tk.Label(f6, text="Medicine Name:").grid(row=2)
lbl3=tk.Label(f6, text="Company Name:").grid(row=3)
lbl4=tk.Label(f6, text="Ingredient Drug Name:").grid(row=4)
lbl5=tk.Label(f6, text="Manufacturing Date:").grid(row=5)
lbl6=tk.Label(f6, text="Expiry Date:").grid(row=6)
lbl7=tk.Label(f6, text="Side Effects:").grid(row=7)

def show_entry_fields2():
    print(" Welcome to Medicine Informetion System")
    print(" Medicine Sr.No:. %s\n Medicine Name: %s\n Company Name: %s\n Ingredient Drug Name: %s\n Manufacturing Date: %s\n Expiry Date: %s\n Side Effects: %s\n "
         % (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get()))

e1 = tk.Entry(f6)
e1.grid(row=1, column=1)
e2 = tk.Entry(f6)
e2.grid(row=2, column=1)
e3 = tk.Entry(f6)
e3.grid(row=3, column=1)
e4 = tk.Entry(f6)
e4.grid(row=4, column=1)
e5 = tk.Entry(f6)
e5.grid(row=5, column=1)
e6 = tk.Entry(f6)
e6.grid(row=6, column=1)
e7 = tk.Entry(f6)
e7.grid(row=7, column=1)
btn1=tk.Button(f6, text='Show Record', command=show_entry_fields2).grid(row=8, column=0)
btn3=tk.Button(f6, text='Search Record').grid(row=8,column=1)
btn5=tk.Button(f6, text='Quit', command=MEDICINE_INFORMATION_SYSYEM).grid(columnspan=2)


#Admin User login page

f3 = tk.Frame(root)
lbl=tk.Label(f3,text="~~~~: ADMIN USER LOGIN PAGE :~~~~~",fg="blue",bg="Light Grey", font=("Calibri", 23)).grid(columnspan=5)
un1=tk.Label(f3,text="Username").grid(row=1,column=0)
e1=tk.Entry(f3).grid(row=1,column=1)
w=tk.Label(f3,text="password").grid(row=2,column=0)
e2=tk.Entry(f3,show="*").grid(row=2,column=1)
b8=tk.Button(f3,text="Login",command=submit).grid(row=3,column=1)
b9 = tk.Button(f3, text="CANCEL", command=MEDICINE_INFORMATION_SYSYEM).grid(row=4,column=1)
chk1= tk.Checkbutton(f3, text="Keep me login").grid(row=3,column=2)

#info page of admin

f4 = tk.Frame(root)
lbl=tk.Label(f4, text="~~~~~: ADMIN INFO PAGE :~~~~~",fg="blue",bg="Light Grey", font=("Calibri", 23)).grid(columnspan=5)
lbl1=tk.Label(f4, text="Medicine Sr.No:. ").grid(row=1)
lbl2=tk.Label(f4, text="Medicine Name:").grid(row=2)
lbl3=tk.Label(f4, text="Company Name:").grid(row=3)
lbl4=tk.Label(f4, text="Ingredient Drug Name:").grid(row=4)
lbl5=tk.Label(f4, text="Manufacturing Date:").grid(row=5)
lbl6=tk.Label(f4, text="Expiry Date:").grid(row=6)
lbl7=tk.Label(f4, text="Side Effects:").grid(row=7)

def show_entry_fields():
    print(" Welcome to Medicine Informetion System")
    print(" Medicine Sr.No:. %s\n Medicine Name: %s\n Company Name: %s\n Ingredient Drug Name: %s\n Manufacturing Date: %s\n Expiry Date: %s\n Side Effects: %s\n "
         % (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get()))

e1 = tk.Entry(f4)
e1.grid(row=1, column=1)
e2 = tk.Entry(f4)
e2.grid(row=2, column=1)
e3 = tk.Entry(f4)
e3.grid(row=3, column=1)
e4 = tk.Entry(f4)
e4.grid(row=4, column=1)
e5 = tk.Entry(f4)
e5.grid(row=5, column=1)
e6 = tk.Entry(f4)
e6.grid(row=6, column=1)
e7 = tk.Entry(f4)
e7.grid(row=7, column=1)
btn1=tk.Button(f4, text='Show Record', command=show_entry_fields).grid(row=8, column=0)
btn2=tk.Button(f4, text='Add Record').grid(row=8,column=1)
btn3=tk.Button(f4, text='Search Record').grid(row=9,column=0)
btn4=tk.Button(f4, text='Update Record').grid(row=9,column=1)
btn5=tk.Button(f4, text='Quit', command=MEDICINE_INFORMATION_SYSYEM).grid(row=10,columnspan=5)
                
f1.pack()
root.mainloop()
