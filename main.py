from tkinter import *
from BankFunctions import *
from tkinter import messagebox
import turtle
    
def DrawChart():
    def draw():
        account_num = ea.get()
        try:
            draw_chart(token,account_num)       
        except FileNotFoundError:
            messagebox.showinfo('Err','Not Found')        
    l = Tk()
    Label(l, text='Account Number').grid(row=0)
    ea = Entry(l)
    ea.grid(row=0,column=1)
    Button(l, text = "GO",command = draw).grid(row =0, column=2)
    mainloop()
    
def Transaction():
    def transact():
        info_dict = {}
        info_dict['fromAccount'] = e1.get()
        info_dict['toAccount'] = e2.get()
        info_dict['amount'] = int(e3.get())
        info_dict['definition'] = e4.get()
        cash = e5.get()
        if cash == 'true':
            info_dict['cash'] = True
        else:
            info_dict['cash'] = False
        try:
            action = transaction(token,info_dict)
            o = Tk()
            scrollbar = Scrollbar(o)
            scrollbar.pack( side = RIGHT, fill = 'y' )
            transactions = Listbox(o, yscrollcommand=scrollbar.set , height=50, width=100)
            transactions.pack(side=LEFT, fill=BOTH)
            for y in action:
                transactions.insert(END, str(y) + ':' + str(action[y]) + '\n')
            scrollbar.config(command=transactions.yview)
            mainloop()
        except FileNotFoundError:
            messagebox.showinfo('Err','Not Found')
        except FileExistsError:
            messagebox.showinfo('Err','Not Enough Credit')
    k = Tk()
    Label(k, text='From Account').grid(row=0)
    Label(k, text='To Account').grid(row=1)
    Label(k, text='Amount').grid(row=2)
    Label(k, text='Definition').grid(row=3)
    Label(k, text='Cash').grid(row=4)
    e1 = Entry(k)
    e1.grid(row=0 , column=1)
    e2 = Entry(k)
    e2.grid(row=1 , column=1)
    e3 = Entry(k)
    e3.grid(row=2 , column=1)
    e4 = Entry(k)
    e4.grid(row=3 , column=1)
    e5 = Entry(k)
    e5.grid(row=4 , column=1)
    Button(k, text = "OK",command = transact).grid(row =5, column=1)
    
def TransactionList():
    j = Tk()
    try:
        transactionlist = transaction_list(token)
        scrollbar = Scrollbar(j)
        scrollbar.pack( side = RIGHT, fill = 'y' )
        transactions = Listbox(j, yscrollcommand=scrollbar.set , height=50, width=100)
        transactions.pack(side=LEFT, fill=BOTH)
        for x in range (len(transactionlist)):
            for y in transactionlist[x] :
                transactions.insert(END, y + ':' + str(transactionlist[x][y]) + '\n')
        scrollbar.config(command=transactions.yview)
    except FileNotFoundError:
        messagebox.showinfo('Err','Not Found')
    mainloop()
    
def AccountOwnerRetrieve():
    i = Tk()
    try:
        owner_dict = account_owner_retrieve(token)
        scrollbar = Scrollbar(i)
        scrollbar.pack( side = RIGHT, fill = 'y' )
        accountInfo = Listbox(i, yscrollcommand=scrollbar.set , height=50, width=100)
        accountInfo.pack(side=LEFT, fill=BOTH)
        for item in owner_dict:
            if item == 'accounts':
                for account in owner_dict[item]:
                    accountInfo.insert(END,'account:'+ account['accountNumber'] + '\t' + 'status:'+ account['status'] + '\n')
            else:
                accountInfo.insert(END, item +':'+ owner_dict[item] + '\n')
        scrollbar.config(command=accountInfo.yview)       
    except FileNotFoundError :
        messagebox.showinfo('Err','Not Found')
    mainloop()

def BankAccountRetrieve():
    h = Tk()
    try :
        account_info_dict = bank_account_retrieve(token)
        scrollbar = Scrollbar(h)
        scrollbar.pack( side = RIGHT, fill = 'y' )
        accountInfo = Listbox(h, yscrollcommand=scrollbar.set , height=50, width=100)
        accountInfo.pack(side=LEFT, fill=BOTH)
        accountInfo.insert(END,'account number:' + account_info_dict['accountNumber'] + '\n' ) 
        for item in account_info_dict['accountOwner']:
            if item == 'accounts':
                for account in account_info_dict['accountOwner'][item]:
                    accountInfo.insert(END,'account:'+ account['accountNumber'] + '\t' + 'status:'+ account['status'] + '\n')
            else:
                accountInfo.insert(END, item +':'+ account_info_dict['accountOwner'][item] + '\n')
        accountInfo.insert(END, 'credit:'+ str(account_info_dict['credit']) + '\n')
        accountInfo.insert(END, 'status:'+ account_info_dict['status'] + '\n') 
        scrollbar.config(command=accountInfo.yview)
            
    except FileNotFoundError :
        messagebox.showinfo('Err','Not Found')
    mainloop()

def BlockAccount():
    def block():
        accountNum = ea.get()
        responce = block_account(token , accountNum)
        if responce == True :
            messagebox.showinfo('','Account has been blocked')
        else:
            messagebox.showinfo('Err','Not Found')
            
    g = Tk()
    Label(g, text='Account Number').grid(row=0)
    ea = Entry(g)
    ea.grid(row=0,column=1)
    Button(g, text = "GO",command = block).grid(row =0, column=2)
    mainloop()

def CloseAccount():
    def close():
        accountNum = ea.get()
        responce = close_account(token,accountNum)
        if responce == True :
            messagebox.showinfo('','Account has been closed')
        else:
            messagebox.showinfo('Err','Not Found')
            
    f = Tk()
    Label(f, text='Account Number').grid(row=0)
    ea = Entry(f)
    ea.grid(row=0,column=1)
    Button(f, text = "GO",command = close).grid(row =0, column=2)
    mainloop()
    
def AddAccountToAccountOwner():
    def get_account_info():
        nationalcode = enc.get()
        try :
            account_info_dict = add_account_to_account_owner(token,nationalcode)
            n = Tk()
            scrollbar = Scrollbar(n)
            scrollbar.pack( side = RIGHT, fill = 'y' )
            accountInfo = Listbox(n, yscrollcommand=scrollbar.set , height=50, width=100)
            accountInfo.pack(side=LEFT, fill=BOTH)
            accountInfo.insert(END,'account number:' + account_info_dict['accountNumber'] + '\n' ) 
            for item in account_info_dict['accountOwner']:
                if item == 'accounts':
                    for account in account_info_dict['accountOwner'][item]:
                        accountInfo.insert(END,'account:'+ account['accountNumber'] + '\t' + 'status:'+ account['status'] + '\n')
                else:
                    accountInfo.insert(END, item +':'+ account_info_dict['accountOwner'][item] + '\n')
            accountInfo.insert(END, 'credit:'+ str(account_info_dict['credit']) + '\n')
            accountInfo.insert(END, 'status:'+ account_info_dict['status'] + '\n') 
            scrollbar.config(command=accountInfo.yview)
            mainloop()
        except FileNotFoundError :
            messagebox.showinfo('Err','Not Found')
        
    
    e = Tk()
    Label(e, text='National Code').grid(row=0)
    enc = Entry(e)
    enc.grid(row=0,column=1)
    Button(e, text = "GO",command = get_account_info).grid(row =0, column=2)

def GetBankAccountLogs():
    def click():
        account_num = ea.get()
        try:
            logs_dict = get_bank_account_logs(token,account_num)
            m = Tk()
            scrollbar = Scrollbar(m)
            scrollbar.pack( side = RIGHT, fill = 'y' )
            T = Listbox(m, yscrollcommand=scrollbar.set , height=50, width=100)
            T.pack(side=LEFT, fill=BOTH)
            T.insert(END,'Current Credit:' + str(logs_dict['currentCredit']) + '\n')
            for i in range(len(logs_dict['logs'])):
                for item in logs_dict['logs'][i]:
                    T.insert(END,item + ':' + str(logs_dict['logs'][i][item]) + '\n')
            scrollbar.config(command=T.yview)
            mainloop()      
        except FileNotFoundError:
            messagebox.showinfo('Err','Not Found')
            
            
    
    d = Tk()
    Label(d, text='Account Number').grid(row=0)
    ea = Entry(d)
    ea.grid(row=0,column=1)
    Button(d, text = "GO",command = click).grid(row =0, column=2)
    mainloop()
    

def SignUp():
    def Signup():
        username = eu.get()
        password = ep.get()
        responce = sign_up(token,username,password)
        if responce:
            messagebox.showinfo('successful!','you successfully signed up')
        else:
            messagebox.showinfo('Err','this username is already taken')
            
    c = Tk()
    Label(c, text='Username').grid(row=0)
    Label(c, text='Password').grid(row=1)
    eu = Entry(c)
    ep = Entry(c)
    eu.grid(row=0, column=1)
    ep.grid(row=1, column=1)
    button=Button(c, text = "Sign Up",command = Signup).grid(row = 2, column=1)
    c.mainloop()

def Createaccount(): #???
    def get_input():
        owner_info_dict = {}
        owner_info_dict['accountOwner'] = {}
        owner_info_dict['accountOwner']['firstName'] = ef.get()
        owner_info_dict['accountOwner']['lastName'] = el.get()
        owner_info_dict['accountOwner']['phoneNumber'] = ep.get()
        owner_info_dict['accountOwner']['nationalCode'] = en.get()
        try:
            owner_account_dict = owner_bank_account_list(token,owner_info_dict)
            p = Tk()
            scrollbar = Scrollbar(p)
            scrollbar.pack( side = RIGHT, fill = 'y' )
            accounts = Listbox(p, yscrollcommand=scrollbar.set , height=50, width=100)
            accounts.pack(side=LEFT, fill=BOTH)
            accounts.insert(END,'account number:' + owner_account_dict['accountNumber'] + '\n' ) 
            for item in owner_account_dict['accountOwner']:
                if item == 'accounts':
                    for account in owner_account_dict['accountOwner'][item]:
                        accounts.insert(END,'account:'+ account['accountNumber'] + '\t' + 'status:'+ account['status'] + '\n')
                else:
                    accounts.insert(END, item +':'+ owner_account_dict['accountOwner'][item] + '\n')
            accounts.insert(END, 'credit:'+ str(owner_account_dict['credit']) + '\n')
            accounts.insert(END, 'status:'+ owner_account_dict['status'] + '\n') 
            scrollbar.config(command=accounts.yview)
        except FileNotFoundError:
            messagebox.showinfo('Err','Something is wrong,try again')
 
    b = Tk()
    Label(b, text='First Name').grid(row=0)
    Label(b, text='Last Name').grid(row=1)
    Label(b, text='Phone Number').grid(row=2)
    Label(b, text='National Code').grid(row=3)
    ef = Entry(b)
    ef.grid(row=0,column=1)
    el = Entry(b)
    el.grid(row=1,column=1)
    ep = Entry(b)
    ep.grid(row=2,column=1)
    en = Entry(b)
    en.grid(row=3,column=1)
    submit_button=Button(b, text = "Submit",command = get_input).grid(row = 4, column=1)
    mainloop()

def BankAccountList():
    try:
        lst = bank_account_list(token)
        a = Tk()
        scrollbar = Scrollbar(a)
        scrollbar.pack( side = RIGHT, fill = 'y' )
        T = Listbox(a, yscrollcommand=scrollbar.set , height=50, width=100)
        T.pack(side=LEFT, fill=BOTH)
        for i in range (len(lst)):
            T.insert(END,'account number:' + lst[i]['accountNumber'] + '\n' ) 
            for item in lst[i]['accountOwner']:
                if item == 'accounts':
                    for account in lst[i]['accountOwner'][item]:
                        T.insert(END,'account:'+ account['accountNumber'] + '\t' + 'status:'+ account['status'] + '\n')
                else:
                    T.insert(END, item +':'+ lst[i]['accountOwner'][item] + '\n')
            T.insert(END, 'credit:'+ str(lst[i]['credit']) + '\n')
            T.insert(END, 'status:'+ lst[i]['status'] + '\n')
        scrollbar.config(command=T.yview)
        mainloop()
    except FileNotFoundError :
        messagebox.showinfo('Err','Not Found')

def logged ():
    e1.destroy()
    Label(loginScreen, text='WELCOME').grid(row=0)
    bank_account_list = Button(loginScreen,text='List of bank accounts',height=2,width=30,command=BankAccountList).grid(row=1,column=0) #
    owner_bank_account_list = Button(loginScreen , text='Create account', height=2,width=30,command=Createaccount).grid(row=2,column=1)
    sign_up = Button(loginScreen, text='Sign up' , height=2,width=30, command=SignUp).grid(row=1,column=1)#
    get_bank_account_logs = Button(loginScreen, text='Get bank account logs', height=2,width=30 , command=GetBankAccountLogs).grid(row=1,column=2)#
    add_account_to_account_owner = Button(loginScreen, text='Add account to account owner',height=2,width=30, command=AddAccountToAccountOwner).grid(row=3,column=1)#
    close_account = Button(loginScreen, text='Close account',height=2,width=30, command=CloseAccount).grid(row=2,column=0) #
    block_account = Button(loginScreen,text='Block account',height=2,width=30, command=BlockAccount).grid(row=3, column=0) #
    bank_account_retrive = Button(loginScreen, text= 'Retrieve bank account',height=2,width=30 , command=BankAccountRetrieve).grid(row=3,column=2) #
    account_owner_retrieve = Button(loginScreen, text= 'Retrieve account owner', height=2,width=30 , command=AccountOwnerRetrieve).grid(row=3,column=3) #
    transaction_list = Button(loginScreen, text= 'Show transactions', height=2,width=30 , command=TransactionList).grid(row=1,column=3) #
    transaction = Button(loginScreen, text= 'Transaction',height=2,width=30, command=Transaction).grid(row=2,column=3)#
    logs_chart = Button(loginScreen, text= 'Logs Chart',height=2,width=30, command=DrawChart).grid(row=2,column=2) #
      
def login ():
    username = e1.get()
    password = e2.get()
    try:
        global token
        token = log_in(username,password)
        logged()
    except FileNotFoundError:
        messagebox.showinfo('Err','username or password is not valid')
         
loginScreen = Tk()
Label(loginScreen, text='Username').grid(row=0)
Label(loginScreen, text='Password').grid(row=1)
e1 = Entry(loginScreen,)
e2 = Entry(loginScreen,)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
button=Button(loginScreen, text = "Log in",command = login).grid(row = 2, column=1)
loginScreen.mainloop()
