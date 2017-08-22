# /usr/bin/env python
# coding:utf-8
import os,json
'''数据库文件相对路径'''
db_path=os.path.dirname(os.path.dirname(__file__))+'/database'
os.chdir(db_path)
def db_json(card_newinfo=False,db='db_card'):
    '''
    数据库交互
    :return: 
    '''
    if card_newinfo:
        with open('db_card', 'w') as f:
            json.dump(card_newinfo, f)
            #f.write( json.dumps(card_newinfo))
    else:
        with open(db, 'r') as f:
            dbreturn_info = json.load(f)
        return dbreturn_info


def My_card(Card_number):
    '''
    查看信用卡信息
    :param Card_number: 
    :return: 
    '''
    My_card_info=db_json()[Card_number]
    if My_card_info['locked']==0:
        My_card_locked='\033[0;42m 正常 \033[0m'
    else:
        My_card_locked = '\033[0;31m 锁定\033[0m'
    print(
        '\033[0;32m 我的信用卡信息 \033[0m'.center(50,'='),
        '\n卡号：%s'%My_card_info['Card_number'],
        '\n总额度：\033[0;32m %s\033[0m'%My_card_info['Limit'],
        '\n可用额度：\033[0;32m %s\033[0m'%(My_card_info['Limit']-My_card_info['Limit_pay']),
        '\n持卡人姓名：%s'%My_card_info['Crad_personinfo'],
        '\n状态:%s'%(My_card_locked)
    )
    return  My_card_info


# def  Transaction_function(Card_number,action):
#     '''实现信用卡转账／提现/还款功能模块'''
#     card_info=db_json()
#     My_card_info = card_info[Card_number]
#     print('\033[0;32m %s \033[0m'%action.center(30, '-'))
#     if action=='还款':
#         withdraw_Amount=My_card_info['Limit']-My_card_info['Limit_balance']
#         print('你的信用卡需还款：\033[0;31m %s \033[0m' % (withdraw_Amount))
#     else:
#         print('你的可用%s额度为：\033[0;32m %s \033[0m' % (action, My_card_info['Limit_balance']))
#     while True:
#         Transaction_number = input('\033[0;34m输入你要%s金额：\033[0m'%action)
#         try:
#             Transaction_number=round(float(Transaction_number),2)#保留两位小数点
#             if action == '还款':
#                 if Transaction_number <= withdraw_Amount:
#                     New_Limit_balance = My_card_info['Limit_balance'] + Transaction_number
#                 else:
#                     print('\033[0;31m %s金额不能超出当前欠款金额 \033[0m' % action)
#                     continue
#             else:
#                 if Transaction_number <= My_card_info['Limit_balance']:
#                     New_Limit_balance = My_card_info['Limit_balance'] - Transaction_number
#                 else:
#                     print('\033[0;31m %s金额不能大于信用卡可用金额 \033[0m' % action)
#                     continue
#             Confirm_Transaction = input('%s金额为：\033[0;31m%s\033[0m\n是否确认？y/n' % (action, Transaction_number))
#             if Confirm_Transaction == 'y':
#                 print('\033[0;32m%s成功！\033[0m\n你的信用卡可用额度\033[0;31m %s \033[0m' % (action, New_Limit_balance))
#                 card_info[Card_number]['Limit_balance'] = New_Limit_balance
#                 db_json(card_info)
#                 break
#             else:
#                 print('已经取消本次交易！')
#                 continue
#         except:
#             print('\033[0;31m 请输入正确度数字 \033[0m')

'''信用卡装饰器'''
def  Transaction_function(Card_number,action):
    '''实现信用卡转账／提现/还款功能模块'''
    card_info=db_json()
    My_card_info = card_info[Card_number]
    print('\033[0;32m %s \033[0m'%action.center(30, '-'))
    if action=='还款':
        print('你的信用卡需还款：\033[0;31m %s \033[0m' % My_card_info['Limit_pay'])
    else:
        print('你的可用%s额度为：\033[0;32m %s \033[0m' % (action, My_card_info['Limit']-My_card_info['Limit_pay']))
    while True:
        Transaction_number = input('\033[0;34m输入你要%s金额：\033[0m'%action)
        try:
            Transaction_number=round(float(Transaction_number),2)#保留两位小数点
            if action == '还款':
                if Transaction_number <= My_card_info['Limit_pay']:
                    New_Limit_pay = My_card_info['Limit_pay'] - Transaction_number
                else:
                    print('\033[0;31m %s金额不能超出当前欠款金额 \033[0m' % action)
                    continue
            else:
                if Transaction_number <= (My_card_info['Limit']-My_card_info['Limit_pay']):
                    New_Limit_pay = My_card_info['Limit_pay'] + Transaction_number
                else:
                    print('\033[0;31m %s金额不能大于信用卡可用金额 \033[0m' % action)
                    continue
            Confirm_Transaction = input('%s金额为：\033[0;31m%s\033[0m\n是否确认？y/n' % (action, Transaction_number))
            if Confirm_Transaction == 'y':
                print('\033[0;32m%s成功！\033[0m\n你的信用卡可用额度\033[0;31m %s \033[0m' % (action, (My_card_info['Limit']-New_Limit_pay)))
                card_info[Card_number]['Limit_pay'] = New_Limit_pay
                db_json(card_newinfo=card_info)

                break
            else:
                print('已经取消本次交易！')
                continue
        except:
            print('\033[0;31m 请输入正确度数字 \033[0m')


def My_transfer(Card_number):
    '''
       实现信用卡转账
       :param Card_number: 
       :return: 
       '''
    Transaction_function(Card_number, action='转账')
def My_withdraw(Card_number):
    '''
       实现信用卡提现
       :param Card_number: 
       :return: 
       '''
    Transaction_function(Card_number,action= '提现')
def My_repayment(Card_number):
    '''
       实现信用卡还款
       :param Card_number: 
       :return: 
       '''
    Transaction_function(Card_number,action= '还款')
def My_card_record(Card_number):
    '''
       实现信用卡记录查询
       :param Card_number: 
       :return: 
       '''
    print('\033[0;32m 信用卡流水单 \033[0m'.center(50, '-'))
    Time_record=input('\033[0;34m输入你要查询日期：\n\033[0m' )
    My_card_record=db_json(db='db_card_record')[Card_number]
    My_card_recordinfo=My_card_record[Time_record]
    print('\033[0;31m信用卡%s在%s交易记录如下\n\033[0m'%(Card_number,Time_record))
    for k,v in My_card_recordinfo.items():
        print('时间:%s %s %s'%(k,v[0],v[1]))

