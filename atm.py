import pyodbc
from tkinter import *
from tkinter import messagebox

def read(connection):
    print("Read")
    cursor=connection.cursor()
    cursor.execute("select * from BANK.dbo.Customers_Data ")
    for row in cursor:
        print(f'row = {row}')
    print()

def create(connection):
    global Name,Phone,Adress,NIC,Balance,Email,Passwd
    print("Create")
    cursor=connection.cursor()
    cursor.execute(
        'insert into BANK.dbo.Customers_Data(Name,Phone,Adress,NIC,Balance,Email,Passwd) values(?,?,?,?,?,?,?);',
        (Name,Phone,Adress,NIC,Balance,Email,Passwd)
    )
    connection.commit()

    read(connection)#calling read fucntion to see the changes

def update(connection):
    global text
    text="ali"
    print("Update")
    cursor=connection.cursor()
    cursor.execute(
        'update BANK.dbo.Customers_Data set Name=? where Customers_Id=?;',
        (text,3020)
    )
    connection.commit()
    read(connection)#calling read fucntion to see the changes

def delete(connection):
    print("Delete")
    cursor=connection.cursor()
    cursor.execute(
        'delete from BANK.dbo.Customers_Data  where Customers_Id=3039;'
    )
    connection.commit()
    read(connection)#calling read fucntion to see the changes


def getEntries():
    global Name, Phone, Adress, NIC, Balance, Email, Passwd,accCreate

    Name = entry1.get()
    Phone = entry7.get()
    Adress = entry5.get()
    NIC = entry2.get()
    Email = entry3.get()
    Passwd = entry4.get()

    Balance=entry6.get()
    # Balance feild should be a integer
    try:
        Balance = eval(entry6.get())
    except:
        messagebox.showerror("error", "Bank balance should be written in Numeric ")

    global changeNIC
    changeNIC = ""
    global flag
    flag=0
    def trying(connection):
        cursor = connection.cursor()
        cursor.execute("select NIC,Email from BANK.dbo.Customers_Data")
        for row in cursor:
            if NIC == row[0]:  # enrty meun jo NIC  likha hai agar wo pehle se exist karta ho
                global changeNIC
                changeNIC = NIC  # to us NIC  ko ek variable mein save kar dia  jaye

        for i in Email:
            if(i=='@'):
                global flag
                flag=1

    trying(connection)

    if(Name=="" or Phone=="" or Adress=="" or NIC=="" or Balance=="" or Email=="" or Passwd=="" ):

        messagebox.showerror("error", "All fields are required ")
        # none=StringVar()
        # none.set("")
        # noneLable=Label(reg_screen,text="All feilds are required")
        # noneLable.place(x=30, y=220)

    elif changeNIC==NIC:
        messagebox.showerror("error", " This NIC Exits ")
        # none = StringVar()
        # none.set("")
        # noneLable = Label(reg_screen, text="exists",fg="green")
        # noneLable.place(x=30, y=260)
    elif flag==0:
        messagebox.showerror("error", " @ is required ")
        # none = StringVar()
        # none.set("")
        # noneLable = Label(reg_screen, text="@ is missing", fg="green")
        # noneLable.place(x=300, y=30)
    # elif isinstance(Balance,(str,float,complex)):
    #     messagebox.showerror("error","Should be a mumneric value")


    else:
        create(connection)
        accCreate.set("Account Created")

8
def Sign_up():
    global entry1, entry2, entry3, entry4, entry5, entry6, entry7,reg_screen,accCreate
    top.withdraw()
    reg_screen= Toplevel()#this will close the old tkinter screen and create a new screen
    reg_screen.geometry("450x450")

    l1 = Label(reg_screen, text="Name", font=("Arial", "10", "bold"), fg="green").place(x=10, y=10)
    entry1 = Entry(reg_screen, width="25")
    entry1.place(x=100, y=10)

    l2 = Label(reg_screen, text="NIC", font=("Arial", "10", "bold"), fg="green").place(x=10, y=40)
    entry2 = Entry(reg_screen, width="25")
    entry2.place(x=100, y=40)

    l3 = Label(reg_screen, text="Email", font=("Arial", "10", "bold"), fg="green").place(x=10, y=70)
    entry3 = Entry(reg_screen, width="25")
    entry3.place(x=100, y=70)

    l4 = Label(reg_screen, text="password", font=("Arial", "10", "bold"), fg="green").place(x=10, y=100)
    entry4 = Entry(reg_screen, width="25")
    entry4.place(x=100, y=100)

    l5 = Label(reg_screen, text="Address", font=("Arial", "10", "bold"), fg="green").place(x=10, y=130)
    entry5 = Entry(reg_screen, width="25")
    entry5.place(x=100, y=130)

    l6 = Label(reg_screen, text="Balance", font=("Arial", "10", "bold"), fg="green").place(x=10, y=160)
    entry6 = Entry(reg_screen, width="25")
    entry6.place(x=100, y=160)

    l7 = Label(reg_screen, text="Phone", font=("Arial", "10", "bold"), fg="green").place(x=10, y=190)
    entry7 = Entry(reg_screen, width="25")
    entry7.place(x=100, y=190)

    accCreate = StringVar()
    accCreate.set("")
    accCreateLable = Label(reg_screen, textvariable=accCreate, font=("Arial", "10", "bold"), fg="green")
    accCreateLable.place(x=30, y=220)

    createBtn = Button(reg_screen, text="create", font=("Arial", "10", "italic"), activebackground="red",command=getEntries)
    createBtn.place(x=350, y=400)

def checkLogin():


    global login1Entry,login2Entry,flag1,login_screen
    checkNIC=login1Entry.get()
    checkPaswd=login2Entry.get()

    flag1 =0
    def trying(connection):

        cursor = connection.cursor()
        cursor.execute("select NIC,Passwd,Name,Balance from BANK.dbo.Customers_Data")
        for row in cursor:
            if checkNIC == row[0] and checkPaswd==row[1]:  # enrty meun jo NIC  likha hai agar wo pehle se exist karta ho
                global  flag1,get_custmr_name,get_custmr_balance
                get_custmr_name=StringVar()#AFTER SUCCESSFULL LOGIN I WILL PRINT THIS name on the top
                get_custmr_name.set(row[2])
                get_custmr_balance=StringVar()
                get_custmr_balance.set(row[3])

                flag1=1


    trying(connection)

    if flag1==1:
        login_screen.withdraw()
        customer_Account=Toplevel()
        customer_Account.geometry("1000x1000")


        def wDraw_Scr_entry_get():
            global  withdraw_Screen,wDraw_Scr_entry
            amount_entered = int(wDraw_Scr_entry.get())

            def trying(connection):

                cursor = connection.cursor()
                cursor.execute("select Balance from BANK.dbo.Customers_Data where NIC='{0}'".format(checkNIC))
                for row in cursor:
                    if row[0]>=amount_entered:

                        remaining_Balance=int(row[0])-amount_entered

                        cursor.execute(
                            'update BANK.dbo.Customers_Data set Balance=? where NIC =?;',
                            (remaining_Balance, checkNIC)
                        )
                        connection.commit()
                        messagebox.showinfo("Information","Withdraw Successful")
                    else:
                        messagebox.askretrycancel("app","You have insuffiecient balance")


            trying(connection)

        def withdraw_func():
            customer_Account.withdraw()
            withdraw_Screen=Toplevel()
            withdraw_Screen.geometry("1000x500")
            wDraw_Scr_lbl = Label(withdraw_Screen, text="Enter Your amount ", font=("Imprint MT Shadow", "32", "bold"),fg="green")
            wDraw_Scr_lbl.place(x=50, y=20)
            global wDraw_Scr_entry
            wDraw_Scr_entry=Entry(withdraw_Screen, font=("Imprint MT Shadow", "32", "bold"))
            wDraw_Scr_entry.place(x=60, y=100)

            wDraw_Scr_btn = Button(withdraw_Screen, text="Enter", font=("Arial", "10", "italic"), activebackground="red",command=wDraw_Scr_entry_get)
            wDraw_Scr_btn.place(x=200, y=300)

        def deposit_Scr_entry_get():

            global deposit_Screen,dpst_Scr_entry
            amount_entered = int(dpst_Scr_entry.get())

            def trying(connection):
                cursor = connection.cursor()
                cursor.execute("select Balance from BANK.dbo.Customers_Data where NIC='{0}'".format(checkNIC))
                for row in cursor:
                    if amount_entered>=0:

                        remaining_Balance = int(row[0]) + amount_entered

                        cursor.execute(
                            'update BANK.dbo.Customers_Data set Balance=? where NIC =?;',
                            (remaining_Balance, checkNIC)
                        )
                        connection.commit()
                        messagebox.showinfo("Information", "Amount Deposited")
                    else:
                        messagebox.askretrycancel("app", "Amount Should be Positive integer")

            trying(connection)

        def deposit_func():
            customer_Account.withdraw()
            deposit_Screen = Toplevel()
            deposit_Screen.geometry("1000x500")
            dpst_Scr_lbl = Label(deposit_Screen, text="Enter Your amount ", font=("Imprint MT Shadow", "32", "bold"),fg="green")
            dpst_Scr_lbl.place(x=50, y=20)
            global dpst_Scr_entry
            dpst_Scr_entry = Entry(deposit_Screen, font=("Imprint MT Shadow", "32", "bold"))
            dpst_Scr_entry.place(x=60, y=100)

            dpst_Scr_btn = Button(deposit_Screen, text="Enter", font=("Arial", "10", "italic"),activebackground="red", command=deposit_Scr_entry_get)
            dpst_Scr_btn.place(x=200, y=300)



        def blnc_Scr_entry_get():
            print("helo")
        def Balance_func():
            customer_Account.withdraw()
            balance_Screen = Toplevel()
            balance_Screen.geometry("1000x500")

            balance_Screen_lbl_hello = Label(balance_Screen, text="Welcome",font=("Imprint MT Shadow", "32", "bold"), fg="green")
            balance_Screen_lbl_hello.place(x=50, y=20)
            balance_Screen_lbl_name = Label(balance_Screen, textvariable=get_custmr_name, font=("Imprint MT Shadow", "32", "bold"),fg="green")
            balance_Screen_lbl_name.place(x=240, y=20)

            balance_Screen_lbl_accnt = Label(balance_Screen, text="Your account has ",font=("Imprint MT Shadow", "32", "bold"), fg="green")
            balance_Screen_lbl_accnt.place(x=30, y=80)

            balance_Screen_lbl_accnt_balnce = Label(balance_Screen, textvariable=get_custmr_balance,font=("Imprint MT Shadow", "32", "bold"), fg="green")
            balance_Screen_lbl_accnt_balnce.place(x=400, y=200)

            def back_fucn():
                balance_Screen.withdraw()
                checkLogin()
            back = Button(balance_Screen, text="back", font=("Arial", "20", "italic"), activebackground="red",command=back_fucn)
            back.place(x=350, y=400)

        global get_custmr_name
        wellcome = Label(customer_Account, text="Welcome ", font=("Imprint MT Shadow", "32", "bold"), fg="green").place(x=10, y=20)
        custmr_name = Label(customer_Account, textvariable=get_custmr_name, font=("Imprint MT Shadow", "32", "bold"), fg="green")
        custmr_name.place(x=230, y=20)
        wellcome1 = Label(customer_Account, text="You may proceed", font=("Imprint MT Shadow", "20", "bold"),fg="green").place(x=10, y=70)


        withdraw = Button(customer_Account, text="Withdraw", font=("Arial", "30", "italic"), activebackground="blue",command=withdraw_func)
        withdraw.place(x=100, y=150)

        deposit = Button(customer_Account, text="Deposit", font=("Arial", "30", "italic"), activebackground="blue",command=deposit_func)
        deposit.place(x=100, y=250)

        balancee = Button(customer_Account, text="Details", font=("Arial", "30", "italic"), activebackground="blue",command=Balance_func)
        balancee.place(x=100, y=350)

    else:
        messagebox.showerror("error","Invalid NIC or Password")

def Sign_in():
    global login_screen
    top.withdraw()
    login_screen = Toplevel()
    login_screen.geometry("450x450")

    global login1Entry,login2Entry
    login1 = Label(login_screen, text="CNIC NO", font=("Arial", "20", "bold"), fg="green").place(x=10, y=100)
    login1Entry= Entry(login_screen, width="20",font=(20))#font is used for height
    login1Entry.place(x=150, y=100)

    login2 = Label(login_screen, text="Password", font=("Arial", "20", "bold"), fg="green").place(x=10, y=180)
    login2Entry = Entry(login_screen, width="20",font=(20))
    login2Entry.place(x=150, y=180)

    login = Button(login_screen, text="Login", font=("Arial", "10", "italic"), activebackground="red",command=checkLogin).place(x=350, y=400)
##################################################################################################
################################Connecting my database  with sql server ##################
##################################################################################################
connection=pyodbc.connect(
    'Driver={SQL SERVER Native Client 11.0};'
    'Server=DESKTOP-OD0A6LL\SQLEXPRESS;'
    'Database=BANK;'
    'Trusted_Connection=yes;'
)
##################################################################################################
################################From here the program started to run ##################
##################################################################################################

top=Tk()
top.title("Home Screen")
top.geometry("450x450")
top.configure(bg="silver")
welcomeBank = Label(top, text="Welcome to ABD Bank ", font=("Arial", "20", "bold"), fg="green").place(x=80, y=140)

##################################################################################################
################################Create your bank account ##################
##################################################################################################

signup=Button(top,text="Sign up",font=("Arial","30","italic"),activebackground="blue",command=Sign_up).place(x=30,y=310)

##################################################################################################
################################Login to your bank account ##################
##################################################################################################

signin=Button(top, text="Sign in", font=("Arial","30","italic"), activebackground="blue", command=Sign_in).place(x=260, y=310)
top.mainloop()
