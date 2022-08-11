#
import numpy as np
import math
def minT():
    Ta=0#公式中的T_a
    Tb=0#公式中的T_b
    T=0#公式中的T
    for i in range(0,len(a)):
        if(Ta+a[i]<Tb+b[i] and Ta+a[i]>T):
            Ta+=a[i]
            T=Ta
        elif(Tb+b[i]<Ta+a[i] and Tb+b[i]>T):
            Tb+=b[i]
            T=Tb 
        else:
            if(Ta+a[i]<Tb+b[i] and Ta+a[i]<T):
                Ta+=a[i]
            elif(Tb+b[i]<Ta+a[i] and Tb+b[i]<T):
                Tb+=b[i]
    return T
#global
a=[2,5,7,10,5,2]
b=[3,8,4,11,3,4]
print('a为：',a)
print('b为：',b)
print('最短时间为：',minT())