# /usr/bin/env python
# coding:utf-8
import os,sys

path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from core import auth,card_info,admincenter


def Choose_id():
    '''函数用于选择控制第一层级主要功能选择
    获取用户输入ID 传值调用第二层级功能
    返回:None
    '''
    print('\033[0;31m 欢迎进入信用卡购物模拟程序\033[0m'.center(50, '+')
          , '\n【1】购物中心'
          , '\n【2】信用卡中心'
          , '\n【3】账户中心'
          , '\n【4】退出程序')
    Choose_id = input('\033[0;34m 选择要进入的功能ID:\033[0m')
    Main_function(Choose_id)

def Main_function(Choose_id):
    '''函数用于选择控制第二主要功能选择
    返回:None
    '''
    if Choose_id == '1':
        # Choose购物中心
        print('\033[0;31m欢迎进入购物中心\033[0m'.center(50, '+'),
              "\n【1】购物商场\n"
              "【2】查看购物车\n"
              "【3】购物结算\n"
              "【4】个人中心\n"
              "【5】返回\n")
    if Choose_id == '2':
        #....Choose信用卡中心
        #....验证信用卡登录
        auth_Card_info=auth.auth_Card()
        if auth_Card_info:
            while True:
                print('\033[0;31m欢迎进入信用卡中心\033[0m'.center(50, '+'),
                      '\n【1】我的信用卡\n'
                      '【2】转账\n'
                      '【3】提现\n'
                      '【4】还款\n'
                      '【5】流水记录\n'
                      '【b】返回\n')
                Choose_card_id = input('\033[0;34m选择要进入的功能ID:\033[0m')
                if Choose_card_id == "1":
                    card_info.My_card(auth_Card_info)
                elif Choose_card_id == "2":
                    card_info.My_transfer(auth_Card_info)
                elif Choose_card_id == "3":
                    card_info.My_withdraw(auth_Card_info)
                elif Choose_card_id == "4":
                    card_info.My_repayment(auth_Card_info)
                elif Choose_card_id == "5":
                    card_info.My_card_record(auth_Card_info)
                elif Choose_card_id == "b":
                    pass
                else:
                    print("\33[31;0m输入的ID无效，请重新选择\33[0m")

    if Choose_id == '3':
        # Choose账户中心
        # ....验证后台管理登录
        auth_Admin_info = auth.auth_Admin()
        if auth_Admin_info:
            while True:
                print('\033[0;31m欢迎进入账户中心\033[0m'.center(50, '+'),
                      '\n【1】创建账户'
                      '\n【2】锁定账户'
                      '\n【3】解锁账户'
                      '\n【4】发信用卡'
                      '\n【5】调整额度'
                      '\n【6】冻结信用卡'
                      '\n【7】解冻信用卡'
                      )
                Choose_Admin_id = input('\033[0;34m选择要进入的功能ID:\033[0m')
                if Choose_Admin_id == "1":
                    admincenter.Create_user()
                elif Choose_Admin_id == "2":
                    admincenter.Lock_user()
                elif Choose_Admin_id == "3":
                    admincenter.Deblock_user()
                elif Choose_Admin_id == "4":
                    admincenter.Create_card()
                elif Choose_Admin_id == "5":
                    admincenter.Credit_card()
                elif Choose_Admin_id == "6":
                    admincenter.Lock_card()
                elif Choose_Admin_id == "7":
                    admincenter.Deblock_card()
                else:
                    print("\33[31;0m输入的ID无效，请重新选择\33[0m")

    # Choose退出程序
    if Choose_id == '4':
        print('\033[0;37;40m已经退出程序\033[0m')
        exit()


def run():
    '''
    这个函数会调用程序开始时,处理用户交互的东西
    返回:None
    '''
    Choose_id()