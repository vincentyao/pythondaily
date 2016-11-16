#!/usr/bin/env python3.5
#-*- coding:utf8 -*-
# from types import MethodType
# from enum import Enum

# class student(object):
#     def __init__(self,name,score):
#         self.__name=name
#         self.__score=score

    # def scoreValue(self):
    #     print('%s,%s'%(self.__name,self.__score))

#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_name(self,name):
#         self.__name=name
#
# bart = student('meng chong', 59)
# lisa = student('lisa dan', 85)
# bart = student()
# lisa = student()
#
# bart.name='lisa dai'
# bart.score=89


# class student(object):
#     __slots__=('name','age')


# def set_age(self,age):
#     self.age=age
#
# class student(object):
#     __slots__=('name')
#     pass

    # def __init__(self,name):
    #     self.name = name



    # def setName(self,name):
    #     self.name = name

#s = student()

# s.name = 'michael'
# del s.name
#
# print(s.name)
#
# s.set_age = MethodType(set_age, s)
# s.set_age(28)
# print(s.age)
# print(s.name)



# bart.scoreValue()
# lisa.scoreValue()

# print(bart.get_score())
#
# print(bart.get_name())
#
# print(round(2.345+8.919,1))

# a=[1,3,2]
# error = 'error occured'
#
# print(hasattr(a, '4',error))

# def FactoryModel(formatInput):
#     callFunc = getattr(formatInput, "%s"%formatInput)
#     return callFunc()

# class student(object):
#     __slots__=('name','age')
#
# def tall(self,tall):
#     self.tall=tall
#
# s=student()
# s.age=18
# s.name='lemon'
# s.tall=MethodType(tall,s)

# class student(object):
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!~')
#         if value<0 or value>100:
#             raise('score must between 0~100!~')
#         self.__x=value

# s= student()
# s.x=99
# print(s.x)
# s.set_score(99.03)
# print(s.get_score())

# class student(object):
#     def __init__(self):
#         self.a,self.b=0,1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>10000:
#             raise StopIteration()
#         return self.a
#
#     def __getattribute__(self,FunctionDiy):
#         return lambda:not find
#
#     def PrintFunc(self):
#         for n in self:
#             print(n)
# s= student()
# s.PrintFunc()


# try:
#    print('try')
#    r=10/0
#    print('result:',r)
# except ZeroDivisionError as e:
#    print('excepting:',e)
#    raise ValueError
# finally:
#    print('coding is running continue...')
