#!/usr/bin/env python3.5
# -*- coding:utf8 -*-
# from random import shuffle
# def findPrime(values):
#     res = True
#
#     for num in range(2,values+1):
#         if values%num==0:
#             res = False
#             return res
#         return res
# joke = list([primeNum for primeNum in range(100)if findPrime(primeNum)])

# primeNum = []
# for n in range(1,100):
#     primeNum.append(n)
#
# r = map(findPrime,primeNum)
#
# joke = list(r)
#
# for result in joke:
#     if(result):
#         print(primeNum)
# original_f = open('uin.txt','r')
# uins = original_f.readlines()
# print('uins cnt:',len(uins))
# original_f.close()
#
#
#
# result =open('send_product:','a')
# shuffle(uins)
# for uin in uins[:1500000]:
#     result.write(uin)
# result.close()
import os
old = 72;
new_source = 85;

r1 = (new_source-old)/old

print('upgrade percent is %.2f' % r1)

classmate = ['m','r','l','c']

classmate.append('A')
classmate.insert(1, 'G')
classmate.pop()
classmate.pop(1)
classmate.append(['999','nverhong'])
print(classmate[4][0])

classmate2 = ('lan','rockey',['monica','lemon'])

classmate2[2].append('stringer')

classmate2[2][0] = 'Alun'
print(classmate2)

age = 20
if age >=18:
    print('%s age is %s'%('michael',age))
else:
    print('else')

age = input('please input your age:')

age_input = int(age)
if age_input >2000:
    print('age result is 00')
else:
    print('age result is before 00')

xiaoming_high = 1.75
xiaoming_weight = 80.5
BMI_value = xiaoming_weight/(xiaoming_high*xiaoming_high)
BMI_value_s = round(BMI_value,2)
if BMI_value<18.5:
    print('less 18.5,too small')
elif BMI_value_s>=18.5 and BMI_value_s<=25:
    print('generation is ok')
else:
    print('done')

if not os.path.exists('testdir'):
    os.makedirs('testdir')

def enroll (name,age,sex='male',address='ShenZhen'):

def addEnd(L=None):
    if L is None:
        L=[]
        L.append['add']
        return L

def person(name,age,**km):
    if 'city' in km:
        pass
    elif 'job' in km:
        pass for job

def fun(name,age,city='shanghai',*km,*,city_choice,):
def def_name(*(1,2,3))
def def_name_2(*[1,2,3])
def func(**{'ip':192.1.1.9,'port':3306})

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

L=[1,2,3,4,5]
L[0:3]
L[:20:5]

dic = {'ip':192.1.1.9,'port':3306}

for key in d:
    print('key==>'key)
for k,v in dic.item:
for value in d.value
