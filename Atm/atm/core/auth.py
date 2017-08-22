# /usr/bin/env python
# coding:utf-8
import os,json
'''数据库文件相对路径'''
db_path=os.path.dirname(os.path.dirname(__file__))+'/database'
def auth_Card():
    '''
    验证用户登录信用卡
    :return: 
    '''
    while True:
           print('\033[0;32m信用卡登录认证\033[0m'.center(50,'-'))
           Card_number=input('\033[0;34m输入信用卡卡号\033[0m:')
           os.chdir(db_path)
           with open('db_card','r') as f:
               db_card_info=json.load(f)
           if db_card_info.get(Card_number):
               while True:
                   Card_Password = input('\033[0;34m输入信用卡密码（6位数字）\033[0m:')
                   if db_card_info[Card_number]['Card_Password'] == Card_Password:
                       print('\033[0;32m 登录成功！\033[0m')
                       return Card_number
                   else:
                       print('\033[0;31m 登录失败！密码错误！\033[0m')
                       continue
           else:
               print('不存在卡号请重新输入！')
               continue


def auth_Admin():
    '''
    验证后台管理登录
    :return: 
    '''
    while True:
           print('\033[0;32m后台管理登录认证\033[0m'.center(50,'-'))
           Admin_user=input('\033[0;34m输入管理员账户\033[0m:')
           # os.chdir(db_path)
           # with open('db_card','r') as f:
           #     db_card_info=json.load(f)
           db_admin_info={'User':'admin','Password':'admin'}
           if db_admin_info['User']==Admin_user:
               while True:
                   Admin_Password = input('\033[0;34m输入管理员账户密码\033[0m:')
                   if db_admin_info['Password'] == Admin_Password:
                       print('\033[0;32m 后台登录成功！\033[0m')
                       return Admin_user
                   else:
                       print('\033[0;31m 登录失败！密码错误！\033[0m')
                       continue
           else:
               print('管理员账户错误请重新输入！')
               continue
