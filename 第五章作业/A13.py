#
import numpy as np
import math

def MaxSub():
    b=np.zeros([1,len(arr)])
    b[0,0]=arr[0]#该子段只有一个元素
    sum=0
    for i in range(1,len(arr)):
        if b[0,i-1]>0:
            b[0,i]=b[0,i-1]+arr[i]
        else:
            b[0,i]=arr[i]
        if b[0,i]>sum:
            sum=b[0,i]
    return sum
arr=[5,31,-35,100,-5,-2,10,-3,1,-5,6,-6,-10]
sum=MaxSub()
print('给定数组为：{',arr,'}')
print('最大子段和为',sum)