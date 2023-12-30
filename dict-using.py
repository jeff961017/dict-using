def check():
    check_who= input("查詢誰 ")
    if check_who in accounts:
        print(accounts[check_who])
    else:
        print("此用戶不存在")
def change():
    change_who= input("更改誰 ")
    if change_who in accounts:
        change_what= input("改為多少")
        accounts[change_who]['balance'] = change_what
    else:
        print("此用戶不存在")
def deleate():
    deleate_who = input("刪除誰 ")
    if deleate_who in accounts:
        del accounts[deleate_who]
    else:
        print("此用戶不存在")

accounts= {
    'John':{
        'name':'John Doe',
        'balance': 1000 
    },
    'Mary': {
        'name': 'Mary Smith',
        'balance': 500
    }
}
while True:
    account = input("名字 ")
    if account!= "end":
        accounts[account]= {}
        name_input = input("姓名 ")
        balance_input = input("balance ")
        accounts[account]['name']= name_input
        accounts[account]['balance'] = balance_input
    elif account== "end":
        print(accounts)
        break
while True:
    case = input("1.查詢存取用戶的全部資料(姓名及金額) 2.修改用戶的存款金額 3.刪除用戶的全部資料 ")
    if case != "none":
        if case == '1':
            check()
        if case == '2':
            change()
        if case =='3':
            deleate()
    elif case == "none":
        break