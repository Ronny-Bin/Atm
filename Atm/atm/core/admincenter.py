# /usr/bin/env python
# coding:utf-8
import os,sys,json
'''数据库文件相对路径'''
path=os.path.dirname(os.path.dirname(__file__))+'/database'
sys.path.append(path)
def db_users(new_info=False):
    '''
    链接db_users数据库
    '''
    os.chdir(path)
    if new_info==False:
        with open('db_users','r') as f:
            user_info=json.load(f)
            return user_info
    else:
        with open('db_users','w') as f:
            json.dump(new_info,f)

def db_card(new_info=False):
    '''
    链接db_card数据库
    '''
    os.chdir(path)
    if new_info==False:
        with open('db_card','r') as f:
            card_info=json.load(f)
            return card_info
    else:
        with open('db_card','w') as f:
            json.dump(new_info,f)
            return True

def Create_user():
    '''
    创建账户
    :return: 
    '''
    user_info=db_users()
    print('开始创建用户'.center(50,'-'))
    for k in  user_info:
        print('系统已有账户：%s'%k)
    flag=False
    while True:
        if flag==False:
            User_name = input('输入添加账户的用户名：')
            if User_name in user_info:
                print('用户已经存在！请重新输入！')
                continue
            else:
                flag = True
        if flag==True:
            User_passwrod = input('输入添加账户的密码：')
            Confirm_passwrod = input('再次输入添加账户的密码：')
            if Confirm_passwrod == User_passwrod:
                print('恭喜！%s用户创建成功！' % User_name)
                dict_none=[]
                for v in user_info.values():
                    dict_none .append(v['Id'])
                User_id=max(dict_none)+1
                user_info[User_name] = {'Id': User_id, 'Name': None, 'Username': User_name, 'Password': User_passwrod,
                                          'Card_number': None, 'locked': 0}
                db_users(user_info)
                break
            else:
                print('两次密码输入不一致，重新输入！')
                continue


def Lock_Decorator(set,db):
    '''
    解锁／锁定用户装饰器
    :param set: 
    :return: 
    '''
    def f_obj(func):
        set_func = lambda  set_info:'解锁' if set_info=='Deblock' else '解锁' if set_info=='Lock' else None
        set_info=set_func(set)
        def wrapp(*args,**kwargs):
            user_info = db()
            print('开始{set_info}用户'.format(set_info=set_info).center(50, '-'))
            for k in user_info:
                if user_info[k]['locked'] == 1:
                    locked_info = '\033[0;31m锁定\033[0m'
                else:
                    locked_info = '\033[0;32m正常\033[0m'
                print('系统已有账户：\033[0;32m%s\033[0m' % k, '状态：%s' % locked_info)
            func(*args, **kwargs)
        return wrapp
    return f_obj

# def Lock_user(set=False):
#     '''
#     锁定用户
#     :return:
#     '''
#     user_info = db_admin()
#     print(user_info)
#     print('开始锁定用户'.center(50, '-'))
#     for k in  user_info:
#         if user_info[k]['locked']==0:
#             locked_info='\033[0;31m锁定\033[0m'
#         else:
#             locked_info='\033[0;32m正常\033[0m'
#         print('系统已有账户：\033[0;32m%s\033[0m'%k,'状态：%s'%locked_info)
#     lock_user=input('输入你要锁定用户的用户名：')
#     if set:
#         user_info[lock_user]['locked'] = 0
#     else:
#         user_info[lock_user]['locked'] = 1
#     db_admin(user_info)
@Lock_Decorator('Deblock',db_users)
def Deblock_user():
    user_info = db_users()
    while True:
        lock_user = input('输入你要解锁用户的用户名：')
        if user_info.get(lock_user):
            user_info[lock_user]['locked'] = 0
            db_users(user_info)
            print('用户%s解锁成功' % lock_user)
            break
        else:
            print('用户名不存在！')
            continue

@Lock_Decorator('Lock',db_users)
def Lock_user():
    user_info = db_users()
    lock_user = input('输入你要锁定用户的用户名：')
    if user_info.get(lock_user):
        user_info[lock_user]['locked'] = 1
        db_users(user_info)
        print('用户%s锁定成功'%lock_user)
    else:
        print('用户名不存在！')

@Lock_Decorator('Deblock',db_card)
def Deblock_card():
    card_info = db_card()
    while True:
        lock_card = input('输入你要解锁信用卡卡号：')
        if card_info.get(lock_card):
            card_info[lock_card]['locked'] = 0
            db_card(card_info)
            print('用户%s解锁成功' % lock_card)
            break
        else:
            print('信用卡不存在！')
            continue
@Lock_Decorator('Lock',db_card)

def Lock_card():
    card_info = db_card()
    lock_card = input('输入你要锁定信用卡卡号：')
    if card_info.get(lock_card):
        card_info[lock_card]['locked'] = 1
        db_card(card_info)
        print('用户%s锁定成功' % lock_card)
    else:
            print('信用卡不存在！')


def Create_card():
    '''
    发信用卡'''
    card_info=db_card()
    print('开始发信用卡'.center(50,'-'))
    for k in  card_info:
            print('系统账户信息  持卡人：%s  信用卡号：%s' % (card_info[k]['Crad_personinfo'],k))
    if_create=input('是否发放新的信用卡，确认【y】取消【n】')
    if if_create=='y':
        while True:
            card_number = input('请输入要发放的信用卡卡号（6位数字）：')
            '''
            判断卡号是否存在
            判断卡号是否6位
            '''
            if len(card_number) != 6:
                print('请输入6位数字卡号')
                continue
            if card_info.get(card_number):
                print('卡号已经存在！')
                continue
            card_password = input('请输入要发放的信用卡的初始密码：')
            card_personinfo = input('请输入要发放的信用卡持卡人姓名：')
            dict_cardid = []
            for v in card_info.values():
                dict_cardid.append(v['Id'])
            card_id = max(dict_cardid) + 1
            card_info[card_number] = {"Id": card_id, "Crad_personinfo": card_personinfo, "Card_number": card_number,
                                      "Card_Password": card_password, "Limit_pay": 0.0, "Limit": 10000.0,
                                      "locked": 0}
            info=db_card(card_info)
            if info:
                print('信用卡：%s发卡成功！' % card_number)
                break
            else:
                print('信用卡：%s发卡失败！' % card_number)
                continue
#Create_card()
'''
调整额度
'''
def Credit_card():
    card_info = db_card()
    print('修改信用卡额度'.center(50, '-'))
    for k in card_info:
        print('信用卡号：%s  总额度：\033[31m%s\033[0m  需还款金额：\033[32m%s\033[0m' % (k,card_info[k]['Limit'],card_info[k]['Limit_pay']))
    if_Credit = input('是否继续信用卡额度修改，确认【y】取消【n】')
    if if_Credit=='y':
        while True:
            card_number = input('请输入想要修改度信用卡卡号（6位数字）：')
            if card_info.get(card_number):
                card_Limit = input('调整信用卡额度为：')
                card_info[card_number]['Limit'] =float(card_Limit)
                info = db_card(card_info)
                if info:
                    print('信用卡：%s额度修改成功！总额度为%s' % (card_number,card_Limit))
                    break
                else:
                    print('信用卡：%s额度修改失败！总额度为%s' % (card_number,card_Limit))
                    continue
            else:
                print('卡号不存在！')
                continue


