import requests
import json
import turtle
base_url = "http://176.9.164.222:2211/"

def log_in (username,password) : #T
    token = requests.post(base_url + 'api/Login', data={'username': username , 'password': password})
    if token.status_code != 200 :
        raise FileNotFoundError
    token = token.json()
    token = token['token']
    return token

def bank_account_list(token): #T
    list_of_bank_accounts = requests.get(base_url + 'api/accounts/BankAccountListCreate',headers={'Authorization': 'JWT ' + token})
    if list_of_bank_accounts.status_code != 200 :
        raise FileNotFoundError
    list_of_bank_accounts = list_of_bank_accounts.json()
    return list_of_bank_accounts

def owner_bank_account_list(token,owner_info_dict):
    data={'accountOwner': owner_info_dict}
    list_of_owner_bank_account = requests.post(base_url + 'api/accounts/BankAccountListCreate', json = data, headers={'Authorization': 'JWT ' + token ,'content-type':'application/json'} )
    code =list_of_owner_bank_account.status_code
    if code != 201 and code != 200:
        raise FileNotFoundError
    list_of_owner_bank_account = list_of_owner_bank_account.json()
    return (code,list_of_owner_bank_account)
 
def sign_up(token,username,password):
    resp = requests.post('http://176.9.164.222:2211/'+ 'api/accounts/User/SignUp', data={'username': username , 'password': password} , headers={'Authorization': 'JWT ' + token})
    resp = resp.json()
    if resp['username'] == ['A user with that username already exists.'] :
        return False
    return True
 
def get_bank_account_logs(token,account_num): #T
    account_logs = requests.post(base_url + 'api/accounts/GetBankAccountLogs' , data={"accountNumber":account_num} ,headers={'Authorization': 'JWT ' + token})
    if account_logs.status_code != 200:
        raise FileNotFoundError
    account_logs = account_logs.json()
    return account_logs
 
def draw_chart(token,account_num):
    dict_logs = get_bank_account_logs(token,account_num)
    currentcredit = dict_logs['currentCredit']
    m = currentcredit
    if len(dict_logs['logs']) >= 10 :
        r = 10
    else:
        r = len(dict_logs['logs'])
    location_dict = {}
    time_dict = {}
    n = 1
    for i in range (len(dict_logs['logs'])-1,len(dict_logs['logs'])-r-1,-1):
        if dict_logs['logs'][i]['logType'] == '+' :
            currentcredit -= dict_logs['logs'][i]['amount']
        else:
            currentcredit += dict_logs['logs'][i]['amount']
        if currentcredit > m :
            m = currentcredit
        time_dict[currentcredit] = dict_logs['logs'][i]['date']
        location_dict[n] = (400 -(700/r)*n , currentcredit)
        n += 1
    for t in location_dict:
        location_dict[t] = (location_dict[t][0] , 400 -(m - location_dict[t][1])*400/m)
    def chart(dic):
        a = turtle.Turtle()
        b = turtle.Turtle()
        c = turtle.Turtle()
        d = turtle.Turtle()
        b.ht()
        a.ht()
        c.ht()
        d.ht()
        d.speed(500)
        n = len(dic)
        d.left(90)
        for j in range(0,len(dic)+1):
            d.up()
            d.goto(-300 + (700/n) * j , -400)
            d.down()
            d.forward(800)
        a.pensize(5)
        b.pensize(5)
        c.pensize(5)
        c.pencolor('red')
        a.speed(400)
        b.speed(400)
        c.speed(400)
        a.up()
        b.up()
        c.up()
        c.goto(-300,0)
        a.goto(-300,0)
        b.goto(-300,0)
        b.st()
        a.st()
        a.speed(3)
        b.speed(3)
        a.down()
        b.down()
        b.left(90)
        a.forward(700)
        b.forward(400)
        b.stamp()
        b.speed(400)
        b.up()
        b.goto(-300,0)
        b.down()
        b.speed(3)
        b.right(180)
        b.forward(400)
        c.goto(dic[len(dic)])
        c.speed(1)
        c.down()
        for i in range (len(dic)-1,0,-1):
            c.goto(dic[i])
        e = turtle.Turtle()
        e.up()
        e.ht()
        e.speed(500)
        e.goto(-500,300)
        credit = list(time_dict.keys())
        for k in range(len(credit)) :
            e.goto(-500,300 - 50*k)
            e.write(time_dict[max(credit)])
            credit.remove(max(credit)) 
    chart(location_dict)
    
def add_account_to_account_owner(token,nationalcode):
    accounts = requests.post('http://176.9.164.222:2211/' + "api/accounts/AddAccountToAccountOwner" , data={"nationalCode":nationalcode}, headers={'Authorization': 'JWT ' + token})
    if accounts.status_code != 200:
        raise FileNotFoundError
    else:
        return accounts.json()

def close_account(token,account_num): #T
    resp = requests.post(base_url + 'api/accounts/CloseAccount', data={'accountNumber':account_num} , headers={'Authorization': 'JWT ' + token})
    if resp.status_code == 200 :
        return True
    return False
 
def block_account(token , accountnum): #T
    resp = requests.post(base_url + 'api/accounts/BlockAccount' , data={'accountNumber': accountnum} , headers={'Authorization': 'JWT ' + token})
    if resp.status_code == 200 :
        return True
    return False
 
def bank_account_retrieve(token):
    resp = requests.get(base_url + 'api/accounts/BankAccountRetrieve/157712224022436000' , headers={'Authorization': 'JWT ' + token})
    if resp.status_code != 200 :
        raise FileNotFoundError
    resp = resp.json()
    return resp
     
def account_owner_retrieve(token):
    resp = requests.get (base_url + 'api/accounts/AccountOwnerRetrieve/2282117778' , headers={'Authorization': 'JWT ' + token})
    if resp.status_code != 200 :
        raise FileNotFoundError
    resp = resp.json()
    return resp
     
def transaction_list(token):
    transaction_list = requests.get(base_url + 'api/transaction/TransactionListCreate',headers={'Authorization': 'JWT ' + token})
    if transaction_list.status_code != 200 :
        raise FileNotFoundError
    transaction_list = transaction_list.json()
    return transaction_list
 
def transaction(token,data_dict):
    transaction = requests.post(base_url + 'api/transaction/TransactionListCreate' , data=data_dict , headers={'Authorization': 'JWT ' + token})
    code = transaction.status_code
    transaction = transaction.json()
    if code != 201 and code != 200 :
        try:
            if transaction['non_field_errors'] ==  ['not enough credit'] :
                raise FileExistsError
        except:
            raise FileNotFoundError
    return transaction
