#!/usr/bin/env python3.5
#-*- coding:utf8-*-

import psutil

phymem = psutil.virtual_memory()

line = "Memory: %5s%% %6s/%s"%(
            phymem.percent,
            str(int(phymem.used/1024/1024))+"M",
            str(int(phymem.total/1024/1024))+"M"
            )
line2=int(phymem.used/1024/1024)
line1=int(phymem.total/1024/1024)

result = int(float(line2/line1)*100)

print(result)
