#!/usr/bin/env python3.5
#-*- coding:utf8 -*-
from flask import Flask
from flask import request
from flask import render_template

# app =Flask(__name__)
#
# @app.route('/',methods=['GET','POST'])
# def home():
#     return '<h1>home</h1>'
#
# @app.route('/signin',methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="Submit">Sing In</button></p>
#               </from>'''
# @app.route('/signin',methods=['post'])
# def signin():
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>hello,admin!~</h3>'
#     return  '<h3>Bad Username or password!</h3>'
#
# if __name__=='__main__':
#     app.run(host='',port='8000')

# app = Flask(__name__)
# @app.route('/',methods=['GET','POST'])
# def home():
#     return render_template('home.html')
#
# @app.route('/signin',methods=['GET'])
# def signin_form():
#     return render_template('form.html')
#
# @app.route('/signin',methods=['POST'])
# def signin():
#     username=request.form['username']
#     password=request.form['password']
#     if username=='admin' and password=='wodeshijie':
#         return render_template('signin-ok.html',username=password)
#     return render_template('form.html',message='Bad username or password',username=username)
#
# if __name__=='__main__':
#     app.run()
