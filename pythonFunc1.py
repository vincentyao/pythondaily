#!/usr/bin/env python3.5
#-*- coding:utf8 -*-
# import pdb
import os,time,random
#from multiprocessing import Pool
from multiprocessing import Process, Queue

# from random import shuffle
# import subprocess
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

# def test1():
#     print("test1 is running")
#     def test2():
#         print('test2 is running')
#         return 0
#     return 0
# test1()

# def foo(n):
#     s=int(n)
#     pdb.set_trace()
#     assert s!=0,'s is zero'
#     return 10/s
#
#
# def main():
#     foo('0')
#
# if __name__=='__main__':
#         main()

# with open('/usr/bin/env/config.txt','r')as f:
#     for line in f.readlines():
#         print(line.strip())
#
# with open('/usr/image/123.jpeg','rb',encoding='gbk')as jg:
#     jg.read()
# print(os.path.join('/Users/onion/Documents/Python', 'PythonOnion'))
# os.mkdir('/Users/onion/Documents/Python/PythonOnion')
# os.rmdir('/Users/onion/Documents/Python/PythonOnion')
# [filename for t in os.walk(search_dir) for filename in t[2] if search_str in os.path.splitext(filename)[0]]
#
#
# lisvalue=[f for f in os.walk('/Users/onion')if os.path.isfile(f) and os.path.splitext(f)[1]=='.py']
#
# for master in lisvalue:
#     if master == 'download.py':
#         print('hello python,write down the code')

# for i in os.walk('/Users/onion'):
#     print(i)
# filename = tuple([f for f in os.walk('/Users/onion')if os.path.isfile(f)])

# def run_proc(name):
#     print('run child process %s(%s)......'%(name,os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.'%os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child process end!')

# def long_time_task(name):
#     print('Run task %s(%s)...'%(name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#
#     print('Task %s runs %0.2f seconds.'%(name,(end-start)))
#
# if __name__=='__main__':
#     print('Parent process %s.'%os.getpid())
#     p=Pool(5)
#
#     for i in range(5):
#         print(i)
#         p.apply_async(long_time_task,args=(i,))
#     print('Wating for all subprocesses done.....')
#     p.close()
#     p.join()
#     print('all subprocesses done............')

# print('$ nslookup')
# p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
def write(q):
    print('Process to write:%s'%os.getpid())
    for value in ['l','o','v','e','!']:
        print('put value --->%s into queue......'%value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s'%os.getpid())

    while True:
        value=q.get(True)
        print('Get value--->%s from queue.'%value)

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()

    # p=Pool(2)
    #
    # for i in range(2):
    #    if i==0:
    #        p.apply_async(write,args=(i,))
    #    else:
    #        p.apply_async(read,args=(i,))
    #
    # p.close()
    # p.join()
