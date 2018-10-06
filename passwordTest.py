password = 'a123456'
chance = 3

while chance <= 3 and chance > 0:   
    userpassword = input('請輸入密碼: ')
    if userpassword == password:
        print('登入成功！')
    else:
        chance = chance - 1
        if chance == 0:
            break
        print('密碼錯誤！還有', chance, '次機會')
print('輸入錯誤次數超過3次，此帳號已暫時鎖定')
        