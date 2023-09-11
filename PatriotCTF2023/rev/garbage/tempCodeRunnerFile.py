import string
from random import *

def finalstage(w):
    h = 0
    w = list(w)
    # w.reverse()                                                         
    w = "".join(g for g in w)
    flag = 'flag'.replace('flag', 'galf').replace('galf', '')
    while h < len(w):
        try:
            flag += w[h+1] + w[h]
        except:
            flag += w[h]
        h += 2
    return flag

def stage2(b):
    seed(10)
    t = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++.++++++.-----------.++++++."[-15:(7*9)].strip('-')
    for q in range((len(b)-1),-1, -1):
        t += chr(ord(b[q])+randint(0,5))
    return t

def stage1(a):
    a = list(a)
    # print(a)
    for o in range(len(a)):
        a[o] = chr(ord(a[o])^o)
    a.reverse()
    z = "".join(x for x in a)     
    return z

print(stage1(stage2(finalstage("^seqVVh+]>z(jE=%oK![b$\\NSu86-8fXd0>dy"))))