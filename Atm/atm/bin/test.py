# /usr/bin/env python
# coding:utf-8
# number=input('number:')
# print(round(float(number),2))
# import json
# json_info={'name':{'key':100,'value':['微信支付',1000]}}
# new_json=json.dumps(json_info)
# print(json.loads(new_json))
#
#
# a={"8888":{"2017-05-09":{"09:59:31":["购物支付",1000]},"2017-06-09":{"09:59:31":["还款",800]},"2017-07-09":{"09:59:31":["转账",1200]}}}
# def stu_register(course='english',name='ronny'):
#     print("----注册学生信息------")
#     print("姓名:",name)
#     print("课程:",course)
# stu_register(name='ronny')
#
#
# dict={'name':{1:'a',2:'b'}}
# dict['roman']={1:'c',2:'d'}
# print(dict)



a={'Ronny': {'Id': 1001, 'Name': '彭彬', 'Username': 'Ronny', 'Password': '1234', 'Card_number': '8888', 'locked': 0}, 'Roman': {'Id': 1002, 'Name': '王菲', 'Username': 'Roman', 'Password': '1234', 'Card_number': '8889', 'locked': 0}, 'User_name': {'Id': 1003, 'Name': None, 'Username': 'roman', 'Password': 'sd', 'Card_number': None, 'locked': None}}
b=a.values()
c=[]
for v in b:
   print(max(v))

print(max(c))