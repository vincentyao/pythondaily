#!/usr/bin/env python3.5
#-*- coding:utf8-*-
from tkinter import *
import tkinter.messagebox as messagebox
# from PIL import Image
# import pytesseract
#
# im=Image.open('loginVerify.jpeg')

# im.load()
# im.split()
#
# vcode=pytesseract.image_to_string(im)
#
# print(vcode)


# imry=im.convert('L')
#
#
# threshold=130
# table=[]
#
# for i in range(256):
#     if i<threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# out=imry.point(table,'1')
#
# out.save('xxx','jpeg')
# text=pytesseract.image_to_string(out)
#
# print(text)
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Entry()
        self.nameInput.pack()
        self.alertButton=Button(self,text='hello',command=self.hello)
        self.alertButton.pack()
        self.helloLablel=Label(self,text='hello,python3 world!')
        self.helloLablel.pack()
        self.quitButton=Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('message','hello,%s'%name)


app=Application()
app.master.title('hello,python3 world')
app.mainloop()
