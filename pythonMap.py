#!/usr/bin/env python3.5
#-*- coding:utf8 -*-
import functools

# from functools import reduce
# import itertools
# import time

# def f(x,y):
#     return x + y
#
# f2 = [1,2,3,4,5]
# f3 = [1,3,5,7,9]
#
# r = reduce(f, f3)
# print(r)
#
#
# s=['a','','b']
# def not_empty(s):
#     return s and s.strip()
# res = filter(not_empty, s)
#
# joke = list(res)
#
# print('joke is joke:')
#
# print(joke)

# def find_prime(x):
#     res = True
#     for num in range(2,x+1):
#         if x%num == 0:
#             res = False
#             return res
#         return res
#
# number = int(input("enter primeNum:"))
# joke = [d for d in range(number)if find_prime(d)]
#
# for n in (1,2):
#     joke.insert(0, n)
#

# print(sorted(joke))

# iter = itertools.permutations([1,2,3])
#
# print(list(iter))

# def fast():
#     time.sleep(0.001)
# def slow():
#     time.sleep(0.01)
# def very_slow():
#     for i in range(100):
#         fast()
#         slow()
#         time.sleep(0.1)
# def main():
#     very_slow()
#     very_slow()
#
# if __name__=='__main__':
#     main()

# def lazy_sum(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax = ax+n
#         return ax
#     return sum
#
# re=lazy_sum(1,3,5,7,9)
#
# print(re())
#
# list(map(lambda x:x*x,[1,2,3]))


#decorator demo
# def salesGirl(method):
#     def serve(*args):
#         print("salesGirl:Hello,what do you want?",method.__name__)
#         result =  method(*args)
#
#         if result:
#             print('salesGirl:this shirt you will pay for it $50')
#         else:
#             print('salesGirl:Well,how about this shirt?')
#         return result
#     return serve
#
# @salesGirl
# def try_this_shirt(size):
#     if size<35:
#         print ("I:%d inches is to small to me"%size)
#         return False
#     else:
#         print ("I:%d inches is just enough"%size)
#         return True
#
# result = try_this_shirt(38)
#
# print("do u wana buy this?",result)

# def log(func):
#     def wrapper(*args,**km):
#         # print('call %s:'%func.__name__)
#         print('wrapper is income')
#         return func(*args,**km)
#     return wrapper
#
# @log
# def now():
#     print("2016-10-19")
#
# now()

# def salesGirl(discount):
#     def expense(method):
#         @functools.wraps(method)
#         def serve(*args):
#             print("salesGirl:Hello,what do you want?",method.__name__)
#             result =  method(*args)
#
#             if result:
#                 print("salesGirl:this shirt you will pay for it $50.as a old user,we promised to discount at %d%%"%discount)
#             else:
#                 print('salesGirl:Well,how about this shirt?')
#             return result
#         return serve
#     return expense
#
# @salesGirl(50)
# def try_this_shirt(size):
#     if size<35:
#         print ("I:%d inches is to small to me"%size)
#         return False
#     else:
#         print ("I:%d inches is just enough"%size)
#         return True
#
# result = try_this_shirt(38)
#
# print("do u wana buy this?",result)
