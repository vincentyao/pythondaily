#!/usr/bin/env python3.5
#-*- coding:utf8-*-
# from urllib import request
# from html.parser import HTMLParser
# from html.entities import name2codepoint
# import time
# import threading
# import base64
# from urllib import request,parse
# def loop():
#     print('thread %s is running...'%threading.currentThread().name)
#     n=0
#
#     while n<5:
#         n=n+1
#         print('thread %s is running'%(threading.currentThread().name))
#         time.sleep(1)
#         print('thread %s ended.'%threading.currentThread().name)
#
# print('thread %s is running......'%threading.currentThread().name)
#
# t=threading.Thread(target=loop)
# t.start()
# t.join()
#
# base64.urlsafe_b64encode
#
# print('thread %s ended..................'%threading.currentThread().name)

# with request.urlopen('https://lender.wolaidai.com/#/')as f:
#     content=f.read()
#
#     print('Status:',f.status,f.reason)
#
#
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#
#     print('=============================')
#
#     print('Data:',content.decode('utf-8'))
#
# req = request.Request('https://lender.wolaidai.com/#/')
#
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376eSafari/8536.25')
#
# with request.urlopen(req)as f:
#     print('Data:',f.read().decode('utf8'))

# telNumber = input('telNumber:')
# passwd = input('passwd:')
#
# login_data = parse.urlencode([('username',telNumber),('passwd',passwd)])

# print('login to weibo.cn...')
#
# email=input('email:')
# passwd=input('PassWord:')
#
# login_data=parse.urlencode([
# ('username', email), ('password', passwd), ('entry', 'mweibo'), ('client_id', ''), ('savestate', '1'), ('ec', ''), ('pagerefer',
# 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn %2F')
# ])
#
# req=request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2 F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req,data=login_data.encode('utf8'))as f:
#     print('status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('data:',f.read().decode('utf8'))
