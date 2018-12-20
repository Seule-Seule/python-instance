#!/usr/bin/env python
# coding=utf-8
# @auother: 范儿
# Email:2809713313@qq.com

'''
注册的网站太多，为避免忘记，
    写了这个python程序作为我的密码本记录密码。
'''

import init
import password


if __name__ == '__main__':
    init.init()
    while True:
        choose = input("$ You can choose write password(0) or read password(1) : \n>>")
        if int(choose) == 0:
            password.password_w()
        elif int(choose) == 1:
            password.password_r()
        else :
            print("$ Invalid input!Please try again: \n")
                                                                                                            