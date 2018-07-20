#coding=utf-8
import time
def getdigit(t):#用于获取整数的位数
    if t == 0:
        return 1
    else:
        c = 0
        while t!= 0:
            t = t/10
            c += 1
        return c
 
 
def count(t):
    count = 0
    # t = input('time: ')
    d1 = getdigit(t)
    while(count < t):
        ncount = t - count
        d2 = getdigit(ncount)
        fillter = ""
        for i in range(d1-d2):#比如如果倒计时从100到99，少了一位，就要补充一个空格才能完全覆盖上一个整数。
            fillter += " "
        formatter = "%d" + fillter + "\r"
        print formatter % ncount,
        time.sleep(1)
        count += 1
    print "done"
