#!/usr/bin/env python3.5
#-*- coding:utf8 -*-
import re
import urllib.request
import lxml
from bs4 import BeautifulSoup

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    print(str(html,'utf-8'))


getHtml('https://www.so.com/s?ie=utf-8&shb=1&src=home_so.com&q=%E8%8D%89%E6%A6%B4%E9%95%9C%E5%83%8F')
