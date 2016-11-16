#!/usr/bin/env python3.5
#-*- coding:utf8 -*-
import re
import urllib.request
import lxml
from bs4 import BeautifulSoup

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html,"lxml").findAll('a')
    myfile=open("out.txt",'w')
    pat = re.compile(r'href="([^"]*)"')
    pat2 = re.compile(r'http')

    for item in soup:
        h = pat.search(str(item))
        href=h.group(1)

        if pat2.search(href):
            ans=href
        else:
            ans = url+href
        myfile.write(ans)
        myfile.write('\r\n')
        print(ans)
    myfile.close()


getHtml('https://www.so.com/s?ie=utf-8&shb=1&src=home_so.com&q=%E7%88%AC%E5%B1%B1')
