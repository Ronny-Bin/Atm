# /usr/bin/env python
# coding:utf-8
'''
|++ 程序主入口
'''
import os,sys
path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from core import main
if __name__=='__main__':
    main.run()