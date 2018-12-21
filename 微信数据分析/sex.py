#!/usr/bin/env python
# coding=utf-8
# @auother: 范儿
# Email:2809713313@qq.com

import itchat

# 登录微信
itchat.login()
# 自动登录
# itchat.auto_login(hotReload = True)
def sex():
    friends = []
    # 获取微信好友列表
    friends_lise = itchat.get_friends()[0:]
    male = 0
    famale = 0
    other = 0
    # 数据分析
    for friend in friends_lise[1:]:
        # 获取好友性别
        sex = friend['Sex']
        if sex == 1:
            male += 1
        elif sex == 2:
            famale +=1
        else:
            other += 1
    friends.append(male)
    friends.append(famale)
    friends.append(other)
    return friends

a = sex()
# 分析结果显示
toal = float(a[0])+float(a[1])+float(a[2])
print("微信好友总数：" + str(a[0]+a[1]+a[2]))
print("男性好友人数：" + str(a[0]) + "\t%.2f%%" % (float(a[0])/toal*100))
print("女性好友人数：" + str(a[1]) + "\t%.2f%%" % (float(a[1])/toal*100))
print("无性别好友人数：" + str(a[2]) + "\t%.2f%%" % (float(a[2])/toal*100))