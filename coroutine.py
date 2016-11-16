#!/usr/bin/env python3.5
#-*- coding:utf8-*-
import asyncio
# def consumer():
#     r=''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[consumer]Consuming %s...'%n)
#         r='200 ok'
#
# def produce(c):
#     c.send(None)
#     n=0
#     while n<5:
#         n=n+1
#         print('[producer]Producing %s...'%n)
#         r=c.send(n)
#         print('[PRODUCer]Consuming return:%s'%r)
#     c.close()
#
#
# c=consumer()
# produce(c)
@asyncio.coroutine
def testAsyncio():
    print('Asyncio testAsyncio!~')
    r=yield from asyncio.sleep(1)
    print('Again!~')

loop=asyncio.get_event_loop()
loop.run_until_complete(testAsyncio())
loop.close()
task=[testAsyncio()]
print(asyncio.wait(task))
